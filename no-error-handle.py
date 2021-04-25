# Run this code either through command line or in the Python shell.
# Enter a year without spaces into the prompt, or the program will not
# accept the input. If the input is bad, the program ends. If the input
# is good, the program prints whetehr the year entered is a leap year.
# If you would like to run the program again, rerun the program with
# either command line or the Python shell.

def isLeap( year ):
    if (x % 4 == 0):
        if (x % 100 == 0):
            if (x % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


str_x = input("Enter year: ")


print("Is leap year:", isLeap(x))
