#Program: GradeStats.py
#Purpose: To help Professor X automate grade calculation for a course
#         through reading data from a file. Then, saving the data results
#         by writing it to an output file. 
#Author: Leo Li
#Date: Feb 21, 2022

import os

#Validation: Making sure user inputs a file name that
#            can be found and be open
def getFileName(prompt):
    while True:
        fileName = input(prompt)
        if os.path.exists(fileName):
            return fileName
        print("Error: that file does not exist. Try again.")

#Calculate the totalScore, numberOfTests, and testAverage for each student 
#and return these values as a list        
def studentAnalysis(line):
    studentData = line.split()
    totalScore = 0
    numberOfTests = 0
    for score in range(1, len(studentData)):
        totalScore += int(studentData[score])
        numberOfTests += 1
    testAverage = totalScore/numberOfTests
    testAvgFormat = "{0:.2f}".format(testAverage)
    return [studentData[0], str(totalScore), str(numberOfTests), testAvgFormat]

#Opening the data file and calculating the total of each student's test scores
#tests taken, and their average for the tests. Creating and writing to an output
#file contains the data for each student.
def calcGradeStats(fileName):
    
    #Open data file and creating new file that will contain all the new data
    file = open(fileName, "r")
    outputFile = open("stats.txt", "w")
    
    #Process each line of the file, and write new line in output file
    for line in file:
        calcData = studentAnalysis(line)
        writeString = " ".join(calcData)
        outputFile.write(writeString + "\n")
    
    #Close both files
    file.close()
    outputFile.close()

if __name__ == "__main__":
    prompt = "Enter name of the data file:"
    fileName = getFileName(prompt)
    calcGradeStats(fileName)
    print("Stats have been save in the output file")
    
        
    

