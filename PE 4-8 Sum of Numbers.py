""" Roger Rues          Student ID: 1000130372
    Program Exercise# 0 Assignment# 0
    Due Date:

    Program Description:
        This program will ask the user in a loop to enter a series of positive numbers.
        The user will enter a negative number to end the loop. The program will then display their sum.
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
#*** Variables
sum = 0


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Process

print("This program will display the sum of all positive numbers entered. To end the program, enter any negative number. ")
print()

validEntry = False
while not validEntry:
    try:
        number = int(input("Enter a number: "))
        validEntry = True
    except ValueError:
        print("ERROR: Invalid entry. Value must a whole number.")
        print()



while number > 0:
    sum += number
    print()
    validEntry = False
    while not validEntry:
        try:
            number = int(input("Enter a new number: "))
            validEntry = True
        except ValueError:
            print("ERROR: Invalid entry. Value must a whole number.")
            print()
    



#*** Report

print()
print(f"The sum of the numbers entered is {sum}.")


print("\n")         #*** newlines prior to OS message
#*** End execution of the program