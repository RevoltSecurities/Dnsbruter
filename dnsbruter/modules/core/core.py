import asyncio
from colorama import Fore, Style
import uvloop
import sys
import aiodns
from alive_progress import alive_bar
import random
import socket
import aiofiles
import string
import os
from .wildcard.wildcard import _wildcards_detect

red = Fore.RED
blue = Fore.BLUE
white = Fore.WHITE
green = Fore.GREEN
yellow = Fore.YELLOW
bold = Style.BRIGHT
reset = Style.RESET_ALL



valid = []

wilds = []

async def save(domain, args):
    try:
            if args.output:
                if os.path.isfile(args.output):
                    filename = args.output
                elif os.path.isdir(args.output):
                    filename = os.path.join(args.output, f"dnsbruter_results.txt")
                else:
                    filename = args.output
            else:
                    filename = "dnsbruter_results.txt"
            async with aiofiles.open(filename, "a") as w:
                    await w.write(domain + '\n')

    except KeyboardInterrupt as e:        
        quit()
    except asyncio.CancelledError as e:
        SystemExit
    except Exception as e:
        pass
 

async def _lookup_(subdomain, args, bar, knowhosts, sem, resolver):
    try:
        results = await resolver.query(subdomain, "A")
        await asyncio.sleep(0.00001)
        if results:
            ips = [ip.host for ip in results]
            rips = ', '.join(ip for ip in ips) if args.ipaddress else ""
            
            if set(ips) != set(knowhosts):
                
                if args.no_color:
                    print(f"[+] {subdomain} {rips}")
                else:
                    print(f"{bold}{green}[+]{reset} {bold}{white}{subdomain}{reset} {bold}{yellow}{rips}{reset}")
                valid.append(subdomain)
                await save(f"{subdomain} {rips}", args)
                
    except asyncio.Timeout as e:
        pass
    
    except TimeoutError as e:
        pass
    
    except socket.gaierror as e:
        if args.verbose and not args.silent:
            if args.no_color:
                print(f"[!]: {subdomain} not valid")
            else:
                print(f"[{bold}{red}!{reset}]: {bold}{white}{subdomain} not valid{reset}")
                
    except aiodns.error.DNSError:
        if args.verbose and not args.silent:
            if args.no_color:
                print(f"[!]: {subdomain} not valid")
            else:
                
                print(f"[{bold}{red}!{reset}]: {bold}{white}{subdomain} not valid{reset}")
                
    except KeyboardInterrupt as e:
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}")
        
        SystemExit
        
    except asyncio.CancelledError as e:

        SystemExit
        
    except Exception as e:
        if args.sec_deb:
            print(f"Exception at _lookups_: {e}, {type(e)}")
        
    finally:
        sem.release()
        bar()
        

async def _loader_(args, wordlist, knownhosts, bar, sem, resolver):
    try:
        tasks = []

        domain = args.domain
        
        for word in wordlist:
            
            await sem.acquire()
            
            if "BRUT" in domain:
                subdomain = domain.replace("BRUT", word.strip())
            else:
                subdomain = f"{word.strip()}.{domain}"
                
            task = asyncio.ensure_future(_lookup_(subdomain, args, bar, knownhosts, sem, resolver)) #calling ensure_future so to manage future events for asynchornous purpose
            
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
        
    except KeyboardInterrupt as e:
        SystemExit
        
    except Exception as e:
        if args.sec_deb :
            print(f"Exception at _loader_: {e}, {type(e)}")
        
        
async def __wild_loader(args, resolver, sem, bar):
    try:
        tasks = []
        for domain in valid:
            
            await sem.acquire()
            
            task =  asyncio.ensure_future(_wildcards_detect(domain, args, resolver, sem, bar))
            
            tasks.append(task)
            
        await asyncio.gather(*tasks, return_exceptions=True)
    except KeyboardInterrupt as e:
        SystemExit
        
    except Exception as e:
        if args.sec_deb:
            print(f"Exception at _wild_loader: {e}, {type(e)}")
    
    
        
