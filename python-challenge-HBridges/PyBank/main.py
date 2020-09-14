import os
import csv

recordspath = 'Resources/budget_data.csv'
print('Financial Analysis')
print('-----------------------------------------')

net = []

with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        net.append(int(row[1]))

    months = len(net)
    print(f'Total Months: {months}')
    print(f'Total: ${sum(net)}')
    print(f'Average Change: ${round(sum(net)/len(net), 2)}')

max_num = max(net)
min_num = min(net)

with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)

    for row in csvreader:
        if int(row[1]) == max_num: 
            print(f'Greatest Increase in Profits: {row[0]} (${row[1]})')
        if int(row[1]) == min_num:
            print(f'Greatest Decrease in Profits: {row[0]} (${row[1]})')

analysispath = 'Analysis/Analysis.txt'
with open(analysispath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ' ')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------------------'])
    csvwriter.writerow([f'Total Months: {months}'])
    csvwriter.writerow([f'Total: ${sum(net)}'])
    csvwriter.writerow([f'Average Change: ${round(sum(net)/len(net), 2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {row[0]} (${row[1]})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {row[0]} (${row[1]})'])

        



        
    

