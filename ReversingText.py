#Program: ReversingText.py
#Purpose: To display a user entered string in reverse
#Author: Leo Li
#Date: Feb 28, 2022

# YOUR FUNCTION DEFINITION HERE
'''
    Purpose of Function: To take a string and reverse the characters in
    the string and return it, using recursion
    
    @param:
    string: a string representing the user inputted string to be reversed
            
    @return: a string representing the result of the original string's
    characters being reversed
'''
def reverseString(string):
    #Base Case
    if len(string) == 0:
        return string
    
    #Recursive Case
    else:
        sliceString = string[1:len(string)]
        return reverseString(sliceString) + string[0]

# The main routine here, after this line
if __name__ == "__main__" :
    userString = input("Enter a string you wish to reverse: ")
    print("Here is the reversed string:", reverseString(userString))
