# Adding two numerical values together
# From a Menu that allows the app to quit
# If a value that is not reconised as a number the an exceptio ValueError is issued
# and the app restarts
# app closes after a correct sum has completed
#


def get_num():
    try:
        i = input("Enter a number: ")
        i = float(i)
    except ValueError:
        print("Value entered is not a number")
        display_menu()
    return i


def display_menu():
    print("\nQ. Quit. ")
    print("1. Add 2 numbers.\n")
    c = input("Enter your choice: ")
    c = c.lower()

    if c == "q":
        print("Program Exits Now!")
        exit()
    elif c == "1":
        x = get_num()
        y = get_num()
        z = x + y

        print("The addtion of the two values equals ", z)
        exit()

                                                                                          
while True:
    display_menu()
