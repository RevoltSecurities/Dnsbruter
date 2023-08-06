import argparse
import dns.resolver 
import requests
import threading
from colorama import Fore,Back,Style
import time as t

red =  Fore.RED

green = Fore.GREEN

yellow = Fore.YELLOW

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

subdomains_list = []



parser = argparse.ArgumentParser(description=f"[{green}INFO{reset}]: A Subdomain Brutforcer for active subomain enumeration")

parser.add_argument("-d", "--domain", help=f"[{blue}INFO{reset}]: Domain name for active subdomain enumeration", type=str)

parser.add_argument("-w", "--wordlist", help=f"[{blue}INFO{reset}]: Wordlist that contains list of subdomain for brutforcing", type=str)

parser.add_argument("-o", "--output", help=f"[{blue}INFO{reset}]: Filename to save the output", type=str)

parser.add_argument("-v", "--verbose", help=f"[{blue}INFO{reset}]: Enabling verbose will print the found subdomain", action="store_true")

parser.add_argument("-t", "--threads", help=f"[{blue}INFO{reset}]: Thread level to make the process to Multiprocess", type=int)

parser.add_argument("-i", "--invalid", help=f"[{blue}INFO{reset}]: Enabling invalid will print the invalid or not found subdomains", action="store_true")



args = parser.parse_args()


banner = ''' 

    ____             ____             __           
   / __ \____  _____/ __ )_______  __/ /____  _____
  / / / / __ \/ ___/ __  / ___/ / / / __/ _ \/ ___/
 / /_/ / / / (__  ) /_/ / /  / /_/ / /_/  __/ /    
/_____/_/ /_/____/_____/_/   \__,_/\__/\___/_/     
                                                   
                                                   
                            Author: D.Sanjai Kumar

'''



        
def get_version():
    
    version = "v1.0.0"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Dnsbruter/releases/latest"
    
    try:
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                message = "latest"
                
                print(f"[{blue}Version{reset}]: Dnsbruter current version {version} ({green}{message}{reset})")
                
                t.sleep(1)
                
            else:
                
                message ="outdated"
                
                print(f"[{blue}Version{reset}]: Dnsbruter current version {version} ({red}{message}{reset})")
                
                t.sleep(1)
                
        else:
            
            pass
                
    except Exception as e:
        
        pass



def check_essentials_one_domain():
    
    
    print(f"{cyan}{banner}{reset}")
    
    get_version()

    if args.domain: 

        print(f"[{green}INFO{reset}]: Active Subdomain enumeration started for {args.domain}")
    
    elif not args.domain: 

        print(f"[{red}INFO{reset}]: User not given domain name for Active Subdomain enumeration")

        exit()

    else:

        print(f"[{red}INFO{reset}]: User not given domain name for Active Subdomain enumeration")

        exit()
        
    if args.wordlist:
        
        try:
            
            
            
            with open(args.wordlist, "r") as r:
                
                read = r.read().splitlines()
                
                for subdomain in read:
                    
                    subdomains_list.append(f"{subdomain.strip()}.{args.domain}")
        
            print(f"[{green}INFO{reset}]: Loading the file from {args.wordlist}")
            
        except Exception as e:
            
            print(f"[{red}INFO{reset}]: Wordlist file not found Check the file path or file exists")
            
            exit()
        
    else:
        
        print(f"[{red}INFO{reset}]: Wordlist to brutforce not given by user continuing with the built-in wordlist")
        
        with open("wordlists.txt", "r") as r:
                
                read = r.read().splitlines()
                
                for subdomain in read:
                    
                    subdomains_list.append(f"{subdomain.strip()}.{args.domain}")
        
                    
        
        
    if args.verbose:
        
        print(f"[{green}INFO{reset}]: Verbose Enabled by user. Now found subdomains will print to console")
        
    else:
        
        print(f"[{blue}INFO{reset}]: Verbose Not Enabled by user. Now found subdomains will not print to console")
        
    if args.invalid:
        
        print(f"[{green}INFO{reset}]: Invalidater Enabled by user. Now Invalid subdomains will print to the console")
        
    else:
        
        print(f"[{blue}INFO{reset}]: Invalidater Not Enabled by user. Now Invalid subdomains will not print to the console")
        
    
        
        
    if args.threads:
        
        if args.threads > 100:
            
            print(f"[{red}CAUTION{reset}]: You are enabled thread level {args.threads} which is more than 100 may cause damage to OS")
            print(f"[{red}CAUTION{reset}]: You are Keeping high Thread level at your own risk")
            
        else:
            
            print(f"[{green}INFO{reset}]: You are Thread level {args.threads} which can perform good without affecting your OS ")
            
    else:
        
        args.threads = 50
        
        print(f"[{blue}INFO{reset}]: You're not enabled Thread. So continuing with Thread level {args.threads} ")
        
    
    if args.output:
        
        
        print(f"[{green}INFO{reset}]: Output will be saved in this file {args.output} ")
        
    else:
        
        print(f"[{blue}INFO{reset}]: Output file not given output will be saved automatically ")
        
        
        
        
def resolver(subdomain):
    
    
    try:
        
        dns.resolver.timeout = 1
        
        dns.resolver.lifetime = 1
    
        searches = dns.resolver.resolve(f"{subdomain}", "A")
        
        if searches:
            
            if args.verbose:
                
                print(f"[{green}FOUND{reset}]: {subdomain}")
                
                if args.output:
                    
                    with open(args.output, "a") as w:
                        
                        w.write(subdomain)
                        
                else:
                    
                    filename = f"{args.domain}_results.txt"
                    
                    with open(filename, "a") as w:
                        
                        w.write(f"{subdomain}\n")
                
                
            else:
                
                if args.output:
                    
                    with open(args.output, "a") as w:
                        
                        w.write(f"{subdomain}\n")
                        
                else:
                    
                    filename = f"{args.domain}_results.txt"
                    
                    with open(filename, "a") as w:
                        
                        w.write(subdomain)
        else:
            
            if args.invalid:
                
                print(f"[{red}InValid{reset}]: {subdomain}")
                
            else:
                
                pass
                
                
        
    except Exception as e:
        
        if args.invalid:
                
                print(f"[{red}InValid{reset}]: {subdomain}")
        else:
            
            pass
    
    
def Threader():
    
    threads = []
    
    for subdomain in subdomains_list:
        
        thread = threading.Thread(target=resolver, args=(subdomain,))
        
        threads.append(thread)
        
        thread.start()
        
    for threader in threads:
        
        threader.join()



if __name__ == "__main__":
    
    check_essentials_one_domain()
    
    Threader()
    
    