def _verified_(args):
    try:
        results = socket.gethostbyname(args.domain)
        return results
          
    except socket.gaierror as e:
            pass
    except Exception as e:
        if args.sec_deb:
            print(f"Exception at _verifies_: {e}, {type(e)}")

            
async def _wildcard_(subdomain, args, resolver):
    try:
        random_subdomain = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        random_domain = f"{random_subdomain}.{subdomain}"
        response = await resolver.query(random_domain, 'A')
        ips = [ip.host for ip in response]
        hosts = ips if ips else []
        return hosts
    except aiodns.error.DNSError as e:
        return []
    except TimeoutError as e:
        return []
    
    except Exception as e:
        pass
    
def _setter_(args, wordlist):
    try: 
        if args.resolver:
            try:
                with open(args.resolver, "r") as streamr:
                    resolvers = streamr.read().splitlines()
            except FileNotFoundError as e:
                if not args.no_color:
                    print(f"[{bold}{blue}INF{reset}]: {bold}{white}{args.resolver} no such file exists.{reset}")
                else:
                    print(f"[INF]: {args.resolver} no such file exists.")
                    
                quit()
            except Exception as e:
                pass
        
        nameserver = resolvers if args.resolver else None
                    
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.get_event_loop()
        resolver = aiodns.DNSResolver(loop=loop, rotate=True, nameservers=nameserver)
        
        if "BRUT" not in args.domain:
            hosts = _verified_(args)
        
            if not hosts:
                if not args.override:
                    if not args.no_color:
                        print(f"[{bold}{red}WRN{reset}]: {bold}{white}{args.domain} verification failed due to unable to resolve it, Please use --override to override the verification and brutforce{reset}")
                    else:
                        print(f"[WRN]: {args.domain} verification failed due to unable to resolve it, Please use --override to override the verification and brutforce{reset}")
                
                    quit()
            
        ips = loop.run_until_complete(_wildcard_(args.domain, args, resolver))
        if "BRUT" not in args.domain:
            if ips:
                if not args.no_color:
                    print(f"[{bold}{red}WRN{reset}]: {bold}{white}Wildcard DNS detected for domain {args.domain} and ignoring which have records: {', '.join(ip for ip in ips)} {reset}")
                else:
                    print(f"[WRN]: Wildcard DNS detected for domain '{args.domain}' and ignoring which have records: {', '.join(ip for ip in ips)} ")
            else:
                if not args.no_color:
                
                    print(f"[{bold}{blue}INF{reset}]: {bold}{white}No wildcard DNS detected for domain {args.domain}{reset}")
                else:
                    print(f"[INF]: No wildcard DNS detected for domain {args.domain}")
                
        sem = asyncio.BoundedSemaphore(args.concurrency)
        wdsem = asyncio.BoundedSemaphore(args.wildcard_threads)
        with alive_bar(title=f"{bold}{white}Dnsbruter{reset}", enrich_print=False, total=len(wordlist)) as bar:
            
            loop.run_until_complete(_loader_(args, wordlist, ips, bar, sem, resolver))
            
        if args.wildcard_detect:
            
            if args.no_color:
                print(f"\n[INF]: Detecting wildcards for valid domains")
            else:
                print(f"\n[{bold}{blue}INF{reset}]: {bold}{white}Detecting wildcards for valid domains{reset}")
            
            
            with alive_bar(title=f"{bold}{white}Wildcards Detection{reset}", enrich_print=False, total=len(valid)) as bar:
                loop.run_until_complete(__wild_loader(args, resolver, wdsem, bar))
                    

    except KeyboardInterrupt as e:
        SystemExit
        
    except Exception as e:
        if args.sec_deb:
            print(f"Exception at _setter_: {e}, {type(e)}")



