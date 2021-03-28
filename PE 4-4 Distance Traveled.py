""" Roger Rues          Student ID: 1000130372
    Program Exercise# 4-4 Distance Traveled Assignment# 3 Uplink
    Due Date: 3/23/21

    Program Description:
        This program will ask the user for a vehicle's speed and hours traveled.
        It will then display the distance traveled for each hour.        
"""

#*** Modules\Libraries
import os                 #*** system() - OS commands

#*** Begin execution of the program
#*** Constants
#*** Variables


os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")
print("This program will ask that you enter a vehicle's speed(mph) and hours traveled.")
print("It will then display the distance traveled for each hour.")
print()


validEntry = False
while not validEntry:
    try:
        vehicleSpeed = float(input("What is the speed of the vehicle in mph? "))
        hoursTraveled = int(input("How many hours has it traveled? "))
        validEntry = True

    except ValueError: 
        print("ERROR: Invalid entry. Please enter a valid numeric value. ")
        print()

#*** Process

print(f"{'Hour':<20} Distance Traveled")
for counter in range(38):
    print("-", end='')
print()


for count in range(1, hoursTraveled + 1):
    distanceTraveled = vehicleSpeed * count
    #*** Report
    print(f"{count:<30} {int(distanceTraveled)}")


print("\n")         #*** newlines prior to OS message
#*** End execution of the program