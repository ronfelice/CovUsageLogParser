import os
import json
import glob

filename_input = input("Enter the filename or pattern: ")

# Validate filename input
if not filename_input:
    print("Filename input is not valid.")
    exit()

# Check if the input is a pattern or a single filename
if '*' in filename_input:
    filenames = glob.glob(filename_input)
else:
    filenames = [filename_input]

fcount = 0

for filename in filenames:
    # Validate filename
    if not os.path.isfile(filename):
        print(f"{filename} does not exist or is a directory.")
        continue

    records = []

#    with open(filename) as f:
#        for line in f:
#            if "AUTHENTICATION_KEY" in line:
#                data = json.loads(line)
#                records.append([data.get('userName'), data.get('authenticationSource')])
    with open(filename) as f:
        for line in f:
            if "AUTHENTICATION_KEY" in line:
                data = json.loads(line)
                if data.get('protocol') == 'WS':
                    records.append([data.get('userName'), data.get('authenticationSource')])

    # Check if any records were found
    if not records:
        print(f"No matching records found in the file {filename}.")
        continue

    with open('full_list.json', 'a') as f:
        json.dump(records, f)
    print(f"Full list of records from {filename} saved to full_list.json")

    def unique_records(records):
        unique_records = []
        for record in records:
            if record not in unique_records:
                unique_records.append(record)
        return unique_records

    # Load existing unique records
    try:
        with open('unique_records.json', 'r') as f:
            existing_unique_records = json.load(f)
    except FileNotFoundError:
        existing_unique_records = []

    # Append new unique records
    unique_list = unique_records(records)
    new_unique_records = [record for record in unique_list if record not in existing_unique_records]
    existing_unique_records.extend(new_unique_records)

    print(f"Found {len(new_unique_records)} new unique records in {filename}")

    # Save updated unique list to the file
    with open('unique_records.json', 'w') as f:
        json.dump(existing_unique_records, f)

    print(f"Unique records from {filename} saved to unique_records.json")