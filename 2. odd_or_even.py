# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Solution:

number = input('Enter a number: ')
value_2 = int(number) % 2
value_4 = int(number) % 4
if value_2 == 0 and value_4 == 0:
    print('The number is even and multiple of 4')
elif value_4 == 0:
    print('The number is multiple of 4')
elif value_2 == 0:
    print('The number is even')
else:
    print('The number is odd')

num = input('Enter a number: ')
check = input('Enter another number to check :')
result = int(num) / int(check)
if result % 2 == 0:
    print('The numbers are evenly divisible')
else:
    print('The numbers are not evenly divisible')
