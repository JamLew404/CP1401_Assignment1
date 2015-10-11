__author__ = 'James'

# Imports the web_utility for use in this module
import web_utility

# A constant value for use across the module
incorrect_value = -1
error_string = "class=bld"

# Currency is converted using the google currency converter website


def convert(amount, first_currency, second_currency):
    url_string = "https://www.google.com/finance/converter?a={}&from={}&to={" \
                 "}".format(amount, first_currency.upper(), second_currency.upper())
    result = web_utility.load_page(url_string)
    if first_currency == second_currency:
        return incorrect_value
    elif error_string not in result:
        return incorrect_value
    else:
        return result[(result.find('class=bld>') + 10):(result.find('</span>') - 4)]


# Converts the country information from a text file into a tuple

def get_details(country_name):
    if country_name == " ":
        return tuple()
    input_file = open('currency_details.txt', encoding='utf-8')
    lines = input_file.readlines()

    for line in lines:
        if line.startswith(country_name):
                return tuple(line.strip().split(','))
        elif country_name not in line:
            return tuple()
    input_file.close()
    return()

if __name__ == "__main__":
    print("This module is running by itself")
else:
    print("This module is being imported")