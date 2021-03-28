#Functions
def main():
    response = True
    while response:
        color = int(input("Enter a selection green(1), orange(2), purple(3): "))
        while color < 1 or color > 3:
            print("ERROR: Color must be between 1 and 3.")
            color = int(input("Enter a selection green(1), orange(2), purple(3): "))

        if color >= 1 and color <= 3:
            if color == 1:
                x = green()
                print(x)
            elif color == 2:
                print(orange())
            else:
                print(purple())
        response = continue_program()


def green():
    return "Green = blue and yellow"


def orange():
    return "Orange = red and yellow"


def purple():
    return "Purple = blue and red"

def continue_program():
    response = input("Would you like to continue? (Y/N): ").upper()
    if response == "Y":
        return True
    else:
        return False


#Execute Functions
main()