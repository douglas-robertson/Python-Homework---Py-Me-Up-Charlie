# Main PyBank Code
# Modules
import os
import csv
import sys
import shutil


# Set path for file
budget_csv = os.path.join( "Resources", "budget_data.csv")

#set variables
num_months = 0
total_profit = 0
cprofit_change_pmonth = 0
prior_profit = 867884
prior_profit2 = 0
profit_change_counter = 0
average_of_PL_changes = 0
greatest_increase = 0
greatest_month = "NaN"
greatest_decrease = 0
worst_month = "Nan"
profit = []

# Open and read csv
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

 
  #The total number of months and total profit included in the dataset

    for row in csv_reader:
        num_months += 1
        total_profit += (int(row[1]))

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        profit_change_pmonth = int(row[1]) - prior_profit
        prior_profit = int(row[1])
        profit_change_counter += profit_change_pmonth

        if profit_change_pmonth >= greatest_increase:
                greatest_increase = profit_change_pmonth
                greatest_month = row[0]

        if profit_change_pmonth <= greatest_decrease:
                greatest_decrease = profit_change_pmonth
                worst_month = row[0]


average_of_PL_changes = round((profit_change_counter / num_months),2)

#print sequence

print(f"Financial Analysis")
print("---------------------")
print (f"Total Months:  {num_months}")
print (f"Total: ${total_profit}")
print (f"Average Change: ${average_of_PL_changes}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})")

#export results to txt file

sys.stdout = open("results.txt", "w")

print(f"Financial Analysis")
print("---------------------")
print (f"Total Months:  {num_months}")
print (f"Total: ${total_profit}")
print (f"Average Change: ${average_of_PL_changes}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})")

sys.stdout.close()

shutil.move('/Users/61430/OneDrive/Desktop/Data Analytics/Coursework/03-Python/3-Homework/PyBank/results.txt','C:/Users/61430/OneDrive/Desktop/Data Analytics/Coursework/03-Python/3-Homework/PyBank/Analysis/results.txt')
