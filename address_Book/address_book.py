import csv


def view_contacts():
    print("Your contacts Info:")
    for contact in contacts:
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Address: {contact['Address']}")
        print("*"*20)


def Add_new_contact(name, phone, email, address):
    new_contact = {'Name': name, 'Phone' : phone, 'Email' : email, 'Address' : address}
    contacts.append(new_contact)
    save_file()

def update_contact(name, param, new_value):
    for contact in contacts:
        # try:
        #     if contact['Name'] == name:
        #         contact[str(param)] = new_value
        #         save_file()
        #         print(f"{param}'s {name} is sucessfully updated!")
        # except NameError:
        #     print(f'contacts {name} dose not exist')
        
        if contact['Name'] == name:
            contact[str(param)] = new_value
            save_file()
            print(f"{param}'s {name} is sucessfully updated!")
            return
        print(f'contacts {name} dose not exist')
    

def search_contact(name):
    for contact in contacts:
        if contact['Name'] == name:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
                

def open_file():
    try:
        with open("address_book.csv",'r') as file:
            lines = csv.DictReader(file)
            for line in lines:
                contacts.append(line)
    except FileNotFoundError:
        print(FileNotFoundError)

def save_file():
    with open("address_book.csv",'w', newline="") as file:
        header_name = ["Name", "Phone", "Email", "Address"]
        writer = csv.DictWriter(file, header_name)
        writer.writeheader()
        writer.writerows(contacts)

while True:
    contacts = []
    open_file()
    print("Address book Menu:")
    print('1. viwe contacts')
    print('2. add New Contact')
    print('3. update Contact')
    print('4. search Contact')
    print('5. Exit')
    
    choice = int(input("Enter your choice (1, 2, 3, 4, 5):").strip())
    
    if choice == 1:
        view_contacts()
        
    elif choice == 2:
        name = str(input("Enter name and family: "))
        phone = input("Enter phone number: ")
        email = str(input("Enter email: "))
        address = str(input("Enter address: "))
        Add_new_contact(name, phone, email, address)
        
    
    elif choice == 3:
        name = str(input("Enter name you want update: "))
        param = input("Enter value name you want update:(Phone, Email, Address) ")
        new_value = input(f"Enter new {param} of {name}: ")
        update_contact(name, param, new_value)
            
    elif choice == 5:
        print("Goodbye")
        exit()