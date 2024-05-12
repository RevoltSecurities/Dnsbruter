#!/usr/bin/env python3
from colorama import Fore,Back,Style
import argparse
import time as t
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

def cli():
    
    try:
        
        parser =  argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False )
        parser.add_argument("-h", "--help", action="store_true")
        parser.add_argument("-d", "--domain", type=str)
        parser.add_argument("-ip", "--ipaddress", action="store_true")
        parser.add_argument("-w", "--wordlist", type=str)
        parser.add_argument("-c", "--concurrency", type=int, default=100)
        parser.add_argument("-up", "--update", action="store_true")
        parser.add_argument("-vr", "--version", action="store_true")
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument("-s", "--silent", action="store_true")
        parser.add_argument("-nc", "--no-color",action="store_true")
        parser.add_argument("-o", "--output", type=str)
        parser.add_argument("-duc", "--disable-check", action="store_true")
        parser.add_argument("-rl", "--resolver", type=str)
        parser.add_argument("-wd", "--wildcard-detect", action="store_true")
        parser.add_argument("-wt", "--wildcard-threads", type=int, default=20)
        parser.add_argument("-ov", "--override", action="store_true")
        parser.add_argument("-ws", "--wildcard-output", type=str)
        parser.add_argument("-sd", "--sec-deb", action="store_true")
        global args 
        return parser.parse_args()
    except argparse.ArgumentError as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Please use the command for more infromation:{reset} {bold}{blue}dnsbruter -h {e}{reset}")
        quit()
        
    except argparse.ArgumentTypeError as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Please use the command for more infromation:{reset} {bold}{blue}dnsbruter -h {e}{reset}")
        quit()
        
    except KeyboardInterrupt as e:
        
        print(f"\n[{bold}{blue}INFO{reset}]: {bold}{white}Dnsbruter exits..{reset}")
        quit()
        
    except Exception as e:
        pass
    
    