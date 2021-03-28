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
#*** Variables


fruit1 = ''
fruit2 = ''
fruit3 = ''

amount1 = 0
amount2 = 0
amount3 = 0

price1 = 0.00
price2 = 0.00
price3 = 0.00

costFruit1 = 0.00
costFruit2 = 0.00
costFruit3 = 0.00

totalCost = 0.00


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")


fruit1 = input("Enter the name of the first fruit. ")
amount1 = int(input("Enter the quantity of fruit being sold. "))
price1 = float(input("Enter the price of the fruit being sold. ")) 
costFruit1 = amount1 * price1
print()

fruit2 = input("Enter the name of the second fruit. ")
amount2 = int(input("Enter the quantity of fruit being sold. "))
price2 = float(input("Enter the price of the fruit being sold. "))
costFruit2 = amount2 * price2
print()

fruit3 = input("Enter the name of the third fruit. ")
amount3 = int(input("Enter the quantity of fruit being sold. "))
price3 = float(input("Enter the price of the fruit being sold. "))
costFruit3 = amount3 * price3
print()

totalCost = costFruit1 + costFruit2 + costFruit3


print("*** Display 1")
print(f"{'Item':<7} Receipt")
print(f"{'-----':<7} --------")
print(f"{'  1':7} Item: {fruit1}")
print(f"{' ':7} Quantity: {amount1}")
print(f"{' ':7} Price: ${price1:.2f}")
print(f"{' ':7} Cost: ${costFruit1:.2f}")
print()
print()

print(f"{'  2':7} Item: {fruit2}")
print(f"{' ':7} Quantity: {amount2}")
print(f"{' ':7} Price: ${price2:.2f}")
print(f"{' ':7} Cost: ${costFruit2:.2f}")
print()
print()

print(f"{'  3':7} Item: {fruit3}")
print(f"{' ':7} Quantity: {amount3}")
print(f"{' ':7} Price: ${price3:.2f}")
print(f"{' ':7} Cost: ${costFruit3:.2f}")

print("--------------------")
print(f"Total Cost: ${totalCost:.2f}")
print()


print("*** Display 2")
print()
print(f"{'Receipt':>44}")
print(f"{'-------':>44}")
print()
print(f"{'Item':<9} {'Fruit':<26} {'Quantity':<21} {'Cost':<16} {'Price'}")
print("-----------------------------------------------------------------------------------")
print(f"{'  1':<9} {fruit1:<29} {amount1:<18} ${price1:<15.2f} ${costFruit1:>6.2f}")
print(f"{'  2':<9} {fruit2:<29} {amount2:<18} ${price2:<15.2f} ${costFruit2:>6.2f}")
print(f"{'  3':<9} {fruit3:<29} {amount3:<18} ${price3:<15.02f} ${costFruit3:>6.2f}")
print(f"{'-------':>83}")
print(f"{'Total':>64} {'$':>12}{totalCost:.2f}")


print("\n")         #*** newlines prior to os message
#*** End execution of the program