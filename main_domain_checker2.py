from domain_name_checker import *

if __name__ == '__main__':
    domains = generate_domain_names(min_length=3, max_length=3, max_domains=100000, domain_ending='.com',
                                    allow_numbers=True, allow_hyphen=True, allow_fada=False,
                                    require_hyphen_or_number=True)
    # Check the availability of each domain name. Print a statement every 50 domains to show progress.
    print(domains)
    print('Length of domains: {}'.format(len(domains)))
    available_domains = []
    for i, domain in enumerate(domains):
        if check_domain_availability(domain):
            available_domains.append([domain])
        if (i + 1) % 50 == 0:
            print('Checked {} domains...'.format(i + 1))
    # Write the available domains to CSV files
    write_to_csvs(folder_name='domain_names', file_name='3_char_words_{}.csv', data=available_domains, batch_size=500)
