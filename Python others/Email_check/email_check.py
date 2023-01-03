import re


def check(email):
    """Function returns True for valid email and False for invalid.
    If the whole string matches this regular expression, e.x.:
    alma.random@random.com - True
    alma.random@random.com cc - False
    //alma.random@random.com cc - False"""
    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,3}\b'
    # pass the pattern and the string into the fullmatch() method
    if (re.fullmatch(pattern, email)):
        return True
    else:
        return False


def check2(email):
    """Function returns True for valid email and False for invalid.
    If zero or more characters at the beginning of string match 
    this regex, e.x.:
    alma.random@random.com - True
    alma.random@random.com cc - True
    //alma.random@random.com cc - False
    """
    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,3}\b'
    # pass the pattern and the string into the match() method
    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Insert your email: ")

print(check(email))
print(check2(email))
