#Program: BACModel.py
#Purpose: Getting user's weight, biological sex and time since last drink, and then printing
#         out a table of information showing the user's status according to their BAC for each
#         proceeding drink
#Author: Leo Li
#Date: 14 February 2022

# YOUR FUNCTIONS DEFINITIONS HERE, INCLUDING DOCUMENTATION USING DOCSTRINGS. SEE EXAMPLE BELOW:
'''
    Purpose of Function: 
    @param: name and purpose of each parameter, if any
    @return: return value, if any
'''
def promptForInteger(lower, upper):
    """
    Purpose of Function: 
    To prompt user for their weight (as an integer), and duration (minutes since
    last drink - as an integer). These input values are validated and returned through this function.
    This function repeatedly asks the user for an integer until they enter one within the
    specified range (lower, upper).
    
    @param: 
    lower -- lower bound (inclusive) for range of integers that user can enter
    upper -- upper bound (inclusive) for range of integers that user can enter
    
    @return:
    Returns a validated integer input from the user
    """
    validInput = False
    while(not validInput):
        try:
            userInteger = int(input())
            if(userInteger < lower) or (userInteger > upper):
                print("Error: value out of bounds")
            else:
                validInput = True
        except:
            print("Error: An integer value was expected. Try again")
            
    return userInteger
    
def promptForMorF():
    """
    Purpose of Function:
    To prompt for user's biological sex and to validate that the user correctly inputs either 
    a 'M' for male or a 'F' for female.
    
    @param: 
    None
    
    @return: 
    Returns a character that stores the validated user input ('M' for male or 'F' for female) 
    """
    validInput = False
    while(not validInput):
        userSex = input().upper()
        if(userSex == 'M' or userSex == 'F'):
            validInput = True
        else:
            print("Error: You must enter M or F")
    return userSex

def computeBloodAlcoholConcentration(drinks, weight, duration):
    """
    Purpose of Function:
    Computes the blood alchol concentration (BAC), based upon the number of drinks,
    weight, and duration. Formula for BAC is the number of drinks divided by the
    person's weight and then multipled by the male constant (3.8) or the female 
    constant (4.5). This BAC value then decreases by 0.1 for each 40 minutes since 
    the user's last drink.
    
    @param:
    drinks -- integer value for number of drinks user drank
    weight -- integer value for user's weight
    duration -- integer value for minutes since the user's last drink
    
    @return:
    Returns both male and female BAC as a list
    """
    #Calculating male and female BAC using given formula: 
    # (number of drinks / person's weight) * male or female constant - (0.01 for each 40 minutes after the last drink)
    male_bac = (drinks/weight) * 3.8 - (0.01 * (duration / 40))
    female_bac = (drinks/weight) *  4.5 - (0.01 * (duration /40))
    
    #Cannot have negative BAC. Sets both male and female BAC to 0 if value is negative.
    if male_bac < 0:
        male_bac = 0
        
    if female_bac < 0:
        female_bac = 0
    
    #Returning both male and female BACs in form of a list 
    return [male_bac, female_bac]

def impairment(bac):
    """ 
    Purpose of Function:
    To identify correct message to return according to user's current blood alcohol concentration (BAC)
    
    @param:
    bac -- the user's BAC value
    
    @return:
    Returns a string with the appropriate message for the BAC value
    """
    if(bac == 0.00):
        return "Safe to Drive"
    elif(bac > 0.00 and bac < 0.04):
        return "Some Impairment"
    elif(bac >= 0.04 and bac < 0.08):
        return "Driving Skills Significantly Affected"
    elif(bac >= 0.08 and bac < 0.10):
        return "Criminal Penalties in Most US States"
    elif(bac >= 0.10 and bac < 0.30):
        return "Legally Intoxicated - Criminal Penalties in All US States"
    else:
        return "Death is Possible!"
        
    
def showImpairmentChart(weight, duration, sex):
    """
    Purpose of Function:
    To display an impairment chart that displays the drink number, the 
    corresponding BAC value for each drink (using computeBloodAlcoholConcentration(drinks, weight, duration), 
    and the appropriate message for the BAC using impairment(bac) function.
    
    @param:
    weight -- integer representing user's weight, used in calculating BAC value
    duration -- integer representing minutes after user's last drink, used in calculating BAC value
    sex -- a character ('M' or 'F') representing user's biological sex, used to get the correct BAC value of user
    
    @return:
    No return value, only contains print statements.
    """
    #Male Impairment Chart
    if(sex == 'M'):
        print(str(weight) + " pounds, male, " + str(duration) + " minute(s) since last drink")
        print(f'{"#drinks":<10}{"BAC":<10}{"Status":<}')
        for i in range(0, 12):
            male_bac = computeBloodAlcoholConcentration(i,weight,duration)[0]
            print(f'{i:<10}{male_bac:<10.4f}{impairment(male_bac):<}')
    
    #Female Impairment Chart
    else:
        print(str(weight) + " pounds, female, " + str(duration) + " minute(s) since last drink")
        print(f'{"#drinks":<10}{"BAC":<10}{"Status":<}')
        for i in range(0, 12):
            female_bac = computeBloodAlcoholConcentration(i, weight, duration)[1]
            print(f'{i:<10}{female_bac:<10.4f}{impairment(female_bac):<}')

#driver to call and organize all other functions
if __name__ == '__main__':
    print('Enter your weight (in lbs): ')
    weight = promptForInteger(0, 500)
    print('How many minutes has it been since your last drink? ')
    duration = promptForInteger(0, 300)
    print('Enter your sex as M or F: ')
    sex = promptForMorF()
    showImpairmentChart(weight, duration, sex)

