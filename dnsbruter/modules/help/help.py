from dnsbruter.modules.logger.logger import blue,bold,white,reset


def help():
    
    print(f"""
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{bold}{white}]{reset}: {bold}{white}dnsbruter is a powerfull tool for asynchronous dns brutforcing and fuzzing with wildcard detection{reset}

{bold}{white}[{reset}{bold}{blue}Usage{reset}{bold}{white}]{reset}: 

    {bold}{white}dnsbruter [options]{reset}
    
{bold}{white}[{reset}{bold}{blue}OPTIONS{reset}{bold}{white}]{reset}: {bold}{white}

    {bold}{white}[{reset}{bold}{blue}INPUT{reset}{bold}{white}]{reset}:{bold}{white}
    
            -d,     --domain               string   : domain name for resolving subdomains.
            -dL,    --domain-list          string   : text file contains domain name for dns bruteforcing.
            -w,     --wordlist             string   : wordlist path for dnsbruter.
            
    {bold}{white}[{reset}{bold}{blue}CONFIG{reset}{bold}{white}]{reset}:{bold}{white}
        
            -rl,    --resolver             string   : filename contains list of resolvers (default: system config).
            -v,     --versbose             command  : increase the verbosity of output.
            -wd,    --wildcard-detect      command  : enable to detect wildcards for found domains.
            -ov,    --override             command  : enable to skip the domain verification and this is not applies to when used BRUT in domain.
            
    {bold}{white}[{reset}{bold}{blue}RATE-LIMIT{reset}{bold}{white}]{reset}: {bold}{white}
        
            -c,     --concurrency            int    : number of concurrency value for dns bruteforcing.             
            -wt,    --wildcard-threds        int    : number of threads values for wildcard detections.
            -rt,    --rate-limit             int    : number of rate limits of DNS queries per second (default: 2000).
            -wrt,   --wildcard-ratelimit     int    : number of rate limits for wild card detection (default: 2000).
            -dl,    --delay                  int    : specify a delay seconds between concurrent DNS quries (default: 1).
            
    {bold}{white}[{reset}{bold}{blue}UPDATES{reset}{bold}{white}]{reset}: {bold}{white}
    
            -up,    --updates              command  : updates the Dnsbruter for latest version (required: pip to be installed). 
            -dc,    --disable-check        command  : disable updates check for dnsbruter.{reset}
            
    {bold}{white}[{reset}{bold}{blue}OUTPUT{reset}{bold}{white}]{reset}: {bold}{white}
    
            -o,     --output               string   : filename to save the scans outputs. 
            -ws,    --wildcard-output      string   : filename to save the found wildcard domains.
            -j,     --json                 command  : enables to display and save output in json format.{reset}
            
    {bold}{white}[{reset}{bold}{blue}DEBUG{reset}{bold}{white}]{reset}: {bold}{white}
    
            -h,     --help                 command  : shows this help message and exits.
            -s,     --silent               command  : only shows essetial outputs and avoid other info.{reset}
""")