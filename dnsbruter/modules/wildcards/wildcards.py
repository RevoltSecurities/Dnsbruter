import aiodns
import random
import string
from dnsbruter.modules.logger.logger import logger
import asyncio
from dnsbruter.modules.save.save import save

async def wildcards_detect(subdomain, args, resolver):
    try:
        random_subdomain = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        random_domain = f"{random_subdomain}.{subdomain}"
        response = await resolver.query(random_domain, 'A')
        if response:
            return response
        else:
            return None          
    except aiodns.error.DNSError as e:
        pass
    except TimeoutError as e:
        pass
    except Exception as e:
        if args.verbose:
            logger(f"Exception occured in the wildcards module due to: {e}, {type(e)}", "warn")

async def manage(subdomain: str, args,resolver: aiodns.DNSResolver, sem: asyncio.Semaphore, bar, ratelimit):
    try:
        await asyncio.sleep(args.delay)
        await ratelimit.wait()
        response = await wildcards_detect(subdomain, args, resolver)        
        if response is None:
            return 
        hosts = [host.host for host in response]
        ips = hosts if hosts else []
        result = {"host": subdomain,"ips": ips}
        if args.json:
            print(result)
            if args.wildcard_output:
                await save(args.wildcard_output, result, args.json)
        else:
            print(subdomain)
            if args.wildcard_output:
                await save(args.wildcard_output, subdomain, args.json)
    except Exception as e:
        if args.verbose:
            logger(f"Exception occured in the wild card load manager due to: {e}, {type(e)}", "warn")
    finally:
        sem.release()
        bar()

async def wilds_loader(subdomains: list[str], args, resolver: aiodns.DNSResolver, sem, bar, ratelimit):
    try:
        tasks = []
        for subdomain in subdomains:
            await sem.acquire()
            task = asyncio.create_task(manage(subdomain, args, resolver, sem, bar, ratelimit))
            tasks.append(task)
        await asyncio.gather(*tasks)
    except Exception as e:
        if args.verbose:
            logger(f"Exception occured in the wild card loader module due to: {e}, {type(e)}", "warn")