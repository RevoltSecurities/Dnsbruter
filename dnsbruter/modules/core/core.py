import asyncio
import aiodns
from alive_progress import alive_bar
import socket
from dnsbruter.modules.logger.logger import logger, bold, white, reset, stdinlog
from dnsbruter.modules.wildcards.wildcards import wildcards_detect, wilds_loader
from asynciolimiter import Limiter
from dnsbruter.modules.save.save import save

class Dnsbruter:
    def __init__(self, domain: str, wordlists: str, args, resolver=None):
        self.domain = domain
        self.wordlists = wordlists
        self.args = args
        self.resolver = resolver
        self.valid = []

    async def dnslookup(self, subdomain, query="A"):
        try:
            results = await self.resolver.query(subdomain, query)
            if results:
                return results
        except (KeyboardInterrupt, asyncio.CancelledError):
            exit(1)
        except (aiodns.error.DNSError, socket.gaierror):
            return None
        except Exception as e:
            print(e)
            return None

    async def manage(self, subdomain, sem, knownips, bar, limiter):
        try:
            await asyncio.sleep(self.args.delay)
            await limiter.wait()
            response = await self.dnslookup(subdomain)
            if response is None:
                return
            hosts = [host.host for host in response]
            ips = hosts if hosts else []
            if set(ips) != set(knownips):
                result = {"host": subdomain, "ips": ips}
                if self.args.json:
                    stdinlog(result)
                    if self.args.output:
                        await save(self.args.output, result, self.args.json)
                else:
                    stdinlog(subdomain)
                    if self.args.output:
                        await save(self.args.output, subdomain, self.args.json)
                self.valid.append(subdomain)
        except (KeyboardInterrupt, asyncio.CancelledError):
            exit(1)
        except Exception as e:
            logger(f"Exception occurred in the load manager module due to: {e}, {type(e)}", "warn")
        finally:
            sem.release()
            bar()

    async def loaders(self, sem, knownips, bar, limiter):
        try:
            tasks = []
            for word in self.wordlists:
                await sem.acquire()
                if "BRUT" in self.domain:
                    subdomain = self.domain.replace("BRUT", word.strip())
                else:
                    subdomain = f"{word.strip()}.{self.domain}"
                task = asyncio.create_task(self.manage(subdomain, sem, knownips, bar, limiter))
                tasks.append(task)
            await asyncio.gather(*tasks)
        except (KeyboardInterrupt, asyncio.CancelledError):
            exit(1)
        except Exception as e:
            logger(f"Exception occurred in the loader module due to: {e}, {type(e)}", "warn")

    async def gethost(self):
        try:
            resolved = await self.resolver.gethostbyname(self.domain, socket.AF_INET)
            return resolved
        except (KeyboardInterrupt, asyncio.CancelledError):
            exit(1)
        except (aiodns.error.DNSError, socket.gaierror):
            pass
        except Exception as e:
            if self.args.verbose:
                logger(f"Exception occurred in host resolver due to: {e}, {type(e)}")

    async def core(self):
        try:
            loop = asyncio.get_event_loop()
            self.resolver = aiodns.DNSResolver(nameservers=self.resolver, loop=loop, rotate=True)
            limiter = Limiter(rate=self.args.rate_limit / 1)
            wlimiter = Limiter(rate=self.args.wildcard_ratelimit / 1)

            if "BRUT" not in self.domain:
                resolve = await self.gethost()
                if not resolve and not self.args.override:
                    logger(f"Unable to resolve the {self.domain}, please use --override to override the domain resolving", "warn")
                    exit(1)

            response = await wildcards_detect(self.domain, self.args, self.resolver)
            ips = [host.host for host in response] if response else []

            if "BRUT" not in self.domain:
                if response:
                    logger(f"Wildcard DNS records found for {self.domain} and ignoring which have records: {', '.join(ip for ip in ips)}", "verbose")
                else:
                    logger(f"No wildcard DNS records found for {self.domain}", "warn")

            sem = asyncio.Semaphore(self.args.concurrency)
            wdsem = asyncio.Semaphore(self.args.wildcard_threads)

            with alive_bar(title=f"{bold}{white}Dnsbruter{reset}", enrich_print=False, total=len(self.wordlists)) as bar:
                await self.loaders(sem, ips, bar, limiter)

            if self.args.wildcard_detect:
                if self.args.verbose:
                    logger(f"Starting wildcard detection for found subdomains.", "verbose")

                with alive_bar(title=f"{bold}{white}Wildcard Detection{reset}", enrich_print=False, total=len(self.valid)) as bar:
                    await wilds_loader(self.valid, self.args, self.resolver, wdsem, bar, wlimiter)

        except (KeyboardInterrupt, asyncio.CancelledError):
            exit(1)
        except Exception as e:
            logger(f"Exception occurred in the core module due to: {e}, {type(e)}", "warn")
