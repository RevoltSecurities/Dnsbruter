# Dnsbruter - Subdomain Bruteforcing Tool

Dnsbruter is a command-line tool written in Python that allows users to perform active subdomain enumeration through brute-forcing. The tool uses multi-threading to speed up the process and supports verbose mode for displaying found subdomains and invalid subdomains.

## Prerequisites

Before running Dnsbruter, make sure you have the following installed:

- Python 3.x
- Required Python packages: `dns.resolver`, `requests`, `colorama`

You can install the required packages using the following command:

```bash
pip install dnspython requests colorama
```

## Installation

1. Clone the Dnsbruter repository from GitHub:

```bash
git clone https://github.com/sanjai-AK47/Dnsbruter.git
```

2. Change directory to the Dnsbruter folder:

```bash
cd Dnsbruter
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python dnsbruter.py -d <target_domain> -t <num_threads> [-o <output_file>] [-v] [-i]
```

### Options:

- `-d, --domain <target_domain>`: Specifies the target domain for active subdomain enumeration.

- `-t, --threads <num_threads>`: Defines the number of threads to use for multi-threading. Use a value less than or equal to 100 for safety.

- `-o, --output <output_file>`: (Optional) Specifies the filename to save the output results. If not provided, results will be saved in a file named `{target_domain}_results.txt`.

- `-v, --verbose`: (Optional) Enable verbose mode to print found subdomains to the console.

- `-i, --invalid`: (Optional) Enable invalid mode to print invalid or not found subdomains to the console.

## Example

```bash
python dnsbruter.py -d example.com -t 50 -o output.txt -v -i
```

This command will start the subdomain enumeration process for the target domain `example.com` using 50 threads. The found subdomains will be displayed on the console due to the verbose mode. Invalid or not found subdomains will also be shown. The results will be saved in the `output.txt` file.

## Disclaimer

This tool is intended for legal and ethical use only. Unauthorized access to systems and services is strictly prohibited. The developer is not responsible for any misuse or damage caused by this tool. Use it responsibly and with the necessary permissions.
