from domain_name_checker import *
import time

if __name__ == '__main__':
    domains = generate_domain_names(min_length=4, max_length=4, max_domains=1000, domain_ending='.com',
                                    allow_numbers=True, allow_hyphen=True, allow_fada=False,
                                    require_hyphen_or_number=True)
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
    write_to_csvs(folder_name='domain_names', file_name='4_char_words_{}.csv', data=available_domains, batch_size=500)
