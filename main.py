import csv
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return (
            f"Name: {self.name} | "
            f"Phone: {self.phone} | "
            f"E-mail: {self.email} | "
            f"Address: {self.address} | "
        )

class ContactManager:
    def __init__(self, filename = "contact_book.csv"):

        self.filename = filename
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, index):
        try:
            index = int(index) -1
        except ValueError:
            print("invalid inex! enter number.")
        if 0 <= index < len(self.contacts):
            removed = self.contacts.pop(index)
            print(f"{removed.name} deleted")
            return
        else:
            print("not found contact")

    def search_contact(self):
        name = input("enter contact name: ")
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                print(contact)
                return
        print("not found contact")

    def edit_contact(self):
        name = input("Enter contact name: ")
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                new_phone = input("New phone: ")
                new_email = input("New email: ")
                new_address = input("New address: ")
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully")
                return
        print("Contact not found")

    def show_contact(self):
        if not self.contacts:
            print("contact list empty")
            return
        print("contact list: ")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

    def save_contacts(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "email", "address"])
            for contact in self.contacts:
                writer.writerow([
                    contact.name,
                    contact.phone,
                    contact.email,
                    contact.address
                ])
    def load_contacts(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                self.contacts.clear()

                for row in reader:
                    contact = Contact(
                        row[0],
                        row[1],
                        row[2],
                        row[3]
                    )
                    self.contacts.append(contact)
        except FileNotFoundError:
            pass
def main():
    manager = ContactManager()
    manager.load_contacts()

    while True:
        print("\n===== contact manager =====")
        print("1. add contact")
        print("2. remove contact")
        print("3. search contact")
        print("4. edit contact")
        print("5. show all contact")
        print("6. save & exit")

        choice = input("please choose an option: ")

        if choice == "1":
            name = input("Please enter name: ")
            phone = input("Please enter phone: ")
            email = input("Please enter email: ")
            address = input("Please enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
            print("contact added successfully")
        elif choice == "2":
            manager.show_contact()
            number = input("Enter contact number: ")
            manager.remove_contact(number)
        elif choice == "3":
            manager.search_contact()
        elif choice == "4":
            manager.edit_contact()
        elif choice == "5":
            manager.show_contact()
        elif choice == "6":
            manager.save_contacts()
            print("contact added successfully")
            print("GOOD BYE!")
            break
        else:
            print("please enter number")

if __name__ == "__main__":
    main()