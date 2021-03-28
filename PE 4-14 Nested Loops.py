""" Roger Rues          Student ID: 1000130372
    Program Exercise# PE 4-24 Nested Loops Assignment# 0
    Due Date:

    Program Description:
        This program demonstrates the use of nested for loops.
        This program will produce 2 triangles (upright, upside down).
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
#*** Variables


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

print("This program will produce an upright traingle and an upside down traingle.")
limit = int(input("Enter a number to create a square: "))
print()

#*** Process

#*** Report

# Upside down triangle
print("Upside down triangle.")
for counter in range(limit):
    for count in range(limit-counter):
        print("*", end ='')
    print()

print()


#Upright triangle
print("Upright triangle.")
for column in range(limit):
    for row in range(column):
        print("*", end='')
    print()

print("\n")         #*** newlines prior to OS message
#*** End execution of the program