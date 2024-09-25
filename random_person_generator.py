from name_generator import name_generator
from address_generator import address_generator

import csv

# stores data to csv file
def dict_to_csv(dictionary, filename):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        writer.writerows(zip(*values))

first_names = []
family_names = []
street_addresses = []
postal_codes = []
post_offices = []

for i in range(10):

    name = name_generator()
    name.generate_name()

    address = address_generator()
    address.generate_address()

    first_names.append(' '.join(name.first_names))
    family_names.append(name.family_name)
    street_addresses.append(address.street_address)
    postal_codes.append(address.postal_code)
    post_offices.append(address.post_office)

person_data = {
    "first_name":first_names,
    "family_name":family_names,
    "street_address":street_addresses,
    "postal_code":postal_codes,
    "post_office":post_offices
}

dict_to_csv(person_data, "persons.csv")
