# Global imports
import argparse

# Local imports
from TLDScanner import tldscan

def main():
    parser = argparse.ArgumentParser(description="Retrieve domain information")
    parser.add_argument('domain', type=str, help="The domain to retrieve information for")
    parser.add_argument('data', type=str, help="The data folder that contains the tld extensions")
    parser.add_argument('--format', choices=['json', 'text'], default='json', help="The output format (default is JSON)")
    args = parser.parse_args()
    
    print(tldscan(args.domain, args.data, args.format))

if __name__ == "__main__":
    main()