""" Roger Rues          Student ID: 1000130372
    Program Exercise# 0 Assignment# 0
    Due Date:

    Program Description:
        This program will calculate the average sales of a two week period.
"""
#*** Modules\Libraries
import os                 #*** system() - OS commands

os.system("cls")            #*** Clear Screen - system() - Windows ("cls"), Mac/Linux ("clear")

#Functions
def main():
    description()
    name = get_name()
    week1_sales = get_amount(1)
    week2_sales = get_amount(2)
    totalSales = get_total_sales(week1_sales, week2_sales)
    average = get_average(week1_sales, week2_sales)
    display_results(name, totalSales, average)

def description():
    #*** Display description of the program
    print('This program will calculate the average sales')
    print('for a two week period.\n') #*** display 2 blank lines

def get_name():
    #Get the salesperson's name
    return input("Enter the salesperson's name? ")

def get_amount(week):
    #Get the sales amount
    validEntry = False
    while not validEntry:
        try:
            sales = float(input(f"Enter the sales amount for week {week}? "))
            validEntry = True
            return sales
        except ValueError:
            print("ERROR: Enter a numeric value.")
            print()

def get_total_sales(sales1, sales2):
    #Calculate total sales for both weeks
    return sales1 + sales2

def get_average(sales1, sales2):
    #Calculate the average
    return (sales1 + sales2)/2

def display_results(name, sales, avg):
    #Display the name and average sales
    print(f"\nThe total sales for {name} is ${sales:.2f}.")
    print(f"\nThe average sales for {name} is ${avg:.2f}.")


#Beginning of program execution
main()

print("\n")         #*** newlines prior to OS message
#*** End execution of the program