import os
import json

filename = input("Enter the filename: ")

# Validate filename
if not filename or not os.path.isfile(filename):
    print(f"{filename} is not a valid filename.")
    exit()

records = []

with open(filename) as f:
    for line in f:
        if "AUTHENTICATION_KEY" in line:
            data = json.loads(line)
            records.append([data.get('userName'), data.get('authenticationSource')])

# Check if any records were found
if not records:
    print("No matching records found in the file.")
    exit()

with open('full_list.json', 'w') as f:
    json.dump(records, f)
print("Full list of records saved to full_list.json")

def unique_records(records):
    unique_records = []
    for record in records:
        if record not in unique_records:
            unique_records.append(record)
    return unique_records

unique_list = unique_records(records)
# print(unique_list)

# Save unique list to a new JSON file
with open('unique_records.json', 'w') as f:
    json.dump(unique_list, f)

print("Unique records saved to unique_records.json")