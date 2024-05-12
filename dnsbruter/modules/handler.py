from colorama import Fore,Back,Style
import os
import random
import asyncio
import subprocess

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
    from .core.core import _setter_
    from .version.version import update_version, check_version
    from .banner.banner import banner
    from .wordlist.wordlist import wordlist
    from .verify.verify import verify
except ImportError as e:
    
    print(f"[{bold}{red}WRN{reset}]: {bold}{white}Import Error occured in Module imports due to: {e}{reset}")
    print(f"[{bold}{blue}INFO{reset}]: {bold}{white}If you are encountering this issue more than a time please report the issues in Dnsbruter Github page.. {reset}")
    quit()
    
        
args = cli()
banners = banner()

def updateme():
    
    latest = check_version()
    version = "v1.0.4"
    pypi="1.0.5"
    if latest == version:
        print(f"[{blue}{bold}Update{reset}]:{bold}{white}dnsbruter already in latest version{reset}")
        exit()
    else:
        url=update_version()
        
        subprocess.run(["pip", "install", f"{url}", "--compile", "--no-deps", "--break-system-packages", "--force-reinstall"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pypilatest = verify("dnsbruter")
        if pypi != pypilatest:
            print(f"[{bold}{red}WRNP{reset}]: {bold}{white}Update failed due to unknow exception please update it manually.{reset}")
            quit()
            

def version():
    
    latest = check_version()
    version = "v1.0.4"
    if latest == version:
        print(f"[{blue}{bold}Version{reset}]:{bold}{white}dnsbruter current version {version} ({green}latest{reset}{bold}{white}){reset}")
    else:
        print(f"[{blue}{bold}Version{reset}]: {bold}{white}dnsbruter current version {version} ({red}outdated{reset}{bold}{white}){reset}")
        

def help():
    all_help()
    quit()
    
def get_version():
    version()
    quit()
    
    
def domain_manager(args):
    
    if args.wordlist:
        wordlists = wordlist(args.wordlist)
        
        _setter_(args, wordlists)
    else:
        if args.no_color:
            print(f"[WRN]: Please provide a wordlists for dnsbruter")
        else:
            print(f"[{bold}{red}WRN{reset}]: {bold}{white}Please provide a wordlists for dnsbruter{reset}")
    

def handler():
     
    global args
    
    if not args.silent:
        print(f"{bold}{random_color}{banners}{reset}")
            
    if args.help:
        help()
        quit()
        
    if args.version:
        get_version()
        quit()
        
    if not args.disable_check:
        if not args.silent:
            version()
        
    if args.update:
        
        updateme()
        quit()
            
        
    if args.domain:
        
        extender()
        
        if not args.wordlist:
            
            if args.no_color:
                print(f"[WRN]: Please specify a wordlist for Dnsbruter")
            else:
                print(f"[{bold}{red}WRN{reset}]: {bold}{white}Please give a wordlist for Dnsbruter{reset}")
            quit()
            
        domain_manager(args)
        
        
def Main():
    handler()
            
            
        