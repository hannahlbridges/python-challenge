import csv
import os

print('Election Results')
print('-----------------------------------------')

resultspath = '/Resources/election_data.csv'

with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    