from domain_name_checker import *
import time
import argparse


def main(args):
    domains = generate_domain_names(
        min_length=args.min_length,
        max_length=args.max_length,
        max_domains=args.max_domains,
        domain_ending=args.domain_ending,
        allow_numbers=args.allow_numbers,
        allow_hyphen=args.allow_hyphen,
        allow_fada=args.allow_fada,
        require_hyphen_or_number=args.require_hyphen_or_number
    )

    # Check the availability of each domain name. Print a statement every 50 domains to show progress.
    print(domains)
    print('Length of domains: {}'.format(len(domains)))
    available_domains = []
    
    # Start timer
    start = time.time()
    
    for i, domain in enumerate(domains):
        if check_domain_availability(domain):
            available_domains.append([domain])
        if (i + 1) % 50 == 0:
            print('Checked {} domains...'.format(i + 1))
            # Print time elapsed
            print('Time elapsed: {} seconds'.format(time.time() - start))
    
    # Write the available domains to CSV files
    write_to_csvs(folder_name='domain_names', file_name='4char_list{}.csv', data=available_domains, batch_size=500)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate and check domain names.')
    parser.add_argument('--min_length', type=int, default=4, help='Minimum length of domain names')
    parser.add_argument('--max_length', type=int, default=4, help='Maximum length of domain names')
    parser.add_argument('--max_domains', type=int, default=1000, help='Maximum number of domains to generate')
    parser.add_argument('--domain_ending', type=str, default='.com', help='Domain ending')
    parser.add_argument('--allow_numbers', action='store_true', help='Allow numbers in domain names')
    parser.add_argument('--allow_hyphen', action='store_true', help='Allow hyphens in domain names')
    parser.add_argument('--allow_fada', action='store_true', help='Allow fada characters in domain names')
    parser.add_argument('--require_hyphen_or_number', action='store_true', help='Require at least one hyphen or number')

    args = parser.parse_args()
    main(args)