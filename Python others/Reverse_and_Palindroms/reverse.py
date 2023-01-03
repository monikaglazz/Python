
def palindromes(word):
    """Function returns True if the word is the same when read backwards,
    else returns False."""
    # change the position of letters
    reverse = word[::-1]

    # lowering all letter and comparing
    if reverse.lower() == word.lower():
        return True
    else:
        return False


def reverse_dictionary(diction):
    """Function returns dictionary with switched keys and values"""
    rev_dictionary = {value: key for key, value in diction.items()}
    return rev_dictionary


dic_before_reverse = {"anna": 22, "sophie": 33}

print(reverse_dictionary(dic_before_reverse))

print(palindromes("eye"))
print(palindromes("cat"))
