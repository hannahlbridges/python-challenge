import csv
import os

print('Election Results')
print('-----------------------------------------')

resultspath = 'Resources/election_data.csv'



with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    candidates = []
    for vote in csvreader:
        candidates.append(vote[2]) if vote[2] not in candidates else candidates
        
with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)        
    total_votes = sum(1 for row in csvreader)

print(f'{candidates[0]}:')
print(f'{candidates[1]}:')
print(f'{candidates[2]}:')
print(f'{candidates[3]}:')
    