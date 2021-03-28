#Functions
def main():
    name = input("Enter your name: ")
    age = int(input("How old are you? "))
    greeting(name, age)
    closure(name)

def greeting(name, aint):
    print(f"Hello world, {name}!")
    print(f"I see you are {aint} years old.")

def closure(name):
    print(f"Goodbye, {name}!")


#Execute Functions
main()