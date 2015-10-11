__author__ = 'James'
import Trip
import Currency

user_input1 = input(str("Enter First Country"))
user_input2 = input(str("Enter Second Country"))
user_input3 = input(str("Enter amount to convert"))
convert_amount = Currency.convert(user_input3, user_input1, user_input2)
print(convert_amount)

print(Currency.convert("1", "AUD", "AUD"))
print(Currency.convert("1", "JPY", "ABC"))
print(Currency.convert("1", "ABC", "USD"))
print(Currency.convert("10.95", "AUD", "JPY"))
print(Currency.convert("943.18", "JPY", "AUD"))
print(Currency.convert("10.95", "AUD", "BGN"))
print(Currency.convert("13.62", "BGN", "AUD"))
print(Currency.convert("200.15", "BGN", "Jpy"))
print(Currency.convert("13859.49", "JPY", "BGN"))
print(Currency.convert("100", "JPY", "USD"))
print(Currency.convert("0.83", "USD", "JPY"))
print(Currency.convert("19.99", "USD", "BGN"))
print(Currency.convert("34.58", "BGN", "USD"))
print(Currency.convert("19.99", "USD", "AUD"))
print(Currency.convert("27.80", "AUD", "USD"))

print(Currency.get_details("Unknown"))
print(Currency.get_details("Japanese"))
print(Currency.get_details(""))
print(Currency.get_details("Australia"))
print(Currency.get_details("Japan"))
print(Currency.get_details("Hong Kong"))

print(Trip.Details.is_empty())
print(Trip.Details.locations)
Trip.Details.add("Australia", "2014/01/02", "2015/02/04")
print(Trip.Details.is_empty())
print(Trip.Details.locations)

Australia = Trip.Country("Australia", "AUD", "$")
print(Australia)