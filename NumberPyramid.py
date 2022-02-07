#Program: NumberPyramid.py
#Purpose: Displaying Pyramid of numbers given user-specified number of lines 
#Author: Leo Li
#Date: 31 January 2022

#Getting User Input and
#Validating user inputted an Integer between 1 and 9
invalidValue = True
while invalidValue:
    try:
        numLines = int(input("Enter the number of lines (1 - 9): "))
        if(numLines < 1 or numLines > 9):
            print("Error: you must enter a value between 1 and 9. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. A integer value was expected. Try again.")

numList = []
for i in range(0, numLines):
    numList.append(i+1)
reversedNumList = numList[::-1]

numSpaces = numLines - 1
print("\n")
for i in range(numLines):
    for j in range(i, numSpaces):
        print(" ", end = "")
    for j in range(i):
        print(reversedNumList[j-(i+1)], end = "")
    for j in range(i+1):
        print(numList[j], end = "")
    print()

