""" Roger Rues          Student ID: 1000130372
    Program Exercise# 3-13 Shipping Charges Assignment# 2B
    Due Date: 3/4/21

    Program Description:
        This program asks the user to input the weight of a package they want to ship. It then displays
        the shipping charges. 
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
MINIMUM_PACKAGE_WEIGHT = 0
MAXIMUM_PACKAGE_WEIGHT = 20

#*** Variables
morePackages = "Y"

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")


print("This program asks the user to input the weight of a package and then displays the shipping charges. ")
print()


#*** Process

while morePackages.upper() == "Y":
    packageWeight = float(input("Please enter the weight of a package you would like to ship: "))
    print()
    while packageWeight <= MINIMUM_PACKAGE_WEIGHT or packageWeight > MAXIMUM_PACKAGE_WEIGHT:
        print(f"ERROR: Invalid input. The weight of a package must be more than {MINIMUM_PACKAGE_WEIGHT} pounds but not greater than {MAXIMUM_PACKAGE_WEIGHT} pounds. Please try again. ")
        packageWeight = float(input("Please enter the weight of a package you would like to ship: "))
        print()

    if packageWeight > 10:
        shippingRate = 4.75
    elif packageWeight > 6:
        shippingRate = 4.00
    elif packageWeight > 2:
        shippingRate = 3.00
    else:
        shippingRate = 1.50

    #*** Report

    print(f"The shipping charges for the package that weights {packageWeight:.2f} pounds is ${shippingRate:.2f}")
    morePackages = input("Would you like to enter the weight of another package? (Y/N): ")
    print()
    while morePackages.upper() != "Y" and morePackages.upper() != "N":
        print("ERROR: Invalid input. Please try again. ")
        morePackages = input("Would you like to enter the weight of another package? (Y/N): ")
        print()

print("Thank you for shopping at The Fast Freight Shipping Company. Have a nice day! ")

print("\n")         #*** newlines prior to OS message
#*** End execution of the program