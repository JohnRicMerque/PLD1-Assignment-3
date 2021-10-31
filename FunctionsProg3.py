# Program3 using functions

# defining functions
def getMoney():
    moneyAmount = float(input("How much money do you have?: "))
    return moneyAmount

def getAplPrice():
    aplPrice = float(input("Enter the price of one apple: "))
    return aplPrice

def getMaxApples(money, price):
    maxApls = int(money//price)
    return maxApls

def getChange(money, price):
    change = money%price
    return change

# calling functions and storing them in variables
amount_of_money = getMoney()
apple_price = getAplPrice()
max_apples = getMaxApples(amount_of_money, apple_price)
total_change = getChange(amount_of_money, apple_price)

print(f"You can buy {max_apples} apples and your change is {total_change} pesos.")
