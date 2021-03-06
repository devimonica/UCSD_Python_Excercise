# Write a program that asks the user how many Fibonacci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# Solution:

sequence = int(input('Enter the length of sequence: '))
def generate_fibonacci():
    start_number = 1
    fibonacci = []
    if sequence == 0:
        fibonacci = []
    elif sequence == 1:
        fibonacci = [1]
    elif sequence == 2:
        fibonacci = [1, 1]
    elif sequence > 2:
        fibonacci = [1, 1]
        while len(fibonacci) < sequence:
            fibonacci.append(fibonacci[start_number]+fibonacci[start_number-1])
            start_number += 1
    return fibonacci
print(generate_fibonacci())
