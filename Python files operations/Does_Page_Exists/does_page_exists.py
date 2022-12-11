# The file pages.txt is a list of pages
# Program opens this file and check if page
# exists or not. After checking it is writing
# the url to specified file: working_pages.txt if
# the page exists an not_working_pages.txt if page
# does not exists.

import requests
from requests.exceptions import ConnectionError


# Function try to load the page and looking for status_code
def does_page_exist(page):
    try:
        status = requests.get(page)
        return True
    except ConnectionError:
        return False


# Create files to write url after checking
workingPages = open("working_pages.txt", "w", encoding="UTF-8")
notWorkingPages = open("not_working_pages.txt", "w", encoding="UTF-8")

# Open file and checking pages
with open("pages.txt", "r", encoding="UTF-8") as file:
    readFile = file.read().split("\n")
    for line in readFile:
        if does_page_exist(line) is True:
            workingPages.write(line + "\n")
        else:
            notWorkingPages.write(line + "\n")


workingPages.close()
notWorkingPages.close()
