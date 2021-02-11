""" Roger Rues          Student ID: 1000130372
    Program Exercise# 2-6 Sales Tax Assignment# 1
    Due Date: 2/18/21

    Program Description:
        This program asks the user for the purchase amount and calculates county tax, state tax,
        total tax, and total sales amount. The program then displays these amounts.
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program

#*** Constants

STATE_TAX_RATE = .05
COUNTY_TAX_RATE = .025

#*** Variables

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

print("This program displays the total sales amount including initial purchase amount, county tax, state tax, and total tax.")
print()

purchaseAmount = float(input("Enter purchase amount: "))
print()

#*** Process

countyTax = purchaseAmount * COUNTY_TAX_RATE
stateTax = purchaseAmount * STATE_TAX_RATE
totalSalesTax = stateTax + countyTax
totalSalesAmount = purchaseAmount + totalSalesTax

#*** Report

print(f"{'Amount of Purchase:':20} ${purchaseAmount:10,.2f}")
print(f"{'County Sales Tax:':20} ${countyTax:10,.2f}")
print(f"{'State Sales Tax:':20} ${stateTax:10,.2f}")
print(f"{'Total Sales Tax:':20} ${totalSalesTax:10,.2f}")
print(f"{'Total Sales Amount:':20} ${totalSalesAmount:10,.2f}")


print("\n")         #*** newlines prior to OS message
#*** End execution of the program