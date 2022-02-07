#Program: DoublingEarnings.py
#Purpose: Display a table showing earnings for each day (in dollar amount) when your
#         salary earnings double each day. The total pay accrued by the end of the user
#         specified period is also displayed.
#Author: Leo Li
#Date: 1 February 2022


# data input and validation - YOU MUST USE LOOPS AND TRY/EXCEPT
validInput = False
while not(validInput):
    try:
        numDays = int(input("Enter the number of days: "))
        if(numDays <= 0):
            print("Error: you must enter a number greater than zero. Try again.")
            numDays = int(input("Enter the number of days: "))
        else:
            validInput = True
    except Exception as e:
        print("Invalid input. A integer value was expected. Try again.")

# calculate and display the earnings for each day - YOU MUST USE LOOPS
print(f'\n{"Day": <5}{"Pennies": <7}')
totalSalary = 0.0
numPennies = 1;
for i in range(numDays):
    numPennies = numPennies*2
    print(f'{i+1: <5}${numPennies*0.01: <7.2f}')
    totalSalary += numPennies*0.01
# print total earned for the given period of days
print("\nThe total salary for ", numDays, "days is $", totalSalary, sep = "")