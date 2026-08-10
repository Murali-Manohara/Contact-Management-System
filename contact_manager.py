contacts = {}


def add_contact():
    contact_id = input("Enter Contact ID: ")
    
    if contact_id in contacts:
        print("Contact ID already exists.")
        return

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts[contact_id] = {
        "name": name,
        "phone": phone
    }

    print("Contact added successfully.")


def display_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== All Contacts =====")

    for contact_id, contact in contacts.items():
        print("ID:", contact_id)
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("------------------------")


def search_contact():
    contact_id = input("Enter Contact ID to search: ")

    if contact_id in contacts:
        contact = contacts[contact_id]

        print("\nContact found:")
        print("ID:", contact_id)
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
    else:
        print("Contact not found.")


def update_phone():
    contact_id = input("Enter Contact ID to update: ")

    if contact_id in contacts:
        new_phone = input("Enter new Phone Number: ")
        contacts[contact_id]["phone"] = new_phone

        print("Phone number updated successfully.")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Phone Number")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            display_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_phone()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


main()