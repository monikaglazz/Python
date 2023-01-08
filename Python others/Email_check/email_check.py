import re


def check(email):
    """Check for validity of email.

    Example:
    alma.random@random.com - True
    alma.random@random.com cc - False
    //alma.random@random.com cc - False

    Args:
        email (str): address email to check

    Returns:
        bool: True for valid email, False for not valid
    """

    # Get te pattern for email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,3}\b'
    # pass the pattern and the string into the fullmatch() method
    if (re.fullmatch(pattern, email)):
        return True
    else:
        return False


def check2(email):
    """Check for validity of email.

    Example:
    alma.random@random.com - True
    alma.random@random.com cc - False
    //alma.random@random.com cc - False

    Args:
        email (str): address email to check

    Returns:
        bool: True for valid email, False for not valid
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
