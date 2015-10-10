__author__ = 'James'


class Error(Exception):
    def __init__(self, error):
        super().__init__(error)


class Country:
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        if name.isalpha() is False:
                print("Country can only have letters")

    def __str__(self, **kwargs):
        return " {} {} {} ".format(self.name, self.currency_code, self.currency_symbol)

    def amount_format(self, amount):
        amount = float(amount)
        if amount < 0:
            raise Error("The amount cannot be less than 0")
        return "{}{}".format(self.currency_symbol, format(amount, ".2f"))


class Details:
    locations = []

    def __int__(self, locations):
        self.locations = locations

    def add(self, country_name, start_date, end_date):
        country_name = str(country_name)
        # Set date formats and make errors for incorrect dates entered
        try:
            start_date.datetime.datetime.strftime("%Y, %m, %d")
        except ValueError:
            raise Error("Incorrect date format entered")
        try:
            end_date.datetime.datetime.strftime("%Y, %m, %d")
        except ValueError:
            raise Error("Incorrect date format entered")
        # exception if add is already in locations
        except:
            if self.add in self.locations:
                return None
        # if statement for raising error when the start date is after the end date
        if end_date < start_date:
            raise Error("You must enter a start date that is before the end date")
        # Enter location into table
        self.locations.append((country_name, start_date, end_date))

    @staticmethod
    def is_empty():
        if not Details.locations:
            return "There is nothing in Locations"
        return "There is something in Locations"

