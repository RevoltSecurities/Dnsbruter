# Dnsbruter - Active Subdomain Enumeration Tool

Dnsbruter is a command-line tool designed for active subdomain enumeration through brute-forcing techniques. It helps security researchers and penetration testers discover potential subdomains for a given target domain. The tool allows users to customize their search and provides options for saving and displaying results.


## Features

Dnsbruter comes with the following features:

- **-d or --domain**: Specify the target domain for subdomain enumeration.
- **-o or --output**: Save the results of the enumeration to a specified output file.
- **-v**: Enable verbose mode to display found and valid domains.
- **-i or --invalid**: Print invalid domains during the enumeration process.
- **-t or --threads**: Define the number of threads to use for faster processing.

## Installation

### Linux Users (Binary)

For Linux users, you can move the provided binary file to a directory included in your system's PATH. This allows you to use the tool from anywhere in the terminal.

1. Download the binary file from the [Releases](https://github.com/sanjai-AK47/Dnsbruter/releases) section of the repository.
2. Move the binary file to a location included in your system's PATH, such as `/usr/local/bin/`:

   ```bash
   sudo mv dnsbruter /usr/local/bin/
   ```

3. Make the binary file executable:

   ```bash
   sudo chmod +x /usr/local/bin/dnsbruter
   ```

### All Users

If you prefer to run the tool directly using Python, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/sanjai-AK47/Dnsbruter.git
   cd Dnsbruter
   ```

2. Install the dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool using the Python file:

   ```bash
   python dnsbruter.py [options]
   ```

## Usage

To start using Dnsbruter, use the following command-line options:

```bash
python3 dnsbruter.py -h
usage: dnsbruter.py [-h] [-d DOMAIN] [-w WORDLIST] [-o OUTPUT] [-v] [-t THREADS] [-i]

[INFO]: A Subdomain Brutforcer for active subomain enumeration

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        [INFO]: Domain name for active subdomain enumeration
  -w WORDLIST, --wordlist WORDLIST
                        [INFO]: Wordlist that contains list of subdomain for brutforcing
  -o OUTPUT, --output OUTPUT
                        [INFO]: Filename to save the output
  -v, --verbose         [INFO]: Enabling verbose will print the found subdomain
  -t THREADS, --threads THREADS
                        [INFO]: Thread level to make the process to Multiprocess
  -i, --invalid         INVALIDS
                        [INFO]: Enabling invalid will print the invalid or not found subdomains

```

**Example:**

```bash
dnsbruter -d example.com -o output.txt -v -i -t 10
```

This command will perform active subdomain enumeration on the `example.com` domain using 10 threads, save the results to `output.txt`, display found and valid domains in verbose mode, and print invalid domains during the enumeration process.

Please note that using this tool for any unauthorized or malicious activities is strictly prohibited. Make sure to obtain proper authorization before scanning any target.

## Contributing

If you find any issues or have ideas to improve Dnsbruter, feel free to contribute to the project. You can create pull requests or open issues on the [GitHub repository](https://github.com/sanjai-AK47/Dnsbruter).



We hope this tool proves useful for your subdomain enumeration needs. Happy hacking! :rocket:
