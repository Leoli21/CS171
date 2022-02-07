#Program: CS 171 - How efficient is your car?
#Purpose: Calculates the fuel efficiency (in miles per gallon) of an automobile given speed of car,
#         distance traveled, and the cost of gasoline.
#Author: Leo Li
#Date: Jan 10, 2022

# import necessary modules
import math

# Define Function
def fuelEfficiency(speed):
    fuelEfficiency = 71.7 * speed * math.pow(2 + 0.0192 * speed, -4.5) + math.exp(-5.1*speed) - 1
    return fuelEfficiency

if __name__ == "__main__" :
    avgSpeed = float(input("Enter the average speed driven (in miles per hour): "))
    distTraveled = float(input("Enter the distance traveled (in miles): "))
    costOfGasoline = float(input("Enter the cost of gasoline (in dollars per gallon): "))
    
    fuelEff = fuelEfficiency(avgSpeed)
    totalGallons = (1 / fuelEff) * distTraveled
    totalCost = totalGallons * costOfGasoline
    print("The fuel efficiency of your vehicle is", round(fuelEff, 2), "miles per gallon.")
    print(round(totalGallons,2), "gallons of gasoline were consumed during this trip.")
    print("The total cost of the consumed gasoline was", round(totalCost, 2), "dollars.")