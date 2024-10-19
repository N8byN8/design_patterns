from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json
from dataclasses import dataclass

@dataclass
class Contact:
    full_name: str
    email: str
    phone_number: str
    is_friend: bool

    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone_number} {'(Friend)' if self.is_friend else 'Foe'}"
    
class FileReader(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        pass

class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source

    @abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass

class XMLContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        root = ET.fromstring(self.data_source.read())
        contacts = []
        for elem in root.iter():
            if elem.tag == 'contact':
                full_name = elem.find('full_name').text
                email = elem.find('email').text
                phone_number = elem.find('phone_number').text
                is_friend = elem.find('is_friend').text.lower() == 'true'
                contact = Contact(full_name, email, phone_number, is_friend)
                contacts.append(contact)
        return contacts
    
class JSONContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        data_dict = json.loads(self.data_source.read())
        contacts = []
        for contact_data in data_dict['contacts']:        
            full_name = contact_data['full_name']
            email = contact_data['email']
            phone_number = contact_data['phone_number']
            is_friend = contact_data['is_friend']
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        return contacts

class XMLReader(FileReader):
    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()
        
class JSONReader(FileReader):
    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()
        
def print_contact_data(contacts_source: ContactsAdapter):
    for contact in contacts_source.get_contacts():
        print(contact)

if __name__ == "__main__":
    xml_reader = XMLReader('structural/adapter/contacts.xml')
    xml_adapter = XMLContactsAdapter(xml_reader)
    print_contact_data(xml_adapter)

    json_reader = JSONReader('structural/adapter/contacts.json')
    json_adapter = JSONContactsAdapter(json_reader)
    print_contact_data(json_adapter)
