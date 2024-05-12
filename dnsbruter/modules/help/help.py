from colorama import Fore,Back,Style


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

def all_help():
    
    print(f"""
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{bold}{white}]{reset}: {bold}{white}dnsbruter is a powerfull tool for asynchronous dns brutforcing and fuzzing with wildcard detection{reset}

{bold}{white}[{reset}{bold}{blue}Usage{reset}{bold}{white}]{reset}: 

    {bold}{white}dnsbruter [options]{reset}
    
{bold}{white}[{reset}{bold}{blue}OPTIONS{reset}{bold}{white}]{reset}: {bold}{white}

    {bold}{white}[{reset}{bold}{blue}INPUT{reset}{bold}{white}]{reset}:{bold}{white}
    
            -d   ,  --domain               string   : domain name for resolving subdomains.
            -w   ,  --wordlist             string   : wordlist path for dnsbruter.
            
    {bold}{white}[{reset}{bold}{blue}CONFIG{reset}{bold}{white}]{reset}:{bold}{white}
        
            -rl,    --resolver             string   : filename contains list of resolvers (default: system config)
            -ip,    --ipaddress            command  : shows ip for valid domains that found by dnsbruter
            -v,     --versbose             command  : increase the verbosity of output
            -wd,    --wildcard-detect      command  : enable to detect wildcards for found domains.
            -ov,    --override             command  : enable to skip the domain verification and this is not applies to when used BRUT in domain.
            
    {bold}{white}[{reset}{bold}{blue}RATE-LIMIT{reset}{bold}{white}]{reset}: {bold}{white}
        
            -c   ,  --concurrency            int    : number of concurrency value for dns bruteforcing.             
            -wt  , --wildcard-threds         int    : number of threads values for wildcard detections
            
    {bold}{white}[{reset}{bold}{blue}UPDATES{reset}{bold}{white}]{reset}: {bold}{white}
    
            -up,    --updates              command  : updates the Dnsbruter for latest version (required: pip to be installed) 
            -dc,    --disable-check        command  : disable updates check for dnsbruter{reset}
            
    {bold}{white}[{reset}{bold}{blue}OUTPUT{reset}{bold}{white}]{reset}: {bold}{white}
    
            -o,     --output               string   : filename to save the scans outputs. 
            -ws,    --wildcard-output      string   : filename to save the found wildcard domains.{reset}
            
    {bold}{white}[{reset}{bold}{blue}DEBUG{reset}{bold}{white}]{reset}: {bold}{white}
    
            -h,     --help                 command  : shows this help message and exits.
            -vr,    --version              command  : shows Version of the dnsbruter and exits:
            -nc,    --no-color             command  : disable the dnsbruter's colorised CLI outputs and info.
            -s,     --silent               command  : only shows essetial outputs and avoid other info.{reset}
               
""")
    