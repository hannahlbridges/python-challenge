import csv
import os

print('Election Results')
print('-----------------------------------------')

resultspath = 'Resources/election_data.csv'



with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []
    for vote in csvreader:
        candidates.append(vote[2]) if vote[2] not in candidates else candidates

with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)      
    for vote in csvreader:    
        if vote[2] == 'Khan':
            khan.append(vote[0])
        elif vote[2] == 'Correy':
            correy.append(vote[0])
        elif vote[2] == 'Li':
           li.append(vote[0])
        elif vote[2] == "O'Tooley":
            otooley.append(vote[0])

print(len(khan), len(correy), len(li), len(otooley))

with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)        
    total_votes = sum(1 for row in csvreader)
    
print(f'Total Votes: {total_votes}')
print(f'{candidates[0]}:')
print(f'{candidates[1]}:')
print(f'{candidates[2]}:')
print(f'{candidates[3]}:')
    