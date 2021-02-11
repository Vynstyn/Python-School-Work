""" Roger Rues          Student ID: 1000130372
    Program Exercise# 2-9 Assignment# 0
    Due Date:

    Program Description:
        This program should ask the user to enter a temperature in Celsius, then display
        the temperature converted to Fahrenheit.
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Variables

userTemp = 0.00
newTemp = 0.00

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

print("This program converts temperatures in Celsius to Fahrenheit.")
print()

userTemp = float(input("Enter a temperature in Celsius so that it can be converted to Fahrenheit: "))
newTemp = ((9 / 5) * userTemp) + 32
print()

print(f"Your temperature {userTemp:.2f} Celsius converted to Fahrenheit is {newTemp:.2f}")

print("\n")         #*** newlines prior to os message
#*** End execution of the program