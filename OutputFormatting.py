""" Roger Rues          Student ID: 1000130372
    Program Exercise# 0 Assignment# 0
    Due Date:

    Program Description:
        Develop a program that will display contents of variables in various formats.
        Declare variables
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Variables
num = -5
num2 = 120.55
char = "M"
name = "Miami"


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")
"""
print("*** Display 1")
print("Values = ", num, ", ", num2, ", ", char, ", ", name, sep = '')
print("Values = ", name, " - ", num, " - ", num2, " - ", char, sep = '')


print("*** Display 2")
print(f"{'Integer':10}#1: {num}")
print(f"{'Float':10}#2: {num2}")
print(f"{'Character':10}#3: {char}")
print(f"{'String':10}#4: {name}")
"""

print("*** Display 3")
print("Values")
print("======")
print(f"{'1.':3} {num}")
print(f"{'2.':3} ${num2}")
print(f"""{'3.':3} '{char}'""")
print(f'''{'4.':3} "{name}"''')


print("\n")         #*** newlines prior to os message
#*** End execution of the program