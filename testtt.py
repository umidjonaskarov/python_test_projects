contacts = {}

def addContact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact_info = {
        'phone': phone,
        'email': email
    }
    contacts[name] = contact_info
    print("Contact added successfully.")

def displayContacts():
    print("All contacts:")
    for name in contacts:
        print("-", name)

def getContactInfo():
    name = input("Enter contact name: ")
    if name in contacts:
        contact_info = contacts[name]
        print("Contact information:")
        print("Name:", name)
        print("Phone:", contact_info['phone'])
        print("Email:", contact_info['email'])
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add a contact")
        print("2. Display all contacts")
        print("3. Get contact information")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            addContact()
        elif choice == "2":
            displayContacts()
        elif choice == "3":
            getContactInfo()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
