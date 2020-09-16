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

with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)        
    total_votes = sum(1 for row in csvreader)

percent_khan = round(len(khan) / total_votes * 100, 3)
percent_correy = round(len(correy) / total_votes * 100, 3)
percent_li = round(len(li) / total_votes * 100, 3)
percent_otooley = round(len(otooley) / total_votes * 100, 3)
    
print(f'Total Votes: {total_votes}')
print(f'{candidates[0]}: {percent_khan}%')
print(f'{candidates[1]}: {percent_correy}%')
print(f'{candidates[2]}: {percent_li}%')
print(f'{candidates[3]}: {percent_otooley}%')
    