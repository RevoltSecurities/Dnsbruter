#!/usr/bin/python3
import argparse
import dns.resolver 
import requests 
import time as t
from colorama import Fore, Back, Style
from multiprocessing.pool import ThreadPool as Pool
from concurrent.futures import ThreadPoolExecutor
import threading
import random
import os



red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
mixed = Fore.RED + Fore.BLUE
white = Fore.WHITE
reset = Style.RESET_ALL
colors = [red, green, yellow, cyan, blue]

random_color = random.choice(colors)
subdomains_list = []


parser = argparse.ArgumentParser(description=f"[{blue}INFO{reset}]: Discover hidden subdomains effortlessly with Dnsbruter")

parser.add_argument("-d", "--domain", help=f"[{blue}INFO{reset}]: Target name to find hidden subdomains", type=str)

parser.add_argument("-w", "--wordlist", help=f"[{blue}INFO{reset}]: Wordlist that contains a list of subdomains for bruteforcing", type=str)

parser.add_argument("-o", "--output", help=f"[{blue}INFO{reset}]: Filename to save the output", type=str)

parser.add_argument("-v", "--verbose", help=f"[{blue}INFO{reset}]: Verbose mode will print the valid subdomains that found", action="store_true")

parser.add_argument("-cn", "--concise", help=f"[{blue}INFO{reset}]: Concise mode will print the invalid subdomains that found", action="store_true")

parser.add_argument("-t", "--threads", help=f"[{blue}INFO{reset}]: Thread level for Multiple Threads", type=int)

parser.add_argument("-C", "--concurrency", help=f"[{blue}INFO{reset}]: Concurrency level for Concurrency Process", type=int)

args = parser.parse_args()


banner = ''' 
    ____             ____             __           
   / __ \____  _____/ __ )_______  __/ /____  _____
  / / / / __ \/ ___/ __  / ___/ / / / __/ _ \/ ___/
 / /_/ / / / (__  ) /_/ / /  / /_/ / /_/  __/ /    
/_____/_/ /_/____/_____/_/   \__,_/\__/\___/_/     
                                                   
                                                   
                            Author: D.Sanjai Kumar

'''
def version_check():
    
    version = "v1.0.1"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Dnsbruter/releases/latest"
    
    try:
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                
                print(f"[{blue}Version{reset}]: Dnsbruter current version {version} is ({green}latest{reset})")
                
                t.sleep(1)
                
            else:
                
                print(f"[{blue}Version{reset}]: Dnsbruter current version {version} is ({red}outdated{reset})")
                
                print(f"[{blue}INFO{reset}]: New version of Dnsbruter is detected update the latest versions by github or pip")
                
                print(f"[{green}Command{reset}]: pip install --upgrade dnsbruter")

                
                
                
        else:
            
            pass
                
    except Exception as e:
        
        pass




def dns_resolver(subdomain):
    

        try:
        
            searches = dns.resolver.resolve(f"{subdomain}", "A")
            
            if searches:
                
                if args.verbose:
                    
                    print(f"[{green}FOUND{reset}]: {subdomain}")

                    
                    
                    save_subdomain(subdomain)
            else:
                
                if args.concise:
                    
                    print(f"[{red}InValid{reset}]: {subdomain}")
                    
        except Exception as e:
            
            if args.concise:
                
                print(f"[{red}InValid{reset}]: {subdomain}")
                
                
def save_subdomain(subdomain):
    
    if args.output:
            
            if os.path.isfile(args.output):
                
                filename = args.output
                
            elif os.path.isdir(args.output):
                
                filename = os.path.join(args.output, f"{args.domain}.subdomains.txt")
                
            else:
                
                filename = args.output
                
            if not args.output:
            
                filename = f"{args.domain}.subdomains.txt"
        
            with open(filename, "a") as w:
            
                w.write(f"{subdomain}\n")


