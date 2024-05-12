
# Dnsbruter - Asynchronous Dns Bruteforcing Tool

Dnsbruter an Asynchronous Dns bruteforcing and Fuzzing  Tool for Penetration Testers and Ethical hackers.
it used to bruteforce and fuzz for domain names in any position of input using BRUT word in it.

![GitHub last commit](https://img.shields.io/github/last-commit/RevoltSecurities/Dnsbruter) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/RevoltSecurities/Dnsbruter) [![GitHub license](https://img.shields.io/github/license/RevoltSecurities/Dnsbruter)](https://github.com/RevoltSecurities/Dnsbruter/blob/main/LICENSE) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/d-sanjai-kumar-109a7227b/)

### features:
<h1 align="center">
  <img src="https://github.com/RevoltSecurities/Dnsbruter/assets/119435129/51cb47ce-2a9d-49f5-a547-bae184a5c19e" width="700px">
  <br>
</h1>

- Asynchronous and concurrent dns bruteforcing.
- Supports both dns brutforcing and fuzzing.
- Manages high level threads.
- Manages high loads wordlist.
- Enhanced asynchronous performance better than before.
- Wildcard detection for found domain.



## Usage

To start using Dnsbruter, use the following command-line options:

```yaml
dnsbruter -h                                
     __              __               __            
 ___/ /  ___   ___  / /   ____ __ __ / /_ ___   ____
/ _  /  / _ \ (_-< / _ \ / __// // // __// -_) / __/
\_,_/  /_//_//___//_.__//_/   \_,_/ \__/ \__/ /_/   
                                                    

                    @RevoltSecurities


[DESCRIPTION]: dnsbruter is a powerfull tool for asynchronous dns brutforcing and fuzzing with wildcard detection

[Usage]: 

    dnsbruter [options]
    
[OPTIONS]: 

    [INPUT]:
            -d   ,  --domain               string   : domain name for resolving subdomains.
            -w   ,  --wordlist             string   : wordlist path for dnsbruter.
            
    [CONFIG]:
            -rl,    --resolver             string   : filename contains list of resolvers (default: system config)
            -ip,    --ipaddress            command  : shows ip for valid domains that found by dnsbruter
            -v,     --versbose             command  : increase the verbosity of output
            -wd,    --wildcard-detect      command  : enable to detect wildcards for found domains.
            -ov,    --override             command  : enable to skip the domain verification and this is not applies to when used BRUT in domain.
            
    [RATE-LIMIT]: 
            -c   ,  --concurrency            int    : number of concurrency value for dns bruteforcing.             
            -wt  , --wildcard-threds         int    : number of threads values for wildcard detections
            
    [UPDATES]: 
            -up,    --updates              command  : updates the Dnsbruter for latest version (required: pip to be installed) 
            -dc,    --disable-check        command  : disable updates check for dnsbruter
            
    [OUTPUT]: 
            -o,     --output               string   : filename to save the scans outputs. 
            -ws,    --wildcard-output      string   : filename to save the found wildcard domains.
            
    [DEBUG]: 
            -h,     --help                 command  : shows this help message and exits.
            -vr,    --version              command  : shows Version of the dnsbruter and exits:
            -nc,    --no-color             command  : disable the dnsbruter's colorised CLI outputs and info.
            -s,     --silent               command  : only shows essetial outputs and avoid other info.

```

### Uses of Dnsbruter:
Dnsbruter is highly asynchronous and concurrent dns brutforcing and fuzzing tool . Dnsbruter can be used to bruteforce for valid subdomains and also can be used to FUZZ in any position the domain for example the normal bruteforce domain can be passed as
`admin.google.com` and default dnsbruter checks for domain is valid and it have wildcard dns are not to ensure get accurate results and the Fuzz method domain can be passed for example `adminBRUT.google.com` and the BRUT word is used for Fuzz method like we use FUZZ in tools like `ffuf` and when BRUT is passed in domain the Dnsbruter will not checks for valid domain because for fuzzing and this also applies to wildcard records of it. Dnsbruter can run more concurrent and powerfull but its all depends on the users **network speed** and resolvers used. Dnsbruter is runs with ligth weight threads which is a advantage for low end **VPS** users and can handle high loads wordlist without causing any system CPU's loads so Dnsbruter supports well in your low end system and it will try best not crash your network like `puredns` so it will be good alternative tool for you.

<h1 align="center">
  <img src="https://github.com/RevoltSecurities/Dnsbruter/assets/119435129/a260df97-17fb-4cd5-8017-687697fcd030" width="2000px">
  <br>
</h1>

### Installation:
Dnsbruter can be installed easily with tools using `pip` & `pipx` to install the tool easily and follow the below method of installation.

#### pip 
requires pip need to be installed with latest python version
```code
pip install --no-deps --force-reinstall --break-system-packages git+https://github.com/RevoltSecurities/Dnsbruter.git
```

#### pipx
requires pipx to be installed with latest python version
```pipx
pipx install git+https://github.com/RevoltSecurities/Dnsbruter.git --break-system-packages
```

### About:
The Dnsbruter is a open source tool for all Security Researchers and CyberSecurity people to use in their security assesments and information gathering process which helps them lot and We encourage open source contributor to help for Dnsbruter
updates and We hope this tools helps everyone if this tool helps please show you support by giving ⭐ to Dnsbruter ⚡.

