import requests
from requests.exceptions import ConnectionError


def does_page_exist(page):
    """Sort working and not working pages.

    Args:
        page (str): link to page to check

    Returns:
        bool: True if exists, False if not
    """

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
