#Program: VendingMachine.py
#Purpose: To simulate a vending machine by displaying a menu and simulating a transaction
#Author: Leo Li
#Date: Jan 29, 2022

# Display Menu
vendingMachineNames = {
    '1' : 'Roasted Almonds',
    '2' : 'Pretzels',
    '3' : 'Chewing Gum',
    '4' : 'Mints',
    '5' : 'Chocolate bar',
    '6' : 'Cookies'
}
vendingMachineCost = {
    '1' : 1.25,
    '2' : 1.75,
    '3' : 0.90,
    '4' : 0.75,
    '5' : 1.50,
    '6' : 2.00
}

print("Vending Machine\n")
print(f'{"1. Roasted Almonds": <20}{"-->":<4}{"$1.25"}')
print(f'{"2. Pretzels": <20}{"-->":<4}{"$1.75"}')
print(f'{"3. Chewing Gum": <20}{"-->":<4}{"$0.90"}')
print(f'{"4. Mints": <20}{"-->":<4}{"$0.75"}')
print(f'{"5. Chocolate bar": <20}{"-->":<4}{"$1.50"}')
print(f'{"6. Cookies": <20}{"-->":<4}{"$2.00"}\n')

# Get and validate user input:
validData = True
#    * valid menu choices: 1 - 6 (int)
try:
    itemChoice = int(input("Enter your choice of item: "))
except:
    print("Value entered was not a number.")
    validData = False
if validData and (itemChoice < 0 or itemChoice > 6):
    print("Invalid item choice.")
    validData = False
    
#    * if user enter a valid menu item then read in money amount (float)
if validData:
    try: 
        money = double(input("Enter money to purchase item:" ))
    except:
        print("Value entered was not a number.")
        validData = False
    #    * money amount must be greater or equal to zero
    if validData and (money < 0.0):
        print("Amount of moeny cannot be a negative value.")
        if(money < vendingMachineCost[str(itemChoice)]):
            deficit = vendingMachineCost[str(itemChoice)] - money
            print("You are $" + deficit + " short.")

# If all data is valid, then calculate change and display appropriate message
if (validData):
    change = money - vendingMachineCost[str(itemChoice)]
    print("Thanks for buying", vendingMachineName[str(itemChoice)])
    print(f'Your change is {change:.2f}')

