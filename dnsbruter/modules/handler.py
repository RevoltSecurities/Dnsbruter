from colorama import Fore,Style
import asyncio
import sys
import uvloop

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

try:
    from dnsbruter.modules.banner.banner import banner
    from dnsbruter.modules.cli.cli import cli
    from dnsbruter.modules.core.core import Dnsbruter
    from dnsbruter.modules.help.help import help
    from dnsbruter.modules.extender.extender import extender
    from dnsbruter.modules.logger.logger import logger,bannerlog
    from dnsbruter.modules.utils.utils import Return_reader,check_perm
    from dnsbruter.modules.version.version import version
except ImportError as e:
    print(f"[{bold}{red}WRN{reset}]: {bold}{white}Import Error occured in Module imports due to: {e}{reset}")
    print(f"[{bold}{blue}INFO{reset}]: {bold}{white}If you are encountering this issue more than a time please report the issues in Dnsbruter Github page{reset}")
    exit(1)

extender()
args = cli()
banner = banner()

git = "v1.0.6"

def git_version():
    try:
        latest = version()
        if latest and latest == git:
            print(f"[{blue}{bold}Version{reset}]:{bold}{white}dnsbruter current version {git} ({green}latest{reset}{bold}{white}){reset}")
        elif latest and latest != git:
            print(f"[{blue}{bold}Version{reset}]: {bold}{white}dnsbruter current version {git} ({red}outdated{reset}{bold}{white}){reset}")
        else:
            logger(f"Unable to get the latest version of dnsbruter", "warn")
    except (KeyboardInterrupt, asyncio.CancelledError):
        exit()
    except Exception as e:
        logger(f"Exception occured in git version checking module due to: {e}, {type(e)}", "warn")
        
        
async def domain_handler(domains: list[str], args):
    try:        
        if args.output:
            await check_perm(args.output)
            
        if args.wildcard_output:
            await check_perm(args.output)
        
        if args.resolver:
            resolver = await Return_reader(args.resolver)
            if resolver is None:
                resolver=None
        else:
            resolver = ["8.8.8.8", "1.1.1.1"]
        
        wordlists = await Return_reader(args.wordlist)
        
        for domain in domains:
            dnsbruter = Dnsbruter(domain, wordlists, args,resolver)
            await dnsbruter.core()
    except (KeyboardInterrupt, asyncio.CancelledError):
        exit()
    except Exception as e:
        logger(f"Exception occured in the domain handler module due to: {e}, {type(e)}", "warn")
    
async def handler():
    try:
        if args.help:
            bannerlog(banner)
            help()
            exit(0)
        if not args.silent:
            bannerlog(banner)
            if not args.disable_check:
                git_version()
    
        if args.domain:
            if not args.wordlist:
                logger(f"dnsbruter requires wordlist to run, please provide wordlist", "warn")
                exit(1)
            await domain_handler([args.domain], args)
            exit(0)
    
        if args.domain_list:
            if not args.wordlist:
                logger(f"dnsbruter requires wordlist to run, please provide wordlist", "warn")
                exit(1)
            domains = await Return_reader(args.domain_list)
            if domains is None:
                exit(1)
            await domain_handler(domains, args)
            exit(0)
            
        if args.update:
            
            latest = version()
            if latest is None:
                logger("unable to get the latest version of dnsbruter, please try to update manually", "warn")
                
            if latest and latest == git:
                logger("dnsbruter is already in latest version", "update")
                exit(1)
            logger("Updating Dnsbruter to latest version, please wait")
            process = await asyncio.create_subprocess_exec(
            "pip", "install", "-U", "git+https://github.com/RevoltSecurities/Dnsbruter", "--break-system-packages",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            if process.returncode == 0:
                logger("successfully updated dnsbruter to latest version", "update")
                exit(0)
            else:
                logger("unable to update dnsbruter to its latest version, please try to update manually", "warn")
                exit(1)
            
        if sys.stdin.isatty():
            logger("no input provided for dnsbruter", "warn")
            exit(1)
        else:
            if not args.wordlist:
                logger(f"dnsbruter requires wordlist to run, please provide wordlist", "warn")
                exit(1)
            domains=[]
            for domain in sys.stdin:
                if domain:
                    domain = domain.strip()
                    domains.append(domain)
            await domain_handler(domains, args)
            exit(0)
    except (KeyboardInterrupt, asyncio.CancelledError):
        exit()
    except Exception as e:
        logger(f"Exception occured in the main handler module due to: {e}, {type(e)}", "warn")
        
def Main():
    try:
        if sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        else:
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(handler())
    except (KeyboardInterrupt, asyncio.CancelledError):
        exit(1)
