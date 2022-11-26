import random

# define alphabet upper letters
alphabet_upper = "ABCDEFGHIJKLMNOPRSQTUWXYZ"


# define alphabet lower letters
alphabet_lower = "abcdefghijklmnoprsqtuwxyz"

# define number
numbers = "1234567890"

# define special marks
special_marks = "?/}{[]+=_-!@#$%^&*()"


# check if the user picks y, n or something different
def check_up(letter):
    if letter == 'y' or letter == 'n':
        return letter
    else:
        print("You can choose only y or n.")
        return ''


# test if given value is a number
def test(value):
    try:
        value_test = int(value)
        return True
    except ValueError:
        print("\nIt has to be a number.")
        return False


#  generate password
def generate_password(howManyDigits, symbols_for_password):
    password = "".join(random.sample(symbols_for_password, howManyDigits))
    return password


x = False
y = False

# get the password length
while x == False:
    how_long = input("\nHow long your password may be: ")
    x = test(how_long)

#  get number of passwords
while y == False:
    how_many = input("\nHow many passwords you want: ")
    y = test(how_many)


print("\nChoose what do you want to include in your password. Chose y for yes and n for no. ")

alphabet_up = ''
alphabet_l = ''
num = ''
special_m = ''
symbols_for_password = ''

#  get decision if upper letters may be included
while alphabet_up == '':
    user_input = input("\nDo you want to include upper letters y/n: ")
    alphabet_up = check_up(user_input)

# if y add upper letters to symbols
if alphabet_up == 'y':
    symbols_for_password += alphabet_upper

#  get decision if lower letters may be included
while alphabet_l == '':
    user_input = input("Do you want to include lower letters y/n: ")
    alphabet_l = check_up(user_input)

# if y add lower letters to symbols
if alphabet_l == 'y':
    symbols_for_password += alphabet_lower

#  get decision if numbers may be included
while num == '':
    user_input = input("Do you want to include numbers y/n: ")
    num = check_up(user_input)

# if y add numbers to symbols
if num == 'y':
    symbols_for_password += numbers

#  get decision if special marks may be included
while special_m == '':
    user_input = input("Do you want to include special marks y/n: ")
    special_m = check_up(user_input)

# if y add special marks to symbols
if special_m == 'y':
    symbols_for_password += special_marks

x = 0

# generate passwords
while x < int(how_many):
    print(generate_password(int(how_long), symbols_for_password))
    x += 1
