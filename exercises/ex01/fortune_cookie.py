"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730318823"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
    
# Begin your solution here...

message: int = randint(1,4)


if message == 1:
    print("Invest in Gamestock. Hold on for dear life.")
else:
    if message == 2:
        print("GET COVID TEST IMMEDATILY!")
    else:
        if message == 3: 
            print("You will get an A on this assignment.")
        else:
            print("You will get an F on this assignment.") 