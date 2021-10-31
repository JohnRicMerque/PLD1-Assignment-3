# Program1 using functions

# function list
def askName():
    _name = input("Enter name: ")
    return _name

def askAge():
    _age = input("Enter age: ")
    return _age

def askAddress():
    _address = input("Enter Address: ")
    return _address

def display(nameF, ageF, addressF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF}.")

# program start
# 1. ask for name then store to a variable
name = askName()
# 2. ask for age then store to a variable
age = askAge()
# 3. ask for address then store to a variable
address = askAddress()
# 4. display the details
display(name, age, address)
