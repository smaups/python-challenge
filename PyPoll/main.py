#The winner of the election based on popular vote.

import os
import csv

voters = []
canidates = []

votes = {"Khan": 0,
        "Correy": 0,
        "Li": 0,
        "OTooley": 0}

winner = 0 


csvpath = os.path.join("../Resources/election_data.csv")


print("----------------------")
print("Election Results")
print("______________________")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#The total number of votes cast
    votecount = sum(1 for row in csvreader)
    print(f'Total Votes: {votecount}')
    print("----------------------")
    csvfile.seek(0)
    next(csvreader)

#A complete list of candidates who received votes
    for row in csvreader:
        if row[2] not in canidates:
            canidates.append(row[2])

#The total number of votes each candidate won
        if row[2] == "Khan":
            votes["Khan"] += 1
        if row[2] == "Correy":
            votes["Correy"] += 1
        if row[2] == "Li":
            votes["Li"] += 1
        if row[2] == "O'Tooley":
            votes["OTooley"] += 1
#find the winner
    if (votes["Khan"] > winner):
        winner = votes["Khan"]
        victor = "Khan"
    if (votes["Correy"] > winner):
        winner = votes["Correy"]
        victor = "Correy"
    if (votes["Li"] > winner):
        winner = votes["li"]
        victor = "Li"
    if (votes["OTooley"] > winner):
        winner = votes["OTooley"]
        victor = "OTooley"
         
#The percentage of votes each candidate won
    percentKhan = (int(votes["Khan"]) / int(votecount))
    percentCorrey = (int(votes["Correy"]) / int(votecount))
    percentLi = (int(votes["Li"]) / int(votecount))
    percentOTooley = (int(votes["OTooley"]) / int(votecount))

    percentKhan = "{0:.0%}".format(percentKhan)
    percentCorrey = "{0:.0%}".format(percentCorrey)
    percentLi = "{0:.0%}".format(percentLi)
    percentOTooley = "{0:.0%}".format(percentOTooley)


#print(canidates)
    print(f'Khan: {percentKhan} {votes["Khan"]} ')
    print(f'Correy: {percentCorrey} {votes["Correy"]}')
    print(f'Li: {percentLi} {votes["Li"]}')
    print(f'OTooley: {percentOTooley} {votes["OTooley"]}')
    print("----------------------")
    print(f'Winner: {victor}')
    print("______________________")


