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
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{bold}{white}]{reset}: {bold}{white}Dnsbruter is a powerfull tool for dns brutforcing  concurrently{reset}

{bold}{white}[{reset}{bold}{blue}Usage{reset}{bold}{white}]{reset}: 

    {bold}{white}Dnsbruter [options]{reset}
    
{bold}{white}[{reset}{bold}{blue}OPTIONS{reset}{bold}{white}]{reset}: {bold}{white}

    {bold}{white}[{reset}{bold}{blue}INPUT{reset}{bold}{white}]{reset}:{bold}{white}
    
            -d   ,  --domain        string   : Domain name for resolving subdomains.
            
            -w   ,  --wordlist      string   : Wordlist path for Dnsbruter.
            
             
    {bold}{white}[{reset}{bold}{blue}RATE-LIMIT{reset}{bold}{white}]{reset}: {bold}{white}
        
            -c   ,  --concurrency   int      : Concurrency value for scans.
            
            -rt  ,  --rate-limit    int      : Rate limit value for sending packets to port scans.
                        
    {bold}{white}[{reset}{bold}{blue}UPDATES{reset}{bold}{white}]{reset}: {bold}{white}
    
            -up  ,  --updates       command  : Updates the Dnsbruter for larest version (required: pip to be installed) {reset}
            
    {bold}{white}[{reset}{bold}{blue}OUTPUT{reset}{bold}{white}]{reset}: {bold}{white}
    
            -o   ,  --output        string   : Filename to save the scans outputs. {reset}
            
    
    {bold}{white}[{reset}{bold}{blue}DEBUG{reset}{bold}{white}]{reset}: {bold}{white}
                
            -vr  ,  --version       command  : Shows Version of the Dnsbruter and exits:
            
            -nc  ,  --no-color      command  : Disable the Dnsbruter's colorised CLI outputs and info.
            
            -s   ,  --silent        command  : Only shows outputs and avoid other info. {reset}
               
""")
    