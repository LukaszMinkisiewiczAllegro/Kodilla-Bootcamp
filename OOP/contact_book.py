from faker import Faker

fake = Faker()

class ContactCard:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
    
    @property
    def name_length(self):
        return len(self.name) + len(self.surname) + 1
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

    def contact(self):
        return f'Kontaktuje sie z {self.name} {self.surname} {self.position} {self.email}'

def create_contact():
    new_contact = ContactCard(fake.unique.first_name(),fake.last_name(), fake.company(), fake.job(), fake.email())
    return new_contact


contact_1 = create_contact()
contact_2 = create_contact()
contact_3 = create_contact()
contact_4 = create_contact()
contact_5 = create_contact()
contact_6 = create_contact()
print(contact_1.contact())

contact_list = [contact_1,contact_2,contact_3,contact_4,contact_5,contact_6]

by_name = sorted(contact_list, key = lambda contact: contact.name)
by_surname = sorted(contact_list, key = lambda contact: contact.surname)
by_email = sorted(contact_list, key = lambda contact: contact.email)

for contact in by_name:
    print(contact)

print(contact_1.name_length)

