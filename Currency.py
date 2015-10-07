__author__ = 'James'

import web_utility

incorrect_value = -1
error_string = "class=bld"

# Currency is converted using the google currency converter website


def convert(amount, first_currency, second_currency):
    url_string = "https://www.google.com/finance/converter".format(amount, first_currency.upper(),
                                                                   second_currency.upper())
    result = web_utility.load_page(url_string)
    if first_currency == second_currency:
        return incorrect_value
    elif error_string not in result:
        return incorrect_value
    else:
        return result[(result.find('class=bld>') + 10):(result.find('</span>') - 4)]


# Converts the country information from a text file into a tuple

def get_details(country_name):
    input_file = open('currency_details.txt', mode='r', encoding='utf-8')
    lines = input_file.readlines()

    for line in lines:
        if country_name in line:
                return tuple(list(line.strip('\n').split(',')))
        elif country_name not in line:
            return tuple()
    input_file.close()
    return()


# # Used to test if the code works
#     conversion_amount = (str(input("How much would you like to convert?")))
#     first_country = (str(input("Select the first country")))
#     second_country = (str(input("Select the second country")))
#     result = (convert(amount_to_convert, first_country, second_country))


if __name__ == "__main__":
    print("This module is running by itself")
else:
    print("This module is being imported")
# Github Test