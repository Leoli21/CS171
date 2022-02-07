#Program: CS 171 - Pizza For Everyone!
#Purpose: Calculates number of slices a pizza can yield and number of pizzas a customer needs to order for his/her
#         party.
#Author: Leo Li
#Date: Jan 10, 2022

# import necessary modules
import math

# define function

#slicePerPizza returns the total number of pizza slices a pizza of given diameter will yield
def slicesPerPizza(diameter):
    sliceArea = 14.125
    pizzaRadius = diameter/2.0
    pizzaArea = math.pi * math.pow(pizzaRadius,2.0)
    return math.floor(pizzaArea/sliceArea)

if __name__=="__main__":
    print("Welcome to Mario and Luigi's Pizzeria")
    # get data from the user
    diameter = int(input("Enter the diameter of the pizzas you want to order (in inches): "))
    totalPeople = int(input("Enter the number of people in your party: "))
    
    # declare other values needed for the calculations
    totalSlices = totalPeople * 3
    
    # calculations
    slicesPerPizza = slicesPerPizza(diameter)
    totalPizzas = math.ceil(totalSlices / slicesPerPizza)
    
    # display results
    print("For a party of", totalPeople, "people you need to order", totalPizzas, "pizza(s).")
    print("A", diameter, "inch pizza will yield", slicesPerPizza, "slices.")
