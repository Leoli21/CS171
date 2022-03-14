#Program: SecretMessage.py
#Purpose: To help Professor X automate grade calculation for a course
#         through reading data from a file. Then, saving the data results
#         by writing it to an output file. 
#Author: Leo Li
#Date: Feb 21, 2022

import os
# DEFINE YOUR FUNCIONS HERE AND FOR EACH FUNCION INCLUDE A DOCSTRING DOCUMENTING THE FUNCTION
def validateUserChoice():
    """
    Purpose of Function:
    To prompt user for whether they want to encode or decode a message and
    validating that they gave a choice that is part of the menu ('e' or 'E'
    to choose encode or 'd' or 'D' to choose to decode)
    
    @param: none
    
    @return: 
    Returns a character that stores the validated user input ('E' for encode or 'D' for decode) 
    """
    validInput = False
    while(not validInput):
        userChoice = input("Enter your choice: ").upper()
        if(userChoice == 'E' or userChoice == 'D'):
            validInput = True
        else:
            print("Error: You must enter E or D")
    return userChoice

def getFileName(prompt):
    """
    Purpose of Function:
    To prompt the user for the name of the file that contains either
    the encryption key (output file) or the file that contains the
    message to be decoded (input file). This file will then be checked
    to see if it exists and can be opened.
    
    @param: 
    prompt -- a string containing the prompt that the user will have
              to answer regarding the name of the file that has either
              the code or the message to decode
    
    @return: 
    Returns the name of the validated file
    """
    while True:
        fileName = input(prompt)
        if os.path.exists(fileName):
            return fileName
        print("Error: that file does not exist")


def encode(originalMsg, code):
    """
    Purpose of Function:
    Performs the encryption of the text entered by the user using
    the encryption key and then saves the encoded message in the
    secret.txt file.
    
    @param: 
    originalMsg -- a string containing the original text entered by
                   the user
    
    code -- a string that represents the name of the file that contains
            the secret encryption key
    
    @return: none
    """
    cwd = os.getcwd()
    encryptionKeyFile = open(code, "r")
    encodedMessageFile = open("secret.txt", "w")
    encodedMsgList = []
    encodedMsg = ""
    stdAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    key = encryptionKeyFile.read()
 
    words = originalMsg.split()
    for word in words:
        encodedWord = ""
        for letter in word:
            if letter.isalpha():
                index = stdAlpha.index(letter)
                encodedLetter = key[index]
                encodedWord = encodedWord + encodedLetter
            else:
                encodedWord = encodedWord + letter
        encodedMsgList.append(encodedWord)
        
    encodedMsg = " ".join(encodedMsgList)
    print("\nEncoded message:", encodedMsg)
    encodedMessageFile.write(encodedMsg)
    print("Encoded message has been saved in secret.txt")
    
    encryptionKeyFile.close()
    encodedMessageFile.close()
    
def decode(codedMsg, code):
    """
    Purpose of Function:
    To decrypt the message in the 'codedMsg' file using the 'code' file
    which contains the encryption key. The decoded message will then be
    displayed.
    
    @param: 
    codedMsg -- a string that represents the name of the file that contains
                the message to be decoded
    code -- a string that represents the name of the file that contains the
            encryption key
            
    @return: none
    """
    encryptionKeyFile = open(code, "r")
    encodedMsgFile = open(codedMsg, "r")
    decodedMsgList = []
    decodedMsg = ""
    
    stdAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encodedMsg = encodedMsgFile.read()
    key = encryptionKeyFile.read()
    

    words = encodedMsg.split()
    for word in words:
        decryptedWord = ""
        for character in word:
            if character.isalpha():
                letterIndex = key.index(character)
                decryptedWord = decryptedWord + stdAlpha[letterIndex]
            else:
                decryptedWord = decryptedWord + character
        decodedMsgList.append(decryptedWord)
            
    decodedMsg = " ".join(decodedMsgList)
    print("\nEncoded message:", encodedMsg)
    print("Decoded message:", decodedMsg)
    
    encryptionKeyFile.close()
    encodedMsgFile.close()


# the main routine goes here after the following line
if __name__ == "__main__" :
    print("Enter E to encode a message.")
    print("Enter D to decode a message.")
    userChoice = validateUserChoice()
    if(userChoice == "D"):
        decodePrompt1 = "Enter name of the file that has the code: "
        code = getFileName(decodePrompt1)
        
        decodePrompt2 = "Enter name of the file that has the message to decode: "
        codedMsg = getFileName(decodePrompt2)
        
        decodedMsg = decode(codedMsg, code)
        
    else:
        encodePrompt1 = "Enter name of the file that has the code: "
        code = getFileName(encodePrompt1)
        
        originalMsg = input("Enter the message you want to encode: ")
        
        encode(originalMsg, code)
    



