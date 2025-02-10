import random

import string
from numpy.core.defchararray import isdigit

print("Welcome to Password generator!")

def password_question(text):
    while True:
        password_input = input(text)
        if isdigit(password_input):
            password_input = int(password_input)
            break
    return password_input

password_letters = password_question("How many letters would you like in your password: \n")
password_symbols = password_question("How many symbols would you like in your password: \n")
password_numbers = password_question("How many numbers would you like in your password: \n")

letters = list(string.ascii_letters)
symbols = list(r"""!@#$%^&*()_+-=[]{}|;:'",.<>?/`~""")
numbers = list(string.digits)

new_password = []

for actual_letter in range(password_letters):
    new_password.append(random.choice(letters))
for actual_symbol in range(password_symbols):
    new_password.append(random.choice(symbols))
for actual_number in range(password_numbers):
    new_password.append(random.choice(numbers))

random.shuffle(new_password)

definitive_password = "".join(str(char) for char in new_password)

print(f"Your new password is: {definitive_password}")