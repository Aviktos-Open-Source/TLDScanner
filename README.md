# TLDScanner
This tool scans a given domain name across all common top-level domain (TLD) extensions (e.g., .com, .net, .io) to check if the domain is registered or available for purchase.

# Note
This tool supports only Python 3 and currently is designed to be used on Unix-based operating systems.

# Warning
This tool has rate limits for WHOIS queries and supports querying over 1,000 TLD extensions (1052 to be exact).

## WHOIS Terms of Use / Acceptable Use Policy
WHOIS queries are subject to various terms of use that restrict their use for spam, high-volume automated queries, or illegal activities. If you plan to use WHOIS data for bulk querying, please be aware of these terms to avoid violating the policies. Failure to comply may result in being restricted or banned from making further queries.

## Installation

```bash
git clone https://github.com/kzegani/TLDScanner.git
cd TLDScanner && pip install -r requirements.txt
```

## Usage

```bash
export PYTHONPATH=$(pwd)/src
# Open the Makefile and edit the domain to the desired one
# example:
# python3 -m TLDScanner.main google src/TLDScanner/data --format json
# python3 -m TLDScanner.main mydomain src/TLDScanner/data --format json
make
```

## Result
You can find registered domains in log/{domain_name} as json format.

Domains that are not registed will not show, or you can see logs interminal mentioning domains that are not found.

## Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
