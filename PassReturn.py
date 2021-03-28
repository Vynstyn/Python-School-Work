#Functions
def main():
    name = input("Enter your name: ")
    lastname = get_surname(name)
    age = int(input(f"Mr. {lastname}, please enter your age: "))
    greeting(name, age)
    closure(name)

def greeting(name, aint):
    print(f"Hello world, {name}!")
    print(f"I see you are {aint} years old.")

def closure(name):
    print(f"Goodbye, {name}!")

def get_surname(first_name):
    last_name = input(f"{first_name}, what is your last name? ")
    return last_name


#Execute Functions
main()