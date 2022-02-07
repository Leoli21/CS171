#Program: Phone Number Converter
#Purpose: To convert a 10-character phone number in the format XXX-XXX-XXXX into its numeric equivalent. Then to 
#         display it.
#Author: Leo Li
#Date: Jan 18, 2022

#Creating Dictionary for letters and numeric equivalents
letter_to_number = { 
    'A': '2', 'B': '2', 'C': '2', \
    'D': '3', 'E': '3', 'F': '3', \
    'G': '4', 'H': '4', 'I': '4', \
    'J': '5', 'K': '5', 'L': '5', \
    'M': '6', 'N': '6', 'O': '6', \
    'P': '7', 'Q': '7', 'R': '7', 'S': '7', \
    'T': '8', 'U': '8', 'V': '8', \
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    
print("Phone Number Translator")
    
#Asking for Phone Number
phone_number = input("Enter a phone number in the format XXX-XXX-XXXX: ")
    
#Declaring String that will store the converted numeric phone number 
converted_string = ""

#Concatenating first 3 digits of the phone number to converted string using string splicing
#Also, adding '-' after first 3 digits to preserve phone number format.
converted_string = converted_string + phone_number[0:3]
converted_string = converted_string + "-"

#Concatenating next 3 digits of the phone number to string and converting digit to numeric equivalent
#if needed. Also adding '-' after 3 digits to preserve phone number format.
converted_string = converted_string + (letter_to_number.get(phone_number[4], phone_number[4]))
converted_string = converted_string + (letter_to_number.get(phone_number[5], phone_number[5]))
converted_string = converted_string + (letter_to_number.get(phone_number[6], phone_number[6]))
converted_string = converted_string + "-"

#Concatenating last 4 digits of the phone number to string and converting digit to numeric equivalent
#if needed. 
converted_string = converted_string + (letter_to_number.get(phone_number[8], phone_number[8]))
converted_string = converted_string + (letter_to_number.get(phone_number[9], phone_number[9]))
converted_string = converted_string + (letter_to_number.get(phone_number[10], phone_number[10]))
converted_string = converted_string + (letter_to_number.get(phone_number[11], phone_number[11]))

#Printing the converted numeric phone number to dial
print("Dial:", converted_string)

    
    
