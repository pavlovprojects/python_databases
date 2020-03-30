import contacts.db as contacts


def _print_contact(contact, full):
    if full: print("id: " + str(contact[0]))
    print("name: " + contact[1], end="\n" if full else " ")
    print("phone: " + str(contact[3]))
    if full: print("email: " + (contact[2] or "-"))
    if full: print("address: " + (contact[4] or "-"))
    if full: print("")


def get_name(command):
    try:
        return command[command.index(" "):].strip()
    except ValueError:
        print("Need contact name")


def list_contacts(full=True):
    contacts_data = contacts.get_all_rows()

    print("--------START----------")
    for num, contact in enumerate(contacts_data, start=1):
        if full: print("Contact # " + str(num))
        _print_contact(contact, full)
    print("--------END----------")


def _input_data():
    name = input("Type contact name: ")
    while not name:
        name = input("Type contact name: ")

    email = input("Type contact email: ")

    phone = input("Type contact phone: ")
    while not phone:
        phone = input("Type contact phone: ")

    address = input("Type contact address: ")
    return (name, email, phone, address)


def add_contact():
    data = _input_data()
    contacts.insert_contact(data)
    print("Contact added.")


def remove_contact(name):
    contacts.delete_contact(name)
    print("Contact " + name + " removed.")


def change_contact(name):
    if not contacts.select_contact(name):
        print("No contact with name", name)
    else:
        field = input("What filed to update? ")
        while field not in ["name", "phone", "email", "address"]:
            print('Only "name", "phone", "email", "address" can be updated! ')
            field = input("What filed to update? ")
        new_value = input("What value to set? ")
        contacts.update_contact(name=name, field=field, new_value=new_value)
        print("Updated: ", field, "->", new_value, "for", name)


def show_contact(name):
    contact = contacts.select_contact(name)
    if contact:
        _print_contact(contact, full=True)
    else:
        print("No contact with name", name)


def get_contact_amount():
    amount = len(contacts.get_all_rows())
    print("Total contacts: ", amount)


def show_help():
    print("""
    Help of contact manager:
    :q - to quit
    :h - help info
    :ls - list contacts
    :list - list full contacts
    :add - add contacts
    :rm [name] - remove contact
    :show [name] - show contact
    :edit [name] - remove contact
    """)


def main():
    print("Contact manager up and running!")
    get_contact_amount()

    while True:
        command = input(">>> Type command ").strip()

        if ":" not in command:
            print("All commands should start with :")
            continue

        if command == ":q":
            print("Bye bye now...")
            break
        elif command == ":h":
            show_help()
        elif command == ":ls":
            list_contacts(full=False)
        elif command == ":list":
            list_contacts()
        elif command == ":add":
            add_contact()
            get_contact_amount()
        elif ":rm" in command:
            remove_contact(get_name(command))
            get_contact_amount()
        elif ":edit" in command:
            change_contact(get_name(command))
        elif ":show" in command:
            show_contact(get_name(command))
        else:
            print("No such command. Try :h to see commands.")


if __name__ == "__main__":
    main()
