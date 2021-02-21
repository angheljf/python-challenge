# Import Modules
import os
import csv

# Set variables
total_months = 0
total_amount = 0
monthly_change =[]
month_count = []
increase = 0
increase_month = 0
decrease = 0
decrease_month = 0

# Set path for file
csvpath = '../git/python-challenge/PyBank/Resources/budget_data.csv'

# Open and Read file
with open (csvpath, newline="") as csvfile:
    # csvreader set variable and delimiter for data
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    row = next(csvreader)
    # Read the header and the first row to check data 
    # print(f"Header: {csvheader}")
    # print(f"Row: {row}")
    previous_row = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    increase = int(row[1])
    increase_month = row[0]

    # Iterate each row after the header
    for row in csvreader:
        
        total_months += 1 # Calculate number of months
        total_amount += int(row[1]) # Calculate Net Amount of Profit/Loss
        # Month to month change
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        if int(row[1]) > increase:
            increase = int(row[1])
            increase_month = row[0]
        if int(row[1]) < decrease:
            decrease = int(row[1])
            decrease_month = row[0]
    average = sum(monthly_change) / len(monthly_change)
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits:, {increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {decrease_month}, (${lowest})") 

# Specify File To Write To
output_file = '../git/python-challenge/PyBank/Analysis/budget_analysis.txt'

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_amount}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(f"Greatest Increase in Profits:, {increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {decrease_month}, (${lowest})\n")
    