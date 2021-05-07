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

if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True
