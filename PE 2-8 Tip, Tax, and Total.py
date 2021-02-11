""" Roger Rues          Student ID: 1000130372
    Program Exercise# 2-8 Tip, Tax, and Total
    Due Date:

    Program Description:
        This program calculates the tip, sales tax, and total of a food charge.
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
TIP_RATE = .18
TAX_RATE = .07

#*** Variables


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

print("This program displays the total charge of food service, includes tip and tax.")
print()

charge = float(input("Enter Food Charge: "))
print()

#*** Process
salesTax = TAX_RATE * charge
tip = TIP_RATE * charge
totalCharge = charge + tip + salesTax

#*** Report
print(f"Food charge : ${charge:7,.2f}")
print(f"Sales Tax   : ${salesTax:7,.2f}")
print(f"Tip         : ${tip:7,.2f}")
print(f"Total Charge: ${totalCharge:7,.2f}")


print("\n")         #*** newlines prior to os message
#*** End execution of the program