import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Enter the index of the contact you want to edit: ")) - 1
        contact = contacts[idx]
    except (ValueError, IndexError):
        print("Invalid index.")
        return
    name = input("Enter new name (leave blank to keep unchanged): ")
    phone = input("Enter new phone number (leave blank to keep unchanged): ")
    email = input("Enter new email address (leave blank to keep unchanged): ")
    if name:
        contact['name'] = name
    if phone:
        contact['phone'] = phone
    if email:
        contact['email'] = email
    save_contacts(contacts)
    print("Contact edited successfully!")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Enter the index of the contact you want to delete: ")) - 1
        del contacts[idx]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid index.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
