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
LIMIT = 5
#*** Variables
#count = 1
grade = 0
sumOfGrades = 0
average = 0

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Process


for count in range(1, LIMIT + 1):
    grade = int(input(f"Enter grade #{count}: "))
    while (grade < 0 or grade > 100):
        print(f"{' ':4}ERROR: Invalid grade.")
        grade = int(input(f"{' ':4}Enter grade #{count}: "))

    sumOfGrades += grade


#*** Report

average = sumOfGrades / count


print(f"{count} {sumOfGrades} {average}")


print("\n")         #*** newlines prior to OS message
#*** End execution of the program