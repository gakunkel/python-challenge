#!/usr/bin/env python
# coding: utf-8

# In[3]:


# script for PyBank

import csv
import os

budget_input = os.path.join("budget_data.csv")
budget_output = os.path.join("budget_analysis.txt")

# data to keep report on/keep track of: months, net profit/loss, change in profit/loss, greatest profit increase & loss decrease
total_months = 0
month_for_change = []
list_net_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000000000000]
total_net = 0

# csv ---> [list of {dictionaries}]
with open(budget_input) as money_data:
    reader = csv.reader(money_data)
    
    # to check current header
    header = next(reader)
    
    
    # test using first row of data
    first_row = next(reader)
    total_months += 1
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    
    # repeat for rest of data using loop
    for row in reader:
        
        # accumulate totals
        total_months += 1
        total_net += int(row[1])
        
        # follow net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        list_net_change += [net_change]
       
        
        month_for_change += [row[0]]
        
        
        if net_change > greatest_increase[1]:
            greatest_increase[0]  = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
    # to get average net change
    net_monthly_avg = sum(list_net_change) / len(list_net_change)
    output = (
        f"\nBudget Analysis\n"
        f"--------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${net_monthly_avg:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    print(output)
    
with open(budget_output, "w") as txt_file:
    txt_file.write(output)





