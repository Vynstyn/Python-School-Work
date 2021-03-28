""" Roger Rues          Student ID: 1000130372
    Program Exercise# 0 Assignment# 0
    Due Date:

    Program Description:
        This program is a template for python programs.
        Replace these statements with the description of your program.
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
#*** Variables


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Process
#*** Report

#Function Definition
def main():
    greeting()
    print()
    closure()
    print()
    for count in range(5):
        greeting()

def greeting():
    print("Hello world!")

def closure():
    print("Goodbye!")

#Execute Functions
print("-----------")
main()
print("------------")

print("\n")         #*** newlines prior to OS message
#*** End execution of the program