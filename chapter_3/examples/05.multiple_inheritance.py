class ContactList(list):
    def search(self, name):
        ''' Return all contacts that contains the search value in thier name.'''
        matching_contacts = []
        for contact in self:
            if name == contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contact = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contact.append(self)

class MailSender:
    def send_mail(self, message):
        print(f"send mail to {self.email}")

class EmailableContact(Contact, MailSender):
    pass

c1 = Contact("ahmed", "ahmed@gmail.com")
c2 = Contact("ahmed mansour", "ahmed_mansour@gmail.com")

e = EmailableContact("ahmed_emailable", "ahmed_emailable@gmail.com")
e.send_mail("Hello!")

# not able to send an email
# c1.send_mail("Hello!")

search_list = [c.name for c in Contact.all_contact.search('ahmed')]
print(search_list)

