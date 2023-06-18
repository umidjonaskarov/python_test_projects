contacts = ['Umid', 'Jack', 'John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Thompson', 'Emily Wilson', 'Michael Brown', 'Sarah Davis', 'David Lee']
info = [
    ('Umidjon Askarov', '998330880808', 'umid@mail.ru'),
    ('Pho Jackson', '998888232', 'VUS@mail.ru'),
    ('John Doe', '1234567890', 'johndoe@example.com'),
    ('Jane Smith', '9876543210', 'janesmith@example.com'),
    ('Alice Johnson', '5551234567', 'alicejohnson@example.com'),
    ('Bob Thompson', '9998887777', 'bobthompson@example.com'),
    ('Emily Wilson', '1112223333', 'emilywilson@example.com'),
    ('Michael Brown', '4445556666', 'michaelbrown@example.com'),
    ('Sarah Davis', '7778889999', 'sarahdavis@example.com'),
    ('David Lee', '2223334444', 'davidlee@example.com')
]

def selectContact():
    c_i = int(input("Enter contact index: "))
    if c_i < len(contacts):
        print("Contact information: ")
        print("Name:", contacts[c_i])
        print("Phone:", info[c_i][0])
        print("Email:", info[c_i][1])
    else:
        print("Invalid contact index. Try again.")
        selectContact()


def menu():
    option = input("Type a to see all contacts or c to create: ")
    if option == "c":
        name = input("Name")
        contacts.append(name)
        phone = input("Phone")
        info.append(phone)
        email = input("Email")
        info.append(email)
        print("Created!", name, phone, email)
        for index, contact in enumerate(contacts):
            print(index, "-", contact + "info")
    elif option == "a":
        print("All contacts:")
        for index, contact in enumerate(contacts):
            print(index, "-", contact)
        selectContact()

while True:
    menu()

