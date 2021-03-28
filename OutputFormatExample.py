""" Roger Rues          Student ID: 1000130372
    Program Exercise# 0 Assignment# 0
    Due Date:

    Program Description:
        This program demonstrates the varius print statements.
"""

#*** Modules\Libraries
import os                 #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Begin execution of the program

os.system("cls")            #*** clear screen

"""

Program description:

    Demonstrates the various print statemts



Data:

    item = Orange

    weight = .3456

    quantity = 20

    cost = .99

"""



item = "Orange"

weight = .3456

quantity = 20

cost = .30



print("1 - Oranges, .3456, 20, .99")



print("2 - ", item, weight, quantity, cost)



print("3a -", format(item, 's'))

print("3b -", format(weight,'f'))

print("3c -", format(quantity, 'd'))

print("3d -", format(cost, 'f'))



print("4 -", format(item, 's'), format(weight,'f'),format(quantity, 'd'), format(cost, 'f'))



print("5 - {3}   {2}   {1}  {0}".format(item, weight,  quantity, cost))



print(f"6 - {item:s} {weight:f} {quantity:d} {cost:f}") 



print("\n")         #*** newlines prior to os message
#*** End execution of the program