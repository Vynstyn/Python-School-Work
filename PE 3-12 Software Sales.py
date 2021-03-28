""" Roger Rues          Student ID: 1000130372
    Program Exercise# 3-12 Software Sales
    Due Date: 2/25/21

    Program Description:
        This program calculates discounts on software packages based on
        how many packages the user decides to purchase. 
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
PACKAGE_PRICE = 99

#*** Variables

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")
print("This program calculates discounts on software packages based on how many packages the customer decides to purchase.")
print()

packagesPurchased = int(input("Please enter how many packages you would like to purchase: "))
print()

#*** Process

if packagesPurchased >= 100:
    discountRate = .4
elif packagesPurchased >= 50 and packagesPurchased <= 99:
    discountRate = .3
elif packagesPurchased >= 20 and packagesPurchased <= 49:
    discountRate = .2
elif packagesPurchased >= 10 and packagesPurchased <= 19:
    discountRate = .1
else:
    discountRate = 0


purchaseAmount = packagesPurchased * PACKAGE_PRICE
discountAmount = purchaseAmount * discountRate
totalPurchaseAmount = purchaseAmount - discountAmount

#*** Report

if discountAmount == 0:
    print("You did not receive a discount. Please purchase 10 or more packages to receive a discount.")
    print(f"Your total purchase amount is ${totalPurchaseAmount:.2f}")
else:
    print(f"The discount amount is ${discountAmount:.2f}")
    print(f"Your total purchase amount after discount is ${totalPurchaseAmount:.2f}")


print("\n")         #*** newlines prior to OS message
#*** End execution of the program