def check_essentials():
    
    print(f"{random_color}{banner}{reset}")
    
    version_check()
    
    if args.domain:
        
        print(f"[{blue}INFO{reset}]: Dnsbruter started subdomain brutforcing for {args.domain}")
        
    elif not args.domain:
        
        print(f"[{red}INFO{reset}]: Target not given for Dnsbruter for brutforcing subdomains ")
        
        exit()
        
    else:
        
        print(f"[{red}INFO{reset}]: Target not given for Dnsbruter for brutforcing subdomains ")
        
        exit()
        
    if args.verbose:
        
        print(f"[{blue}INFO{reset}]: Verbose Enabled by user. Now found subdomains will print to the console.")
        
    else:
        
        print(f"[{blue}INFO{reset}]: Verbose Not Enabled by user. Now found subdomains will not print to the console.")
        
    if args.concise:
        
        print(f"[{blue}INFO{reset}]: Concise Enabled by user. Now invalid subdomains will print to the console.")
        
    else:
        
        print(f"[{blue}INFO{reset}]: Concise Not Enabled by user. Now invalid subdomains will not print to the console.")


    if args.concurrency:
        
        if args.concurrency > 5:
            
            print(f"[{red}CAUTION{reset}]: You have enabled thread level {args.concurrency}, which is more than 5 and that may cause damage to the OS.")
            
            print(f"[{red}CAUTION{reset}]: Keeping high Thread Concurrency is at your own risk.")
        else:
            
            print(f"[{blue}INFO{reset}]: You have Concurrency level {args.concurrency}, which can perform well without affecting your OS.")
    else:
        
        args.concurrency = 5
        
        print(f"[{blue}INFO{reset}]: You haven't enabled Concurrency  level. Continuing with Concurrency level {args.concurrency}.")
        
    
    if args.threads:
        
        if args.threads > 50:
            
            print(f"[{red}CAUTION{reset}]: You have enabled thread level {args.threads}, which is more than 50 and may cause damage to the OS.")
            
            print(f"[{red}CAUTION{reset}]: Keeping high Thread level is at your own risk.")
            
        else:
            
            print(f"[{blue}INFO{reset}]: You have Thread level {args.threads}, which can perform well without affecting your OS.")
            
    else:
        
        args.threads = 40
        
        print(f"[{blue}INFO{reset}]: You haven't enabled Thread level. Continuing with Thread level {args.threads}.")
        
    
    if args.wordlist:
        
        try:
            
            with open(args.wordlist, "r") as r:
                
                read = r.read().splitlines()
                
                for subdomain in read:
                    
                    subdomains_list.append(f"{subdomain.strip()}.{args.domain}")
                    
            print(f"[{blue}INFO{reset}]: Loading the wordlist from {args.wordlist}")
            
            print(f"[{blue}INFO{reset}]: Total subdomains loaded for brutforce {len(subdomains_list)}")
            
        except FileNotFoundError as e:
            
            print(f"[{red}INFO{reset}]: Wordlist file not found. Dnsbruter continuing with built-in wordlist.")
            
            with open("wordlists.txt", "r") as r:
                
                read = r.read().splitlines()
                
            for subdomain in read:
                
                subdomains_list.append(f"{subdomain.strip()}.{args.domain}")
                
        except Exception as e:
            
            print(f"[{red}INFO{reset}]: Unknown error occured in Dnsbruter please report this is issues in Dnsbruter github page")
            
            
            
    else:
        print(f"[{red}INFO{reset}]: Wordlist to brute force not given by the user. Continuing with the built-in wordlist.")
        
        with open("wordlists.txt", "r") as r:
            
            read = r.read().splitlines()
            
        for subdomain in read:
                
            subdomains_list.append(f"{subdomain.strip()}.{args.domain}")
            
            
def Threader():
    
    Threads = min(args.threads*args.concurrency, len(subdomains_list))
    
    for i in range(0, len(subdomains_list), Threads):
        
        Thread_holder = []
        
        for subdomain in subdomains_list[i:i+Threads]:
            
            thread = threading.Thread(target=dns_resolver, args=(subdomain,))
            
            Thread_holder.append(thread)
            
            thread.start()
            
        for thread in Thread_holder:
            
            thread.join()
            
def main():
    
    check_essentials()
    
    Threader()
        
    

if __name__ == "__main__":
    
    
    main()
    
    
    
    
    