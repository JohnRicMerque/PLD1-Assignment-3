# Program2 using functions

# defining functions
def getApls():
    nOfApls = int(input("Enter the number of apples you want to buy: "))
    return nOfApls

def getOrgs():
    nOfOrgs = int(input("Enter the number of oranges you want to buy: "))
    return nOfOrgs

def getPrice(apl_number, org_number):
    apl_price = apl_number * 20
    org_price = org_number * 25
    total = apl_price + org_price
    return total

# calling functions and storing in variables
applesN = getApls()
orangesN = getOrgs()
totalPrice = getPrice(applesN, orangesN)

print(f"The total amount is {totalPrice}.")
