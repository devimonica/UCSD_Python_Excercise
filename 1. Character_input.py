# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

    # Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
    # (Hint: order of operations exists in Python)
    # Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Solution:
name = input('Enter Name: ')
age = input('Enter Age: ')
copies = input('Enter no.of copies: ')
year_100 = 2020 + (100 - int(age))
# for i in range(int(copies)):
#     print(f'You will be 100 years old by {year_100}')
print(int(copies) * f'You will be 100 years old by {year_100} \n')
