# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# Solution:

# This solution generates a password which definitely contains one lower case, one uppercase, one number and one symbol

import string
import random
alphabets_lower = list(string.ascii_lowercase)
alphabets_upper = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)
password = []
for i in range(2):
    password.append(random.choice(alphabets_lower))
    password.append(random.choice(alphabets_upper))
    password.append(str(random.choice(numbers)))
    password.append(str(random.choice(symbols)))
    final = ''.join(password)
print(final)

# Solution 2:

# This solution randomly generates from everything. It is not mandatory that it contains all the categories like above.

characters = list(string.printable)
password = []
for i in range(8):
    password.append(str(random.choice(characters)))
    result = ''.join(password)
print(result)
