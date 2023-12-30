import whois
import argparse

def main():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description='Perform a WHOIS lookup for a domain.')
    parser.add_argument('domain', type=str, help='Domain name to perform WHOIS lookup on')
    args = parser.parse_args()

    # Perform the WHOIS lookup
    domain_info = whois.whois(args.domain)

    # Print the WHOIS information
    print(domain_info)

if __name__ == '__main__':
    main()
