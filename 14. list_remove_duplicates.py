# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

# Solution:

def remove_duplicates():
    first_list = input('Enter a list: ')
    second_list = []
    for number in first_list:
        if number not in second_list:
            second_list.append(number)
    return second_list
print(remove_duplicates())
