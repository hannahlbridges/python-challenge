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

max_num = max(monthly_change)
min_num = min(monthly_change)

max_index = monthly_change.index(max_num) + 1
min_index = monthly_change.index(min_num) + 1


with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    rows = list(csvreader)
    max_row = rows[max_index]
    min_row = rows[min_index]
    print(f'Greatest Increase in Profits: {max_row[0]} (${max_num})')
    print(f'Greatest Decrease in Profits: {min_row[0]} (${min_num})')

with open(analysispath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ' ')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------------------'])
    csvwriter.writerow([f'Total Months: {months}'])
    csvwriter.writerow([f'Total: ${sum(net)}'])
    csvwriter.writerow([f'Average Change: ${round(average_change, 2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {max_row[0]} (${max_num})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {min_row[0]} (${min_num})'])

        



        
    

