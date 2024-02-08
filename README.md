
https://github.com/sanjai-AK47/Dnsbruter/assets/119435129/7dff92b0-0af4-4755-b229-6a23b366c05e
# Dnsbruter - Asynchronous Dns Bruteforcing Tool


### V1.0.3 features:

- Asynchronous and concurrent bruteforcing
- Manages high level threads and wordlists
- Improved performance and usages in commands of dnsbruter
- User desired console for outputs
- Resolved issues in updating dnsbruter

### Installation



### Method 1:

   ```bash
   pip install git+https://github.com/sanjai-AK47/Dnsbruter.git
   dnsbruter -h
   ```

### Method 2:
   ```bash



   git clone https://github.com/sanjai-AK47/Dnsbruter.git
   cd Dnsbruter
   pip install .
   dnsbruter -h
   ```



https://github.com/sanjai-AK47/Dnsbruter/assets/119435129/ad46775f-1f17-4084-b619-06219e03c93e



## Usage

To start using Dnsbruter, use the following command-line options:

```yaml
dnsbruter -h                                
    ___                ___               _               
   /   \ _ __   ___   / __\ _ __  _   _ | |_   ___  _ __ 
  / /\ /| '_ \ / __| /__\//| '__|| | | || __| / _ \| '__|
 / /_// | | | |\__ \/ \/  \| |   | |_| || |_ |  __/| |   
/___,'  |_| |_||___/\_____/|_|    \__,_| \__| \___||_|   
                                                         

    
                     Author : D.SanjaiKumar @CyberRevoltSecurities

[Version]: Dnsbruter current version v1.0.2 (latest)

[DESCRIPTION]: Dnsbruter is a powerfull tool for dns brutforcing  concurrently

[Usage]: 

    Dnsbruter [options]
    
[OPTIONS]: 

    [INPUT]:
    
            -d   ,  --domain        string   : Domain name for resolving subdomains.
            
            -w   ,  --wordlist      string   : Wordlist path for Dnsbruter.
            
             
    [RATE-LIMIT]: 
        
            -c   ,  --concurrency   int      : Concurrency value for scans.
            
            -rt  ,  --rate-limit    int      : Rate limit value for sending packets to port scans.
                        
    [UPDATES]: 
    
            -up  ,  --updates       command  : Updates the Dnsbruter for larest version (required: pip to be installed) 
            
    [OUTPUT]: 
    
            -o   ,  --output        string   : Filename to save the scans outputs. 
            
    
    [DEBUG]: 
                
            -vr  ,  --version       command  : Shows Version of the Dnsbruter and exits:
            
            -nc  ,  --no-color      command  : Disable the Dnsbruter's colorised CLI outputs and info.
            
            -s   ,  --silent        command  : Only shows outputs and avoid other info. 

```

**INFO:** Dnsbruter is very high in concurrent but high threads causes high loads I recommend use a range of 50-300 for your resolving or the choice is up to you, Dnsbruter is a userfriendly tool and gives good performance, I hope the project
helps in your recon part if you like this project then give a ⭐ to show your support on it.
