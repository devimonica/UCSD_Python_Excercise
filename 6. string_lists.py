# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

# Solution:

string = input('Enter a string: ')
if string[:] == string[::-1]:
    print('This string is a palindrome')
else:
    print('This string is not a palindrome')
