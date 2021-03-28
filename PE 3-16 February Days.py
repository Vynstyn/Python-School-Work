""" Roger Rues          Student ID: 1000130372
    Program Exercise# 3-16 Febrruary Days Assignment# 0
    Due Date:

    Program Description:
        This program displays the amount of days in the month of February
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
#*** Variables
leapYearFlag = False

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Process
print("This program displays the amount of days in the month of February. ")
print()

year = int(input("Enter the year: "))

if (year % 100 == 0):
	if(year % 400 == 0):
		leapYearFlag = True
else:
    if (year % 4 == 0):
        leapYearFlag = True






#*** Report

if (leapYearFlag):
	print(f"In {year} February has 29 days.")
else:
	print(f"In {year} February has 28 days. ") 


print("\n")         #*** newlines prior to OS message
#*** End execution of the program