__author__ = 'James'


class Error(Exception):
    def __init__(self, error):
        super().__init__(error)


class Country:
    # This is used to define the values
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        if name.isalpha() is False:
                print("Country can only have letters")

        # amount = int(input("Enter your amount: "))
        # amount = float(amount)
        # print({}, {}, {} + format(amount, ".2f"))

    def __str__(self, **kwargs):
        return " {} {} {} ".format(self.name, self.currency_code, self.currency_symbol)

    def amount_format(self, amount):
        if amount < 0:
            raise Error("The amount cannot be less than 0")
        amount = float(amount)


class Details:
    def __int__(self, locations):
        self.locations = locations
