# Dnsbruter - Asynchronous DNS Bruteforcing Tool

<h1 align="center">
  <img src="img/dnsbruter.webp" alt="Dnsbruter" width="450px">
  <br>
</h1>

Dnsbruter is a lightweight, fast, and smooth asynchronous DNS brute-forcing and fuzzing tool designed for penetration testers, ethical hackers, and anyone conducting active attack surface reconnaissance. This tool helps you discover subdomains and identify vulnerabilities in it.

![GitHub last commit](https://img.shields.io/github/last-commit/RevoltSecurities/Dnsbruter) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/RevoltSecurities/Dnsbruter) [![GitHub license](https://img.shields.io/github/license/RevoltSecurities/Dnsbruter)](https://github.com/RevoltSecurities/Dnsbruter/blob/main/LICENSE) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/d-sanjai-kumar-109a7227b/)

### V1.0.6 Features:

<h1 align="center">
  <img src="https://github.com/RevoltSecurities/Dnsbruter/assets/119435129/51cb47ce-2a9d-49f5-a547-bae184a5c19e" width="700px">
  <br>
</h1>

- **Improved Speed & Efficiency**: Significantly faster and smoother DNS brute-forcing with lightweight resource usage.
- **Memory & Resource Management**: Optimized to handle large-scale DNS scans without consuming excessive system resources.
- **Flexible Input**: Supports both stdin and file-based domain lists for DNS brute-forcing.
- **Concurrency Control**: Rate limiting and concurrency management to ensure stable performance under heavy loads.
- **JSON Output**: Option to save scan results in a structured JSON format for easy integration with other tools.

### Installation:

Dnsbruter can be installed quickly using various methods, including `pip`, `pipx`, and `Docker`. Choose the method that best suits your environment.

#### pip Installation
Ensure you have `pip` installed with the latest version of Python:

```bash
pip install --break-system-packages git+https://github.com/RevoltSecurities/Dnsbruter.git
```

#### pipx Installation
For isolated Python environments, you can use `pipx`:

```bash
pipx install git+https://github.com/RevoltSecurities/Dnsbruter.git
```

#### Docker Installation
For Docker-based environments, build the Docker image using:

```bash
git clone https://github.com/RevoltSecurities/Dnsbruter.git && cd Dnsbruter
sudo docker build -t dnsbruter .
```

**Docker Usage:**

```bash
sudo docker run --rm -it -v /path/to/wordlist.txt:/opt/wordlist.txt -v $(pwd):/output dnsbruter -d google.com -w /opt/wordlist.txt --output /output/test.txt
```

## Usage

To use Dnsbruter, execute the following command to display help options:

```bash
dnsbruter -h
```

This will show you the following available options:

```yaml
dnsbruter -h
       __                    __                     __               
  ____/ /   ____    _____   / /_    _____  __  __  / /_  ___    _____
 / __  /   / __ \  / ___/  / __ \  / ___/ / / / / / __/ / _ \  / ___/
/ /_/ /   / / / / (__  )  / /_/ / / /    / /_/ / / /_  /  __/ / /    
\__,_/   /_/ /_/ /____/  /_.___/ /_/     \__,_/  \__/  \___/ /_/     
                                                                     

                    - RevoltSecurities


[DESCRIPTION]: dnsbruter is a powerfull tool for asynchronous dns brutforcing and fuzzing with wildcard detection

[Usage]: 

    dnsbruter [options]
    
[OPTIONS]: 

    [INPUT]:
    
            -d,     --domain               string   : domain name for resolving subdomains.
            -dL,    --domain-list          string   : text file contains domain name for dns bruteforcing.
            -w,     --wordlist             string   : wordlist path for dnsbruter.
            
    [CONFIG]:
        
            -rl,    --resolver             string   : filename contains list of resolvers (default: system config).
            -v,     --versbose             command  : increase the verbosity of output.
            -wd,    --wildcard-detect      command  : enable to detect wildcards for found domains.
            -ov,    --override             command  : enable to skip the domain verification and this is not applies to when used BRUT in domain.
            
    [RATE-LIMIT]: 
        
            -c,     --concurrency            int    : number of concurrency value for dns bruteforcing.             
            -wt,    --wildcard-threds        int    : number of threads values for wildcard detections.
            -rt,    --rate-limit             int    : number of rate limits of DNS queries per second (default: 2000).
            -wrt,   --wildcard-ratelimit     int    : number of rate limits for wild card detection (default: 2000).
            -dl,    --delay                  int    : specify a delay seconds between concurrent DNS quries (default: 1).
            
    [UPDATES]: 
    
            -up,    --updates              command  : updates the Dnsbruter for latest version (required: pip to be installed). 
            -dc,    --disable-check        command  : disable updates check for dnsbruter.
            
    [OUTPUT]: 
    
            -o,     --output               string   : filename to save the scans outputs. 
            -ws,    --wildcard-output      string   : filename to save the found wildcard domains.
            -j,     --json                 command  : enables to display and save output in json format.
            
    [DEBUG]: 
    
            -h,     --help                 command  : shows this help message and exits.
            -s,     --silent               command  : only shows essetial outputs and avoid other info.
```

### Features of Dnsbruter:

Dnsbruter is a powerful asynchronous DNS brute-forcing and fuzzing tool, built for penetration testers and security researchers. It allows you to brute-force valid subdomains and fuzz any portion of a domain name. The tool is highly concurrent and performs well even in resource-constrained environments like low-end VPSs.

#### 1. Single Domain Input:
Brute-force a single domain and check for valid subdomains using the `-d` flag.

**Command Syntax:**

```bash
dnsbruter -d <domain>
```

**Example:**

```bash
dnsbruter -d google.com
```

**Explanation:**
- Dnsbruter will attempt to resolve subdomains of `google.com`.
- It checks for valid subdomains and accounts for wildcard DNS records to ensure the results are accurate.

#### 2. Brute-force with Fuzzing (BRUT Input):
Fuzz a specific part of the domain by replacing it with the `BRUT` keyword.

**Command Syntax:**

```bash
dnsbruter -d <domain_with_BRUT>
```

**Example:**

```bash
dnsbruter -d adminBRUT.google.com
```

**Explanation:**
- The tool will replace the `BRUT` keyword with different values, such as `admin123`, `adminxyz`, etc.
- This method is used for fuzzing and discovering hidden subdomains or alternate domain configurations.


<h1 align="center">
  <img src="https://github.com/RevoltSecurities/Dnsbruter/assets/119435129/a260df97-17fb-4cd5-8017-687697fcd030" width="2000px">
  <br>
</h1>

---

#### 3. Brute-force Domains from a File:
Use the `-dL` flag to read a list of domains from a file and attempt to brute-force subdomains or fuzz them.

**Command Syntax:**

```bash
dnsbruter -dL <file_with_domains>
```

**Example:**

```bash
dnsbruter -dL domains.txt
```

**Explanation:**
- Each line in the file should contain a single domain name.
- Dnsbruter will process each domain and attempt brute-force or fuzzing as specified.

#### 4. Passing Domains via Stdin:
You can also pass domains via stdin to integrate Dnsbruter into your scripts or tools.

**Command Syntax:**

```bash
echo "<domain>" | dnsbruter -d -
```

**Example:**

```bash
echo "example.com" | dnsbruter -d -
```

**Explanation:**
- This allows you to pipe domain names dynamically into Dnsbruter from other tools or scripts.

---

### About:

Dnsbruter is an open-source tool for security researchers and cybersecurity professionals involved in security assessments and information gathering. It is designed to assist in active DNS enumeration. We encourage contributions from the open-source community to improve Dnsbruter and keep it up-to-date. If you find this tool helpful, please show your support by giving ⭐ to the repository.
