__author__ = 'James'


class Error(Exception):
    def __init__(self, error):
        super(Error, self).__init__(Exception)


class Country:
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        amount = int(input("Enter your amount: "))
        amount = float(amount)
        print({}, {}, {} + format(amount, ".2f"))
        if name.isalpha() is False:
            print("Country can only have letters")


    def __str__(self, **kwargs):
        return "{}, {}, {}".format(self.name, self.currency_code, self.currency_symbol)


# class Details:
#     def