# Dnsbruter - Active Subdomain Enumeration Tool

Dnsbruter is a command-line tool designed for active subdomain enumeration through brute-forcing techniques. It helps security researchers and penetration testers discover potential subdomains for a given target domain. The tool allows users to customize their search and provides options for saving and displaying results.


## New Features

Dnsbruter comes with the following features:

-  Define the number of threads to use for faster processing.
-  Define the concurrency for multiple processing for brutforcing subdomains
-  User desired verbose and concise mode to print valid
-  Main focued in concurrecy for brutforcing the subdomains
-  Able to save output Whether its a directory or text file
-  User defined wordlist or built-in wordlist provided for brutforcing subdomains
-  Dnsbruter works like NSE script of [nmap](https://nmap.org/nsedoc/scripts/dns-brute.html) to find subdomains by brutforcing

## Installation

### ALL Users

### Method 1:

   ```bash
   pip install dnsbruter

   dnsbruter -h
   ```

### Method 2:
   ```bash
   git clone https://github.com/sanjai-AK47/Dnsbruter.git
   cd Dnsbruter
   pip install .
   dnsbruter -h
   ```


## Usage

To start using Dnsbruter, use the following command-line options:

```bash
dnsbruter -h                                                                                      
usage: dnsbruter [-h] [-d DOMAIN] [-w WORDLIST] [-o OUTPUT] [-v] [-cn Concise] [-t THREADS] [-C CONCURRENCY]

[INFO]: Discover hidden subdomains effortlessly with Dnsbruter

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        [INFO]: Target name to find hidden subdomains
  -w WORDLIST, --wordlist WORDLIST
                        [INFO]: Wordlist that contains a list of subdomains for bruteforcing
  -o OUTPUT, --output OUTPUT
                        [INFO]: Filename to save the output
  -v, --verbose         [INFO]: Verbose mode will print the valid subdomains that found
  -cn, --concise        [INFO]: Concise mode will print the invalid subdomains that found
  -t THREADS, --threads THREADS
                        [INFO]: Thread level for Multiple Threads
  -C CONCURRENCY, --concurrency CONCURRENCY
                        [INFO]: Concurrency level for Concurrency Process

```

**Example:**


![Screenshot from 2023-10-01 23-12-08](https://github.com/sanjai-AK47/Dnsbruter/assets/119435129/29a1da5a-30a2-4f98-9f50-9768989fd112)

```bash
dnsbruter --domain google.com --output output.txt --verbose  --threads 50 --concurrency 5 --wordlist /path/to/wordlists
```

This command is recommonded for all and will perform perfect active subdomain enumeration on the `google.com` domain using 50 threads + 5 concurrecy multiprocessing, save the results to `output.txt`, display found and valid domains in verbose mode, and print invalid domains during the enumeration process if the concise mode is enabled

Show you love ❤️ and give  ⭐ for [Dnsbruter](https://github.com/sanjai-AK47/Dnsbruter)

We hope this tool proves useful for your subdomain enumeration needs. Happy hacking! :rocket:
