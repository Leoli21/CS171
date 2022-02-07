#Program: Precipitation Stats
#Purpose: To calculate and display the total precipitation for the year, the
#         average monthly precipitation, and the months with the highest and lowest
#         precipitation amounts. Precipitation is measured in inches. 
#Author: Leo Li
#Date: Jan 18, 2022

#Creating Lists
monthly_precipitation = []
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
               'September', 'October', 'November', 'December']
               
#Getting User Input 
monthly_precipitation.append(float(input("Enter total precipitation for January: ")))
monthly_precipitation.append(float(input("Enter total precipitation for February: ")))
monthly_precipitation.append(float(input("Enter total precipitation for March: ")))
monthly_precipitation.append(float(input("Enter total precipitation for April: ")))
monthly_precipitation.append(float(input("Enter total precipitation for May: ")))
monthly_precipitation.append(float(input("Enter total precipitation for June: ")))
monthly_precipitation.append(float(input("Enter total precipitation for July: ")))
monthly_precipitation.append(float(input("Enter total precipitation for August: ")))
monthly_precipitation.append(float(input("Enter total precipitation for September: ")))
monthly_precipitation.append(float(input("Enter total precipitation for October: ")))
monthly_precipitation.append(float(input("Enter total precipitation for November: ")))
monthly_precipitation.append(float(input("Enter total precipitation for December: ")))

#Calculating Total Precipitation, Average Precipitation
total_precipitation = sum(monthly_precipitation)
avg_precipitation = total_precipitation / len(monthly_precipitation)

#Identifying Highest/Lowest Precipitation 
lowest_precipitation = min(monthly_precipitation)
highest_precipitation = max(monthly_precipitation) 
lowest_month = month_names[monthly_precipitation.index(lowest_precipitation)]
highest_month = month_names[monthly_precipitation.index(highest_precipitation)]

#Dispalying Precipitation Statistics
print(f"Total precipitation: {total_precipitation:.2f}")
print(f"Average precipitation: {avg_precipitation:.2f}")
print(f"{highest_month:s} has the highest precipitation: {highest_precipitation:.2f}")
print(f"{lowest_month:s} has the lowest precipitation: {lowest_precipitation:.2f}")