import time as t
from colorama import Fore, Back, Style
import asyncio 
import aiofiles
from alive_progress import alive_bar
import os
import random
import aiodns
import async_dns
import dns.asyncresolver
import aiodns



red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

lblue = Fore.LIGHTBLUE_EX

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)




async def save(subdomain,args):
    
    try:
        
        
            if args.output:
        
        
            
                if os.path.isfile(args.output):
                
                    filename = args.output
                
                elif os.path.isdir(args.output):
                
                    filename = os.path.join(args.output, f"{args.domain}_results.txt")
                
                else:
                
                    filename = args.output
            
        
            async with aiofiles.open(filename, "a") as w:
                    
            
                    await w.write(f"{subdomain}" + '\n')

    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}")
        
        quit()
        
    except asyncio.CancelledError as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}\n")
        
        quit()
        
        
    except Exception as e:
                
                pass
            


async def dnb_resolver(sem,subdomain, args, bar):
    
    try:
        
        async with sem:
            
            resolver = aiodns.DNSResolver()
            
            result = await resolver.query(subdomain, "A")

            
            
            if result:
            

            
                if args.no_color:
            
                    print(f"[INF]: {subdomain}")
                
                else:
                
                    print(f"[{bold}{blue}INF{reset}]: {bold}{white}{subdomain}{reset}")
                    
                await save(subdomain, args)
            
                
                
            await asyncio.sleep(args.rate_limit)
                
            
    except (dns.exception.DNSException, async_dns.DNSError, aiodns.error.DNSError):
        
        if args.verbose:
            
            if args.no_color:
            
                print(f"[WRN]: {subdomain} not valid")
                
            else:
                
                print(f"[{bold}{red}WRN{reset}]: {bold}{white}{subdomain} not valid{reset}")
                
    
    
    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}")
        
        quit()
        
    except asyncio.CancelledError as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}\n")
        
        quit()
        
    except TimeoutError as e:
        
        pass
        
    except Exception as e:
                
        pass
        
                
    finally:
        
        bar()
        

    
    
async def dns_thread(wordlist, args):
    
    try:
        
        sem = asyncio.Semaphore(args.concurrency)
        


        with alive_bar(title=f"{bold}{white}Dnsbruter{reset}", enrich_print=False, total=len(wordlist), spinner="classic", bar="classic") as bar:
            
            
                tasks = [dnb_resolver(sem,f"{hostname}.{args.domain}", args, bar)for hostname in wordlist]
            
                await asyncio.gather(*tasks, return_exceptions=False)
        
    except KeyboardInterrupt as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}")
        
        quit()
        
    except asyncio.CancelledError as e:
        
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}\n")
        
        quit()
        
    except Exception as e:
                
                pass