from random import randint
from random import choice
import json

class address_generator:

    def __init__(self, street_prefix = "Testi"):

        self.name_json = "street_names.json"
        self.postal_json = "postal_codes.json"
        self.street_prefix = street_prefix

        self.get_address_data()

    def get_address_data(self):

        with open(self.name_json) as input_file:
            name_data = json.load(input_file)
    
        with open(self.postal_json) as input_file:
            postal_data = json.load(input_file)

        self.street_name_list = name_data["street_names"]
        self.postal_codes_list = postal_data["postal_codes"]

    def generate_address(self):

        self.postal_code = choice(self.postal_codes_list)
        self.post_office = self.postal_code[1]
        self.postal_code = self.postal_code[0]

        self.street_name = choice(self.street_name_list)

        if self.street_prefix:
            self.street_name = self.street_prefix + self.street_name.lower()

        self.appartment_number = str(randint(1,50))

        address_style = choice([1,2,3])
        if address_style == 2:
            self.appartment_number += " " + choice(["A", "B", "C", "D"])
        elif address_style == 3:
            self.appartment_number += " " + choice(["A", "B", "C", "D"]) + " " + str(randint(1,10))

        self.street_address = self.street_name + " " + self.appartment_number

if __name__=="__main__":

    random_address_generator = address_generator()
    random_address_generator.generate_address()
    print(random_address_generator.street_address, random_address_generator.postal_code, random_address_generator.post_office)
