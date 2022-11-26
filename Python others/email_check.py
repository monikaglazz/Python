import re


# Define first function for validating an Email
def check(email):
    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the pattern and the string into the fullmatch() method
    if (re.fullmatch(pattern, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


# Define second function for validating an Email
def check2(email):
    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the pattern and the string into the match() method
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")


email = input("Insert your email: ")

check(email)
check2(email)
