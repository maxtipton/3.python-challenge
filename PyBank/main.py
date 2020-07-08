# In this challenge, you are tasked with creating 
# a Python script for analyzing the financial records of your company. 

#Calculate each of the following:

# import modules
import os
import csv

#declare CSV path 
csvpath = os.path.join("/Users/bartholdy9000/Desktop/UPenn Bootcamp/Homework/3. python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

   # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    data = []

    for row in csvreader:
        d={}
        d['month'] = row[0]
        d['net'] = int(row[1])
        data.append(d)

#1. The total number of months included in the dataset
months = []
for d in data: 
    months.append(d['month'])
    
total_months = len(months)
print("Total Months: ", total_months),

#2. The net total amount of "Profit/Losses" over the entire period
net = []
for d in data: 
    net.append(d['net'])
    
total_net = sum(net)
print("Total: $", total_net)

#3. The average of the changes in "Profit/Losses" over the entire period
diffs = []
greatest_net_sofar = 0
least_net_sofar = 0
greatest_month_sofar = ""
least_month_sofar = ""

for index,d in enumerate(data[1:]): 
    previous_net = data[index - 1]['net']
    diff = d['net'] - previous_net
    diffs.append(diff)
    if diff > greatest_net_sofar:
        greatest_net_sofar = diff
        greatest_month_sofar = d["month"]
    if diff < least_net_sofar:
        least_net_sofar = diff
        least_month_sofar = d["month"]

average = sum(diffs) / len(diffs) 
print("Average Change: $", average)

#4. The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: :", greatest_month_sofar, greatest_net_sofar)

#5. The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits: :", least_month_sofar, least_net_sofar)

with open('PyBank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'___________________________', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_net}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {greatest_month_sofar} ({greatest_net_sofar})', file=text_file)
    print(f'Greatest Decrease in Profits: {least_month_sofar} ({least_net_sofar})', file=text_file)

