import string
import random

length = int(input("Enter a number for your password's length: "))

letters = string.ascii_letters
digits = string.digits
symbol = string.printable

mix = letters +  digits + symbol

password = ''.join(random.sample(mix, length))

print(password)
