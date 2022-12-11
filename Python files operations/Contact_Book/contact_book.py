# Find and manage contacts in .csv file

import csv
import re


# set the file with contacts
file_with_contacts = "Contact_book.csv"


# function to open the file and save data as list
def change_csv_to_list(contact_book_file):
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


# Function to get the filter option
def second_decision():
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


# Function to check phone number
def check_phone_number(number):
    if len(number) == 9:
        return True


# Define second function for validating an Email
def check_email(email):
    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # pass the pattern and the string into the match() method
    if re.match(pattern, email):
        return True
    else:
        return False


# getting list of contacts from .csv file with matching data
def get_contacts(filter_data, contacts_list, index):

    # empty list to storage matching contacts
    matching_contacts = []

    # look for similarity on every row and exact column
    for i in range(1, len(contacts_list)):
        contact_data = str(contacts_list[i][index])

        # if match append to the matching contact list
        if (str(filter_data)).lower() == contact_data.lower():
            matching_contacts.append(contacts_list[i])

    return matching_contacts


# function to show all data for contact
def show_contact_data(matching_contacts):

    # if there are contacts
    if len(matching_contacts) != 0:
        print("\nMatching data:")
        for contact in matching_contacts:
            print("\nFirst Name:", contact[0], "\nLast Name:",
                  contact[1], "\nPhone:", contact[2], "\nEmail:", contact[3])
    # if not
    else:
        print("No matching contacts.")


# function to find a contact
def find_contact(contacts_list):

    # get searching method
    filtering = second_decision()

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


# function to get the first name for new contact
def get_first_name():
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


# function to get the last name for new contact
def get_last_name():
    last_name = input("Give Last Name or skip by pressing Enter: ")
    if last_name == '':
        print("You left Last Name empty. OK.")

    return last_name


# function to get the phone for new contact
def get_phone():
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


# function to get the email for new contact
def get_email():
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


#  Function to insert a contact to .csv file
def insert_contact(contacts_file):
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
