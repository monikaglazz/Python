
# create empty list to contain names and surnames for future operations
list_of_persons = []

# Open a file with name and surnames and change it to the list od persons
with open('name_and_surname.txt', 'r', encoding="UTF-8") as name_and_surname:
    all_persons = name_and_surname.readlines()
    for single_person in all_persons:
        list_of_persons.append(single_person.split())

    print(list_of_persons)


# Open a file and write ony [0] position for each pearson to file
with open("names.txt", "w", encoding="UTF-8") as names:
    for person in list_of_persons:
        names.write(person[0] + "\n")


# Open a file and write ony [1] position for each pearson to file
# If there is no surname it leaves the empty line
with open("surnames.txt", "w", encoding="UTF-8") as surnames:
    for person in list_of_persons:
        try:
            surnames.write(person[1] + "\n")
        except IndexError:
            surnames.write("" + "\n")
