# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele

# Then I would see the string:

#   Michele is name My

# shown back to me.

# Solution:

def reverse_order():
    string = input('Enter a sentence: ')
    # words = string.split()
    # new_string = words[::-1]
    # result = " ".join(new_string)
    # return result
    return " ".join(string.split()[::-1])
print(reverse_order())
