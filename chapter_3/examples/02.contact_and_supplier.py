class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print(f"send '{order}' to '{self.name}'")

# Contacts
c1 = Contact("ahmed", "ahmed@gmail.com")
c2 = Contact("ahmed mansour", "ahmed_mansour@gmail.com")

# Suppliers
s1 = Supplier("supplier", "supplier@gmail.com")

s1.order("Hello!") # output: send 'Hello!' to 'supplier'

# c1.order("Hello!") # output: error
