from colorama import Fore,Style,init
import sys
import random
init()

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


def logger(message: str, level="info"):
    if level == "info":
        leveler = f"{bold}{blue}INFO{reset}"
    elif level == "warn":
        leveler = f"{bold}{red}WARN{reset}"
    elif level == "error":
        leveler = f"{bold}{red}ERR{reset}"
    elif level == "verbose":
        leveler = f"{bold}{green}VRB{reset}"
    else:
        leveler = f"{bold}{green}{level.upper()}{reset}"
        
    print(f"[{bold}{blue}{leveler}{reset}]: {bold}{white}{message}{reset}", file=sys.stderr)
    
def bannerlog(banner: str):
    print(banner, file=sys.stderr)
    
def stdinlog(message):
    print(message)