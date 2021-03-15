# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

# Solution: 

a = [5, 10, 15, 20, 25]
# b = [a[0], a[-1]]
# print(b)
def list_ends(x):
    return [x[0], x[-1]]
print(list_ends(a))
