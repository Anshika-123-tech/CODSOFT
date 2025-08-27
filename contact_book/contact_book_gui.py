contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts available.\n")
        return
    print("📒 Contact List:")
    for name, details in contacts.items():
        print(f"- {name} | {details['phone']}")
    print()

def search_contact():
    search = input("Enter Name or Phone Number to Search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['phone']:
            print(f"🔎 Found Contact:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True
    if not found:
        print("❌ Contact not found.\n")

def update_contact():
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Leave blank if you don't want to change a field.")
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")

        if phone: contacts[name]["phone"] = phone
        if email: contacts[name]["email"] = email
        if address: contacts[name]["address"] = address

        print(f"✏️ Contact '{name}' updated successfully!\n")
    else:
        print("❌ Contact not found.\n")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("❌ Contact not found.\n")

# --- Main Menu ---
while True:
    print("📞 Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")
# Simple Contact Book Application