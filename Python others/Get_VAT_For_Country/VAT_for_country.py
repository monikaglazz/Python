import csv


def change_csv_to_list(file):
    """Convert .csv file to a list

    Args:
        file (str): name of source file

    Returns:
        int: 0 if file is not existing
        or
        list: list of str with countries
    """

    try:
        file = open(file)
    except FileNotFoundError:
        print("File is not existing.")
        return 0

    # read .csv
    file_read = csv.reader(file)

    # convert to list
    file_list = [data for data in file_read]

    file.close()

    return file_list


def print_all_countries(country_list):
    """Function prints all countries from list.

    Args:
        country_list (list): list of str with countries
    """

    index = 1
    for country in country_list:
        if index <= 28:
            print("Index:", index, "EU Country:", country[0])
        else:
            print("Index:", index, "Country:", country[0])

        index += 1


def get_price():
    """Get price from a user.

    Returns:
        float: price of product from a user.
    """

    while True:
        try:
            price = float(input("\nGive me your price: "))
            break
        except ValueError:
            print("You can use only numbers and dot, e.x.: 200.45")

    return price


def get_country_index(country_list):
    """Checks correctness of country index.

    Args:
        country_list (list): list of str with countries

    Returns:
        int: index of a county
    """

    print("\nCountries from 1 - 28 are in EU, 29 - 167 are outside EU.")
    print("All countries are in alphabetical order.\n")
    print_all_countries(country_list)

    while True:
        try:
            country_index = int(input("\nIndex of your country: "))
        except ValueError:
            print("It has to be a number.")
            continue

        if 0 > country_index or country_index > 167:
            print("It has to be a number from 1 - 167.")
        else:
            break

    return country_index


def get_country_VAT(country_list, country_index):
    """Gets a tax value for a country.

    Args:
        country_list (list): list of str with countries
        country_index (int): index of a county

    Returns:
        int: tax value for a country
    """

    index = 1
    tax_value = 0
    for country in country_list:
        if index == country_index:
            tax_value = country[1]
            break
        index += 1

    return tax_value


def price_before_VAT(price, country_list, country_index):
    """Gets the price before the tax was added.

    Args:
        price (float): price given by the user
        country_list (list): list of str with countries
        country_index (int): index of a county

    Returns:
        float: price before the tax was added
    """
    tax_value = get_country_VAT(country_list, country_index)
    return round(((1 - (float(tax_value) / 100)) * price), 4)


def price_after_VAT(price, country_list, country_index):
    """Gets the price with the tax.

    Args:
        price (float): price given by the user
        country_list (list): list of str with countries
        country_index (int): index of a county

    Returns:
        float: price with the tax
    """
    tax_value = get_country_VAT(country_list, country_index)
    return round(((1 + (float(tax_value) / 100)) * price), 5)


print("\nHello! You can check the VAT tax with this calculator!")

# explanation what VAT is
print("""\nA value-added tax (VAT), known in some countries as
a goods and services tax (GST), is a type of tax that is assessed
incrementally. It is levied on the price of a product or service
at each stage of production, distribution, or sale to the end consumer.
If the ultimate consumer is a business that collects and pays to the
government VAT on its products or services, it can reclaim the tax paid""")

# Start the program
while True:

    print("""\nChoose what do you want to do:
    1 - know product value before tax was added (u have product price with VAT)
    2 - know product value with added tax (u have product price without VAT)
    3 - exit""")

    # get user choice and check for mistakes
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("It has to be a number: 1, 2 or 3.")
        continue

    # change csv to a list
    country_list = change_csv_to_list("VAT_for_country.csv")

    if choice == 1:
        # get the price of product
        price = get_price()

        # get the country index
        country_index = get_country_index(country_list)

        # return price before tax
        price_before = price_before_VAT(price, country_index, country_list)
        print("Price with VAT:", price, "Price before VAT:", price_before)
    elif choice == 2:
        # get the price of product
        price = get_price()

        # get the country index
        country_index = get_country_index(country_list)

        # return price after tax
        price_after = price_after_VAT(price, country_index, country_list)
        print("Price before VAT:", price, "Price after VAT:", price_after)
    elif choice == 3:
        print("Bye!")
        break
    else:
        print("It can only be: 1, 2 or 3.")
