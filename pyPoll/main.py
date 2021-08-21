import csv

total_votes=0
candidate_list=[]
candidate_vote=[]
vote_percentage=[]
max_vote=0
with open('resources/election_data.csv','r') as csvfile:
    csvread=csv.reader(csvfile,delimiter=',')
    header=next(csvfile)
    for row in csvread:
        total_votes+=1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_vote.append(0)
        for i in range(len(candidate_list)):
            if row[2]==candidate_list[i]:
                candidate_vote[i]+=1
    for i in range(len(candidate_list)):
        vote_percentage.append(round((candidate_vote[i]/total_votes*100),2))
        if candidate_vote[i]>max_vote:
            max_vote=candidate_vote[i]
            winner=candidate_list[i]

print('Election Results \n-------------------------')
print(f'Total Votes: {total_votes}\n-------------------------')
for i in range(len(candidate_list)):
    print(f'{candidate_list[i]}:{vote_percentage[i]}% ({candidate_vote[i]})')
print(f'-------------------------\nWinner: {winner}\n-------------------------')


print('Election Results \n-------------------------',file=open("analysis/analysis.txt", "a"))
print(f'Total Votes: {total_votes}\n-------------------------',file=open("analysis/analysis.txt", "a"))
for i in range(len(candidate_list)):
    print(f'{candidate_list[i]}:{vote_percentage[i]}% ({candidate_vote[i]})',file=open("analysis/analysis.txt", "a"))
print(f'-------------------------\nWinner: {winner}\n-------------------------',file=open("analysis/analysis.txt", "a"))



