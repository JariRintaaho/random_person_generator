import json
from random import randint
from random import choice

class name_generator:

    def __init__(self, family_name_prefix = "Testi"):

        self.family_name_prefix = family_name_prefix
        self.name_json = "names.json"

        self.get_name_lists()


    def get_name_lists(self):

        with open(self.name_json) as input_file:
            name_data = json.load(input_file)

        self.family_name_list = name_data["family_names"]
        self.female_name_list = name_data["female_names"]
        self.male_name_list = name_data["male_names"]

    def generate_name(self, gender = "random"):

        self.family_name = choice(self.family_name_list)
        if self.family_name_prefix:
            self.family_name = self.family_name_prefix + self.family_name.lower()

        self.first_names = []

        if gender == "random":
            gender = choice(["female", "male"])

        for i in range(0, randint(2,3)):
            if gender == "female":
                self.first_names.append(choice(self.female_name_list))
            elif gender == "male":
                self.first_names.append(choice(self.male_name_list))


if __name__=="__main__":

    random_name_generator = name_generator()
    random_name_generator.generate_name("female")
    print(random_name_generator.family_name, random_name_generator.first_names)

    random_name_generator = name_generator("Testi")
    random_name_generator.generate_name("male")
    print(random_name_generator.family_name, random_name_generator.first_names)

    random_name_generator.generate_name()
    print(random_name_generator.family_name, random_name_generator.first_names)
