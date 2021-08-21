import csv

total_votes=0
candidate_dic={}
vote_percentage=[]
max_vote=0
with open('resources/election_data.csv','r') as csvfile:
    csvread=csv.reader(csvfile,delimiter=',')
    header=next(csvfile)
    for row in csvread:
        total_votes+=1
        if row[2] not in candidate_dic.keys():
            candidate_dic[row[2]]=0
        candidate_dic[row[2]]+=1

lines=[
        'Election Results \n-------------------------\n',
        f'Total Votes: {total_votes}\n-------------------------\n'
    ]

for keys,values in candidate_dic.items():
    line= (f'{keys}: {round((values/total_votes*100),2)} % ({values})\n')
    lines.append(line)
    if values>max_vote:
        max_vote=values
        winner=keys

lines.append(f'-------------------------\nWinner: {winner}\n-------------------------')

with open('analysis/analysis.txt', 'w', newline='') as t:
    t.writelines(lines)

with open('analysis/analysis.txt','r') as f:
    for x in f:
        print(x)