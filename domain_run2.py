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
    
    # Start timer
    start = time.time()
    
    batch_size = args.batch_size
    available_domains = []
    batch_num = 1

    for i in range(0, len(domains)):
        
        available = check_domain_availability(domains[i])
        if available:
            available_domains.append([domains[i]])
        if len(available_domains) == batch_size:
            # Name file based on batch number
            file_name = 'batch_{}.csv'.format(batch_num)
            write_to_csv(folder_name='domain_names', file_name=file_name, data=available_domains)
            batch_num += 1
            available_domains = []
        if (i + 1) % 50 == 0:
            print('Checked {} domains...'.format(i + 1))

    # Deal with any remaining domains
    if len(available_domains) > 0:
        file_name = 'batch_{}.csv'.format(batch_num)
        write_to_csv(folder_name='domain_names', file_name=file_name, data=available_domains)

    # Stop timer
    end = time.time()
    print('Time taken: {} seconds'.format(end - start))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate and check domain names.')
    parser.add_argument('--min_length', type=int, default=4, help='Minimum length of domain names')
    parser.add_argument('--max_length', type=int, default=4, help='Maximum length of domain names')
    parser.add_argument('--max_domains', type=int, default=10000000, help='Maximum number of domains to generate')
    parser.add_argument('--batch_size', type=int, default=500, help='Number of domains to print in a CSV')
    parser.add_argument('--domain_ending', type=str, default='.com', help='Domain ending')
    parser.add_argument('--allow_numbers', type=bool, default=True, help='Allow numbers in domain names')
    parser.add_argument('--allow_hyphen', type=bool, default=True, help='Allow hyphens in domain names')
    parser.add_argument('--allow_fada', type=bool, default=False, help='Allow fadas in domain names')
    parser.add_argument('--require_hyphen_or_number', type=bool, default=True, help='Require hyphen or number in domain names')

    args = parser.parse_args()
    main(args)