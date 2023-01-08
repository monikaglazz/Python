
def palindromes(word):
    """Checks if a word is a palindrome.

    Args:
        word (str): word to check

    Returns:
        bool: True if it is a palindrome and False if not
    """
    # change the position of letters
    reverse = word[::-1]

    # lowering all letter and comparing
    if reverse.lower() == word.lower():
        return True
    else:
        return False


def reverse_dictionary(diction):
    """Switch keys with values in a dictionary.

    Args:
        diction (dict): dictionary to reverse

    Returns:
        dict: dictionary with reversed keys and values.
    """
    rev_dictionary = {value: key for key, value in diction.items()}
    return rev_dictionary


dic_before_reverse = {"anna": 22, "sophie": 33}

print(reverse_dictionary(dic_before_reverse))

print(palindromes("eye"))
print(palindromes("cat"))
