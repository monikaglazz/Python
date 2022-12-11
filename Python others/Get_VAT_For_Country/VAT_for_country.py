import csv


# convert csv to list
def change_csv_to_list(file):
    file_open = open(file)
    file_read = csv.reader(file_open)

    file_list = [data for data in file_read]

    file_open.close()

    return file_list


# show all countries with indexes
def print_all_countries(country_list):

    index = 1
    for country in country_list:
        if index <= 28:
            print("Index:", index, "EU Country:", country[0])
        else:
            print("Index:", index, "Country:", country[0])

        index += 1


# get price from user
def get_price():
    while True:
        try:
            price = float(input("\nGive me your price: "))
            break
        except ValueError:
            print("You can use only numbers and dot, e.x.: 200.45")

    return price


# get the country idex
def get_country_index(country_list):
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


# get tax value in % for county index
def get_country_VAT(country_list, country_index):

    index = 1
    tax_value = 0
    for country in country_list:
        if index == country_index:
            tax_value = country[1]
            break
        index += 1

    return tax_value


# return a price before VAT
def price_before_VAT(price, country_index, country_list):
    tax_value = get_country_VAT(country_list, country_index)
    return round(((1 - (float(tax_value) / 100)) * price), 4)


# return value after VAT
def price_after_VAT(price, country_index, country_list):
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
