from name_generator import name_generator
from address_generator import address_generator


for i in range(10):

    name = name_generator()
    name.generate_name()

    address = address_generator()
    address.generate_address()

    personal_details = {"first_name": ' '.join(name.first_names), 
                        "family_name": name.family_name, 
                        "street_address" : address.street_address,
                        "postal_code" : address.postal_code,
                        "post_office" : address.post_office
                        }

    print(personal_details)
