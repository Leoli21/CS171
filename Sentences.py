#Program: Sentence Response
#Purpose: To respond to a user-inputted sentence given certain specified circumstances.
#Author: Leo Li
#Date: Jan 29, 2022

#Define functions here
def evenCharacters(myString):
    if(len(myString) % 2 == 0):
        return True
    else:
        return False

if __name__=="__main__":
    # read a sentence from the user
    sentence = input("Enter a sentence: ")

    # decide what to output
    if(sentence.endswith('?')):
        if(evenCharacters(sentence)):
            print("Yes")
        else:
            print("No")
    elif(sentence.endswith('!')):
        print("Wow")
    else:
        print("You always say \"" + sentence + "\"")
    
