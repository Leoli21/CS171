#Program: CountingLetters.py
#Purpose: Counting the occurence of each letter in a user-inputted sentence
#Author: Leo Li
#Date: 31 January 2022

#Getting user input
sentence = input("Enter a sentence: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Counting occurenes of each letter
for letter in alphabet:
    occurences = sentence.count(letter)
    if(occurences > 0):
        print(letter + ": " + str(occurences) + " times")
    
     
    
    
