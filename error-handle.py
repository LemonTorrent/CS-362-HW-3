# Run this code either through command line or in the Python shell.
# Enter a year without spaces into the prompt, or the program will not
# accept the input. If the input is bad, the program ends. If the input
# is good, the program prints whetehr the year entered is a leap year.
# If you would like to run the program again, rerun the program with
# either command line or the Python shell.

def handleInput( year_input ):
    for i in range(len(year_input)):
        if ( (year_input[i] < '0') or (year_input[i] > '9') ):
             return False
    return True

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

# print(handleInput(str_x))

if (handleInput(str_x) == True):
    x = int(str_x)
    print("Is leap year:", isLeap(x))
else:
    print("Invalid input")
