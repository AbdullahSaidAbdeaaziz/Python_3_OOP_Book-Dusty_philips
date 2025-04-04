class ContactList(list):
    def search(self, name):
        ''' Return all contacts that contains the search value in thier name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contact = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contact.append(self)


c1 = Contact("ahmed", "ahmed@gmail.com")
c2 = Contact("ahmed mansour", "ahmed_mansour@gmail.com")

search_list = [c.name for c in Contact.all_contact.search('ahmed')]
print(search_list)
