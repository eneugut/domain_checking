import csv
import itertools
import os

# Setting up the directory on the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')  # Path to the desktop
folder_name = 'domain_names/4char'
folder_path = os.path.join(desktop_path, folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Characters: 26 letters + 10 digits
characters = [chr(i) for i in range(97, 123)] #+ [str(i) for i in range(10)]  # a-z, 0-9
# Include hyphen for the middle two positions
middle_characters = characters + ['-']

# Generating all combinations
combinations = itertools.product(characters, middle_characters, middle_characters, characters)

# Function to write to CSV
def write_to_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Domain'])  # Header
        writer.writerows(data)

# File path and naming
file_path = os.path.join(folder_path, '4_char_words_{}.csv')

# Batch size
batch_size = 500

# Batching and writing data
batch = []
file_count = 1
for combo in combinations:
    batch.append([''.join(combo)])
    if len(batch) == batch_size:
        write_to_csv(file_path.format(file_count), batch)
        batch = []
        file_count += 1

# Write any remaining domains in the last batch
if batch:
    write_to_csv(file_path.format(file_count), batch)
