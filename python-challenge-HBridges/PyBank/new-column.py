import os
import csv

recordspath = 'Resources/budget_data.csv'
analysispath = 'Analysis/Analysis.txt'

print('Financial Analysis')
print('-----------------------------------------')

net = []

with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        net.append(int(row[1]))

with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    last_month = 0
    monthly_change = []
    for profit in csvreader:
        if last_month == 0:
            last_month = int(profit[1])
        else:
            monthly_change.append(int(profit[1]) - last_month)
            last_month = int(profit[1])

total_change = sum(monthly_change)
average_change = total_change / len(monthly_change)

months = len(net)
print(f'Total Months: {months}')
print(f'Total: ${sum(net)}')
print(f'Average Change: ${round(average_change, 2)}')

monthly_change.append(0, 0)
monthly_change.append(0, 'Monthly Change')

