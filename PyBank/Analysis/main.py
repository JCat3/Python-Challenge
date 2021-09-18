# import os module  and module for reading csv file
import os
import csv

# path to collect data from resources folder
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#month counter
total_months = 0
total_profit = 0
profit_change = []
date = []
revenue = []

# Read CSV module
with open(budget_csv) as csv_file:

    # add CSV reader
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip headers
    csv_header = next(csv_file)

    for row in csv_reader:
         # loop through looking for Date
        date.append(row[0])
        revenue.append(int(row[1]))
        
        #count months
        total_months += 1

# loop through revenue list - out of range with + 1, need to end loop one early
for i in range(len(revenue)-1):
   
    profit_change.append(revenue[i + 1] - revenue[i])

# print(profit_change)
# print(len(profit_change))

# average profit change
avg_profit_change = sum(profit_change) / (len(profit_change))

# max and min change
max_profit_change = max(profit_change)
min_profit_change = min(profit_change)  

# total profit/losses
total_profit = sum(revenue)

#max & min month
max_profit_month = date[profit_change.index(max_profit_change) +1]
min_profit_month = date[profit_change.index(min_profit_change) +1]
 
    
# print months
print(f"Financial Analysis")
print(f"------------------------------")
print(f"Total Months: {total_months}")        
print(f"Total: {total_profit}")
print(f"Average Change: {avg_profit_change:.2f}")
print(f"Greatest Increase in Profits: {max_profit_month} {max_profit_change}")
print(f"Greatest Decrease in Profits: {min_profit_month} {min_profit_change}")

# output CSV
output_path = os.path.join("..", "Analysis", "Financial_Analysis.txt" )

with open(output_path, 'w', newline="") as file:

# write in text file
    file.write("Financial Analysis")
    file.write("\n")
    file.write(f"------------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")        
    file.write(f"Total: {total_profit}")
    file.write("\n")
    file.write(f"Average Change: {avg_profit_change:.2f}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_profit_month} {max_profit_change}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_profit_month} {min_profit_change}")