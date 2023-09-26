

#Coffee Shop program
#price of one cup = 1.85
#tax rate --> 0.15
#The math --> price of a cup * price of 1 cup * tax rate --> how much tax is charged
#       --> price of 1 cup + tax amount

price = 2
taxRate = 0.15

print("Welcome to Geoff's Coffee Shop!")
print("Click the (imaginary) button below to get your coffee.")

#The math
numofCups = int(input("how many cups do you want to buy today?"))
TaxAmount = (price * int(numofCups)) * taxRate
finalTotal = (price * int(numofCups)) + TaxAmount
finalTotal = round(finalTotal, 2)
print("Thanks for your order! Your total is ${0: .2f}".format (finalTotal))

