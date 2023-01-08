# Find and manage contacts in .csv file

import csv
import re
import sys


# set the file with contacts
file_with_contacts = "contact_book.csv"


def change_csv_to_list(contact_book_file):
    """Convert .csv file to a list

    Args:
        contact_book_file (str): name of source file

    Returns:
        int: 0 if file is not existing
        or
        list: list of str with contacts
    """

    try:
        file = open(contact_book_file)
    except FileNotFoundError:
        print("File is not existing.")
        return 0

    # read .csv
    file_read = csv.reader(file)

    # convert to list
    file_list = [data for data in file_read]

    file.close()

    return file_list


def searching_method():
    """Find filtering option.

    Returns:
        int: filtering option from menu
    """

    while True:
        # get the number
        print("Choose your searching option:\n"
              "1 - First Name\n"
              "2 - Last Name\n"
              "3 - Phone\n"
              "4 - Email\n"
              "5 - Back to menu\n")
        try:
            second_decision = int(input("Your choice: "))
        except ValueError:
            print("You have to pick a number 1 - 5.")
            continue

        # check if it is 1 - 5
        if 0 < second_decision <= 5:
            return second_decision
        else:
            print("You have to pick a number 1 - 5.")
            continue


def check_phone_number(number):
    """Validate phone number.

    Args:
        number (str): 9 digits number

    Returns:
        bool: True if number is correct, False if is incorrect
    """

    # Get te pattern for phone number
    pattern = r'^\d{9}$'

    # pass the pattern and the string into the match() method
    if re.match(pattern, number):
        return True
    else:
        return False


def check_email(email):
    """Validate email.

    Args:
        email (str): email address

    Returns:
        bool: True if email is correct, False if is incorrect
    """

    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # pass the pattern and the string into the match() method
    if re.match(pattern, email):
        return True
    else:
        return False


def get_contacts(filter_data, contacts_list, index):
    """Finds matching contacts.

    Args:
        filter_data (str): inserted data to find
        contacts_list (list): list of str with contacts data
        index (int): index of column used for filtering

    Returns:
        list: list of str witch matching contacts
    """

    # empty list to storage matching contacts
    matching_contacts = []

    # look for similarity on every row and exact column
    for i in range(1, len(contacts_list)):
        contact_data = str(contacts_list[i][index])

        # if match append to the matching contact list
        if (str(filter_data)).lower() == contact_data.lower():
            matching_contacts.append(contacts_list[i])

    return matching_contacts


def show_contact_data(matching_contacts):
    """Show all data for contact.

    Args:
        matching_contacts (list): list of str witch matching contacts
    """

    # if there are contacts
    if len(matching_contacts) != 0:
        print("\nMatching data:")
        for contact in matching_contacts:
            print("\nFirst Name:", contact[0], "\nLast Name:",
                  contact[1], "\nPhone:", contact[2], "\nEmail:", contact[3])
    # if not
    else:
        print("No matching contacts.")


def find_contact(contacts_list):
    """Finds matching contacts and all data about it.

    Args:
        contacts_list (list): list of str with contacts data
    """

    # get searching method
    filtering = searching_method()

    # index for chosen searching method in contacts list
    data_index = filtering - 1

    # tasks for every searching method
    # 1 - First Name
    if filtering == 1:
        filtering_name = input("\nGive First Name: ")
        found_contacts = get_contacts(
            filtering_name, contacts_list, data_index)
        show_contact_data(found_contacts)
    # 2 - Last Name
    elif filtering == 2:
        filtering_surname = input("\nGive Last Name: ")
        found_contacts = get_contacts(
            filtering_surname, contacts_list, data_index)
        show_contact_data(found_contacts)
    # 3 - Phone
    elif filtering == 3:
        filtering_phone = input("\nGive Phone number: ")
        correct = check_phone_number(filtering_phone)
        if correct is True:
            found_contacts = get_contacts(
                filtering_phone, contacts_list, data_index)
            show_contact_data(found_contacts)
        else:
            print("Wrong number. It has to have 9 digits.")
    # 4 - Email
    elif filtering == 4:
        filtering_email = input("\nGive Email: ")
        correct = check_email(filtering_email)
        if correct is True:
            found_contacts = get_contacts(
                filtering_email, contacts_list, data_index)
            show_contact_data(found_contacts)
        else:
            print("Wrong email address. Try again.")
    # 5 - Exit
    elif filtering == 5:
        print()


def get_first_name():
    """Gets First Name for new contact. Cannot be empty.

    Returns:
        str: First Name for new contact
    """

    first_name = ''
    while True:
        input_user = input("Give First Name: ")
        if input_user == '':
            print("You have to give name of contact")
            continue
        else:
            first_name = input_user
            break

    return first_name


def get_last_name():
    """Gets Last Name for new contact.

    Returns:
        str: Last Name for new contact
    """

    last_name = input("Give Last Name or skip by pressing Enter: ")
    if last_name == '':
        print("You left Last Name empty. OK.")

    return last_name


def get_phone():
    """Gets Phone number for new contact.

    Returns:
        str: Phone number for new contact
    """

    phone = ''
    while True:
        input_user = input("Give Phone number or skip by pressing Enter: ")
        if input_user == '':
            print("You left Phone number empty. OK.")
            break
        else:
            correct = check_phone_number(input_user)
            if correct is True:
                phone = input_user
                break
            else:
                print("Wrong! It has to have 9 digits. Try again.")
    return phone


def get_email():
    """Gets Email for new contact.

    Returns:
        str: Email for new contact
    """

    email = ''
    while True:
        input_user = input("Give Email address or skip by pressing Enter: ")
        if input_user == '':
            print("You left Email address empty. OK.")
            break
        else:
            correct = check_email(input_user)
            if correct is True:
                email = input_user
                break
            else:
                print("Incorrect e-mail. Try again.")

    return email


def insert_contact(contacts_file):
    """Inserts new contact to .csv file

    Args:
        contacts_file (str): name of source file
    """

    first_name = get_first_name()
    last_name = get_last_name()
    phone = get_phone()
    email = get_email()

    new_contact = [first_name, last_name, phone, email]

    with open(contacts_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(new_contact)


# Main part of working program
contacts_list = change_csv_to_list(file_with_contacts)

if contacts_list != 0:
    while True:
        print("\nChoose what do you want to do:\n"
              "1 - Search for contact\n"
              "2 - Adding contact\n"
              "3 - Quit\n")
        try:
            decision = int(input("Your choice: "))
        except ValueError:
            print("You have to pick a number 1, 2 or 3.")
            continue

        if decision == 1:
            find_contact(contacts_list)
        elif decision == 2:
            insert_contact(file_with_contacts)
            print("Contact has been added")
        elif decision == 3:
            print("End of program. Bye!")
            break
        else:
            print("This number is not in menu. Try again.")
else:
    sys.exit()
