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
count = 1
grade = 0
sumOfGrades = 0
average = 0

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Process

grade = int(input(f"Enter grade #{count} or -99 to end: "))
while grade != -99:
    while (grade != -99 and (grade < 0 or grade > 100)):
        print(f"{' ':4}ERROR: Invalid grade.")
        grade = int(input(f"{' ':4}Enter grade #{count} or -99 to end: "))

    if grade == -99:
        continue

    sumOfGrades += grade
    count += 1
    grade = int(input(f"Enter grade #{count} or -99 to end: "))

#*** Report
count -= 1

if count > 0:
    average = sumOfGrades / count


print(f"{count} {sumOfGrades} {average}")


print("\n")         #*** newlines prior to OS message
#*** End execution of the program