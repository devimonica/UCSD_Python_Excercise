# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

#     Use binary search.
    
# Solution:

def element_search(list_num, check_num):
    is_present = False
    if check_num in list_num:
        is_present = True
    return is_present
print(element_search([1,2,3], 13))

# Solution with binary search: