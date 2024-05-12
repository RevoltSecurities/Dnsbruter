from colorama import Fore, Style
import aiodns
import random
import aiofiles
import string
import os
import asyncio

red = Fore.RED
blue = Fore.BLUE
white = Fore.WHITE
green = Fore.GREEN
yellow = Fore.YELLOW
bold = Style.BRIGHT
reset = Style.RESET_ALL

async def save(domain, args):
    try:
            if args.output:
                if os.path.isfile(args.wildcard_output):
                    filename = args.wildcard_output
                elif os.path.isdir(args.wildcard_output):
                    filename = os.path.join(args.wildcard_output, f"dnsbruter_wildcards.txt")
                else:
                    filename = args.wildcard_output
            else:
                    filename = "dnsbruter_wildcards.txt"
                    
            async with aiofiles.open(filename, "a") as w:
                    await w.write(domain + '\n')

    except KeyboardInterrupt as e:        
        quit()
    except asyncio.CancelledError as e:
        SystemExit
    except Exception as e:
        pass


async def _wildcards_detect(subdomain, args, resolver, sem, bar):
    try:
        random_subdomain = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        random_domain = f"{random_subdomain}.{subdomain}"
        response = await resolver.query(random_domain, 'A')
        if response:
            if args.no_color:
                print(f"[!]: {subdomain}")
            else:
                print(f"[{bold}{green}+{reset}]: {bold}{white}{subdomain}{reset}")
                
            await save(subdomain, args)
            
    except aiodns.error.DNSError as e:
        pass
    except TimeoutError as e:
        pass
    except Exception as e:
        if args.sec_deb:
            print(f"at wildcards bunch: {e}, {type(e)}")
    finally:
        sem.release()
        bar()
    