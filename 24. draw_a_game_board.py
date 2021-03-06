# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

# Remember that in Python 3, printing to the screen is accomplished by

#   print("Thing to show on screen")

# Hint: this requires some use of functions, as were discussed [previously on this blog] and [elsewhere on the Internet, like this TutorialsPoint link].
# previously on this blog - https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# elsewhere on the Internet, like this TutorialsPoint link - http://www.tutorialspoint.com/python/python_functions.htm?utm_source=7_&utm_medium=affiliate&utm_content=5f34cd37cdf1050001b09537&utm_campaign=Admitad&utm_term=a5e196742126bebb5adcdb73b91b882c

# Trivial solution:

a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))

# Solution using a while loop:

def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = "--- "
    ve = "|   "
    ho = ho * kamal
    ve = ve * (kamal+1)
    while i < kamal+1:
        print ho
        if not (i == kamal):
            print ve
        i += 1
