import os
import csv

election_data_csv = os.path.join("data", "election_data_1.csv")

# create lists to store data
idcolumn = []
countycolumn = []
candidatecolumn = []
candlist = []
votecount = []
percentofvotes = []


with open(election_data_csv, newline="") as csvfile:
    electionreader = csv.reader(csvfile, delimiter=",")
    
    for row in electionreader:
    
        # add ids
        idcolumn.append(row[0])
        ids = idcolumn[1:]

        # add candidate
        candidatecolumn.append(row[1])
        candidates = candidatecolumn[1:]


Total_votes = len(ids)

# create list of unique candidates
for i in range(0, int(Total_votes) - 1): 

    if candidates[i] in candlist:

        candlist = candlist
    
    else: 
        
        candlist.append(candidates[i]) 


# count the votes

x = 1

for i in range(0, int(len(candidates)) - 1):
    
    for j in range(0, int(len(candlist)) - 1):

        if candidates[i] == candlist[j]:
           
            votecount[j] = x + 1



print("Election Results")
print("--------------------")
print("Total Votes: " + int(len(ids)))
print("--------------------")

for i in range(0, int(len(candlist)) - 1): 

    percentofvotes = (int(votecount[i]) / int(Total_votes))

    candsummary = str(candlist[i]) + ": " + str(percentofvotes[i]) + " (" + str(votecount[i]) + ")" + '\n'
    
    print(candsummary)

print("--------------------")
print("Winner: ")
print("--------------------")
