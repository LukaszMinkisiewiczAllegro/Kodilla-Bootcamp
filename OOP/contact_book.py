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


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    
    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonie do {self.name} {self.surname}'

    @property
    def name_length(self):
        return len(self.name) + len(self.surname) + 1

class BusinessContact(BaseContact):
    def __init__(self, buss_phone, position, company,*args, **kwargs):
        self.buss_phone = buss_phone
        self.position = position
        self.company = company
        super().__init__(*args, **kwargs)

    def contact(self):
        return f'Wybieram numer {self.buss_phone} i dzwonie do {self.name} {self.surname}'    


def create_contact():
    new_contact = ContactCard(fake.unique.first_name(),fake.last_name(), fake.company(), fake.job(), fake.email())
    return new_contact


def create_contacts(a = 'Base', how_many = 1):
    cnt = 0
    contact_list_1 = []
    while cnt < how_many:
        if type == 'Base':
            contact_list_1.append(BaseContact(fake.unique.first_name(),fake.last_name(),fake.phone_number(), fake.email()))
        else:
            contact_list_1.append(BusinessContact(fake.phone_number(),fake.job(), fake.company(), fake.unique.first_name(),fake.last_name(),fake.phone_number(), fake.email(),))
        
        cnt += 1
    
    return contact_list_1


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


test_contacts = create_contacts(how_many=5)
print(test_contacts)

for obj in test_contacts:
    print(obj.contact())