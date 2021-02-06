"""An exercise in remainders and boolean logic."""

__author__ = "730318823"


# Begin your solution here...

test: int = int(input("Enter a number!"))

if test % 2 == 0 and test % 7 == 0:
    print("TAR HEELS")
else:
    if test % 7 == 0:
        print("HEELS")
    else:
        if test % 2 == 0:
            print("TAR")
        else:
            print("CAROLINA")

