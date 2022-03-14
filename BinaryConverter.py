#Program: BinaryConverter.py
#Purpose: To convert a user-inputted positive integer number to binary using
#         recursion and returning it as a string.
#Author: Leo Li
#Date: Feb 28, 2022

# YOUR FUNCTION DEFINITION HERE
'''
    Purpose of Function: asks user to enter a positive integer value,
    or zero to end the program and validates their input.
    @param: None
    @return: Returns user's validated positive integer value or zero
'''
def getValidInteger():
    while True:
        try:
            num = int(input("Enter a positive integer or 0 to end: "))
            if num >= 0:
                return num
            else:
                print("Error: you entered a negative value. Try again")
                
        except:
            print("Error: An integer value was expected. Try again")
            
            
            
'''
    Purpose of Function: Take a positive integer number in decimal and
    converts it to binary through recursion
    
    @param:
    number: an integer representing the user's validated positive integer
            value. This value gets converted to binary.
            
    @return: a string representing the parameter's binary representation
'''
def decimalToBinary(number):
    #Base Case 
    if number == 0:
        return ''
        
    #Recursive Case
    else:
        remainder = number % 2
        number = number // 2
        return decimalToBinary(number) + str(remainder)
    

# The main routine here, after this line
if __name__ == "__main__" :
    number = getValidInteger()
    
    #Continue to convert user entered decimal number to binary until user enters 0
    while number > 0:
        print("The equivalent of", number, "in Binary is", decimalToBinary(number))
        number = getValidInteger()
        
        
