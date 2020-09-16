import csv
import os

resultspath = 'Resources/election_data.csv'

with open(resultspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    candidates = []
    for vote in csvreader:
        candidates.append(vote[2]) if vote[2] not in candidates else candidates

khan = []
correy = []
li = []
otooley = []

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

most_votes = max(len(khan), len(correy), len(li), len(otooley))
if most_votes == len(khan):
    winner = "Khan"
elif most_votes == len(correy):
    winner = "Coorey"
elif most_votes == len(li):
    winner = "Li"
elif most_votes == len(otooley):
    winner = "O'Tooley"

print('Election Results')
print('---------------------------------------')    
print(f'Total Votes: {total_votes}')
print('---------------------------------------')
print(f'{candidates[0]}: {percent_khan}% ({len(khan)})')
print(f'{candidates[1]}: {percent_correy}% ({len(correy)})')
print(f'{candidates[2]}: {percent_li}% ({len(li)})')
print(f'{candidates[3]}: {percent_otooley}% ({len(otooley)})')
print('---------------------------------------')
print(f'Winner: {winner}')  
print('---------------------------------------')

analysispath = 'Analysis/Analysis.txt'

with open(analysispath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ' ')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['---------------------------------------'])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(['---------------------------------------'])
    csvwriter.writerow([f'{candidates[0]}: {percent_khan}% ({len(khan)})'])
    csvwriter.writerow([f'{candidates[1]}: {percent_correy}% ({len(correy)})'])
    csvwriter.writerow([f'{candidates[2]}: {percent_li}% ({len(li)})'])
    csvwriter.writerow([f'{candidates[3]}: {percent_otooley}% ({len(otooley)})'])
    csvwriter.writerow(['---------------------------------------'])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(['---------------------------------------'])