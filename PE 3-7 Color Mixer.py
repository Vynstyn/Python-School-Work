""" Roger Rues          Student ID: 1000130372
    Program Exercise# 3-7 Color Mixer Assignment# 0
    Due Date:

    Program Description:
        This program gets two colors from the user and mixes them to display a third color.
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
#*** Variables


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#*** Process

print ("This program asks for two primary colors and displays a mixed color. ")
print()

color1 = input('Enter primary color: ')
color2 = input('Enter primary color: ')
print()



flag1 = False
flag2 = False

if color1 == 'red' or color1 == 'blue' or color1 == 'yellow':
    flag1 = True
    
if color2 == 'red' or color2 == 'blue' or color2 == 'yellow':
    flag2 = True
    
if flag1 == False or flag2 == False:
    print("You didn't input two primary colors.")
else:
    if (color1 == 'red' or color1 == 'blue') and (color2 == 'red' or color2 == 'blue'):
        color3 = 'purple'
        print(f"When you mix {color1} and {color2}, you get {color3}.")
    elif (color1 == 'red' or color1 == 'yellow') and (color2 == 'red' or color2 == 'yellow'):
        color3 = 'orange'
        print(f"When you mix {color1} and {color2}, you get {color3}.")
    elif (color1 == 'blue' or color1 == 'yellow') and (color2 == 'blue' or color2 == 'yellow'):
        color3 = 'green'
        print(f"When you mix {color1} and {color2}, you get {color3}.")
    
    

#*** Report




print("\n")         #*** newlines prior to OS message
#*** End execution of the program