# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you.

# Solution:

## This solution does not predict correctly for all the numbers

given_number = int(input('Enter a number: '))
numbers = range(2, given_number+1)
def prime():
    if given_number == 1:
        print('It is not a prime number')
    elif given_number == 2:
        print('It is a prime number')
    else:
        for number in numbers:
            if given_number % number != 0:
                print('It is a prime number')
                break
            else:
                print('It is not a prime number')
                break
prime(given_number)


# Corrected solution:

def prime_num(checking_num):
    if checking_num == 1:
        print('not a prime number')
    if checking_num == 2:
        print('it is a prime number')
    elif checking_num > 2:
        for number in range(2, checking_num):
            if checking_num % number == 0:
                print('it is not a prime number')
                break
    else:
        print('It is a prime number')
        
        
prime_num(9)
