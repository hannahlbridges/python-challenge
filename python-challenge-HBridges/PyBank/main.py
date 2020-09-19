import os
import csv

recordspath = 'Resources/budget_data.csv'
analysispath = 'Analysis/Analysis.txt'

print('Financial Analysis')
print('-----------------------------------------')

# Total Number of Months

with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    all_months = []
    for row in csvreader:
        all_months.append(int(row[1]))
months = len(all_months)

# List of Month to Month Change

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

# Sum and Average Monthly Change

total_change = sum(monthly_change)
average_change = total_change / len(monthly_change)

print(f'Total Months: {months}')
print(f'Total: ${sum(all_months)}')
print(f'Average Change: ${round(average_change, 2)}')

# Max and Min Monthly Change - Month and Change Amount

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

# Write to CSV File

with open(analysispath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ' ')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------------------'])
    csvwriter.writerow([f'Total Months: {months}'])
    csvwriter.writerow([f'Total: ${sum(all_months)}'])
    csvwriter.writerow([f'Average Change: ${round(average_change, 2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {max_row[0]} (${max_num})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {min_row[0]} (${min_num})'])

# Remove Quotations in CSV File

text = open(analysispath, "r")
text = ''.join([i for i in text]) \
    .replace('"', "")
x = open(analysispath,"w")
x.writelines(text)
x.close()       



        
    

