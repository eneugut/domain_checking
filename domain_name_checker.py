import itertools
import string
import random
import whois
import csv
import os


def generate_domain_names(min_length, max_length, max_domains, allow_numbers=True, allow_hyphen=True, allow_fada=True, domain_ending=".com", is_random = False, require_fada=False, require_hyphen=False, require_number=False, require_hyphen_or_number = False, require_fada_or_hyphen_or_number=False):
    characters = list(string.ascii_lowercase)  # a-z
    if allow_numbers:
        characters.extend(string.digits)  # 0-9
    if allow_hyphen:
        characters.append('-')
    if allow_fada:
        characters.extend(['á', 'é', 'í', 'ó', 'ú'])  # Adding vowels with fada

    domains = []
    for length in range(min_length, max_length + 1):
        # Generate all combinations for the current length
        for combo in itertools.product(characters, repeat=length):
            domain = ''.join(combo) + domain_ending
            # If combo starts or ends with a hyphen, skip it
            if combo[0] == '-' or combo[-1] == '-':
                continue
            # Check for required characters
            if (require_hyphen and '-' not in combo) or \
               (require_fada and not any(c in combo for c in ['á', 'é', 'í', 'ó', 'ú'])) or \
               (require_number and not any(c.isdigit() for c in combo)) or \
                (require_hyphen_or_number and not any(c.isdigit() or c == '-' for c in combo)) or \
                (require_fada_or_hyphen_or_number and not any(c.isdigit() or c == '-' or c in ['á', 'é', 'í', 'ó', 'ú'] for c in combo)):
                continue
            domains.append(domain)
            # Stop if the maximum number of domains is reached
            if len(domains) == max_domains:
                break
        if len(domains) == max_domains:
            break

    if is_random:
        # Randomly sample the generated domains without repetition
        # Note: This step can be memory-intensive for large data sets
        domains = random.sample(domains, min(len(domains), max_domains))

    return domains


def check_domain_availability(domain):
    try:
        domain_info = whois.whois(domain)
        return False
    except:
        print('Available: {}'.format(domain))
        return True

def write_to_csv(folder_name, file_name, data):
    # Setting up the directory on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')  # Path to the desktop
    folder_path = os.path.join(desktop_path, folder_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # File path and naming
    file_path = os.path.join(folder_path, file_name)

    # Writing data to CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # writer.writerow(['Domain'])  # Header
        writer.writerows(data)

    print('Wrote {} domains to {}.'.format(len(data), file_name))

# Function that writes the list of domains that are available to CSV files
def write_to_csvs(folder_name,file_name, data, batch_size):
    # Setting up the directory on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')  # Path to the desktop
    folder_path = os.path.join(desktop_path, folder_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # File path and naming
    file_path = os.path.join(folder_path, file_name)

    # Batching and writing data
    batch = []
    file_count = 1
    for domain in data:
        batch.append([domain])
        if len(batch) == batch_size:
            with open(file_path.format(file_count), 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Domain'])  # Header
                writer.writerows(batch)
            batch = []
            file_count += 1

    # Write any remaining domains in the last batch
    if batch:
        with open(file_path.format(file_count), 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Domain'])  # Header
            writer.writerows(batch)
 

# Function that takes a list of domains, checks them, takes the ones that are available and writes them to one csv file
def check_and_write_to_csv(domain_list, file_name):
    available_domains = []
    for i, domain in enumerate(domain_list):
        if check_domain_availability(domain):
            available_domains.append([domain])
        if (i + 1) % 50 == 0:
            print('Checked {} domains...'.format(i + 1))

        # Write the available domains to a CSV file
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Available Domains'])
        csv_writer.writerows(available_domains)
