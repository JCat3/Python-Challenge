# import os module  and module for reading csv file
import os
import csv

# path to collect data from resources folder
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#month counter
total_months = 0


# Read CSV module
with open(budget_csv) as csv_file:

    # add CSV reader
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip headers
    csv_header = next(csv_file)

    for row in csv_reader:
        
        #count months
        total_months = total_months + 1

        print (total_months)

    # loop through looking for Date
        date = row[0]
        profit_losses = row[1]

        
        # for budget_csv in 