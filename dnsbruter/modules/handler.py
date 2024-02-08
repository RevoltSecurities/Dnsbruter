import asyncio
from colorama import Fore,Back,Style
import os
import random


red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)

try:
    
    from .help.help import all_help
    from .extender.extender import extender
    from .cli.cli import cli
    from .core.core import dns_thread
    from .version.version import update_version, check_version
    from .banner.banner import banner
    from .wordlist.wordlist import wordlist
    
except ImportError as e:
    
    print(f"[{bold}{red}INFO{reset}]: {bold}{white}Import Error occured in Module imports due to: {e}{reset}")
    
    print(f"[{bold}{blue}INFO{reset}]: {bold}{white}If you are encountering this issue more than a time please report the issues in Dnsbruter Github page.. {reset}")
    
    quit()
    

def updateme():
    
    latest = check_version()
    
    version = "v1.0.2"
    
    if latest == version:
        
        print(f"[{blue}{bold}Update{reset}]:{bold}{white}Dnsbruter already in latest version{reset}")
        
        exit()
        
    else:
        
        url=update_version()
        
        os.system(f"pip install {url}")
        
        print(f"[{blue}{bold}Update{reset}]: {bold}{white}Please check once manually for Dnsbruter latest version{reset}")
        
        quit()
        

def version():
    
    latest = check_version()
    
    version = "v1.0.2"
    
    if latest == version:
        
        print(f"[{blue}{bold}Version{reset}]:{bold}{white}Dnsbruter current version {version} ({green}latest{reset}{bold}{white}){reset}")
        
    else:
        
        print(f"[{blue}{bold}Version{reset}]: {bold}{white}Dnsbruter current version {version} ({red}outdated{reset}{bold}{white}){reset}")
        

def help():
    
        
    all_help()
        
    quit()
    

def get_version():
    
    version()
    
    quit()
    
def domain_manager(args):
    
    if args.wordlist:
        
        wordlists = wordlist(args.wordlist)
        
        
        asyncio.run(dns_thread(wordlists, args))
    
    
    

def handler():
     
    global args
    
    args = cli()
    
    banners = banner()
    
    if not args.silent:
        
        print(f"{bold}{random_color}{banners}{reset}")
    
    if not args.version:
        
        if not args.silent:
        
            version()
            
    if args.help:
        
        help()
            
    if args.version:
        
        get_version()
        
    
    if args.domain:
        
        extender()
        
        if not args.wordlist:
            
            if args.no_color:
                
                print(f"[WRN]: Please give a wordlist for Dnsbruter")
                
            else:
                
                print(f"[{bold}{red}WRN{reset}]: {bold}{white}Please give a wordlist for Dnsbruter{reset}")
                
            quit()
            
        domain_manager(args)
            
            
        