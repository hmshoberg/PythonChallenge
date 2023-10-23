#3 Columns : "Voter ID", "County", "Candidate" Calculate the following:
#Total number of votes cast
#Percentatge of votes each candidate won
#Total number of votes each candidate won
#Winner of the election based on popular vote

import os
import csv
              
path = "PyPoll/Resources/election_data.csv"

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the headers
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #values and lists
    total_vote = 0
    candidates = []
    percent_votes ={}
    candvotes = {}

    for row in csvreader:
    
        #Add counter
        total_vote +=1

        if row [2] in candvotes:
            candvotes[row[2]] +=1
            
        else:
            candvotes[row[2]] = 1

    winner_count = 0    
        
        #Percentage of votes
    for candidates in candvotes:

        percent_votes[candidates] = (candvotes[candidates] / total_vote) * 100
        percentage_formatted = "{:.3f}".format(percent_votes[candidates])

        #The winner based on popular vote

        if candvotes[candidates] > winner_count:
            winner_count = candvotes[candidates]
            winner = candidates


        print("Election Results" + "\n")
        print("------------------------------")
        print(f"Total Votes: {total_vote}" + "\n")
        print("------------------------------")
        print()
        print(f"Winner: {winner}" + "\n")

#Export results to a text file
Results = os.path.join("PyPoll", "Analysis", "PyPoll.txt")

with open("PyPoll.txt", "w") as text:
    text.write("Election Results" + "\n")
    text.write("------------------------------\n")
    text.write(f"Total Votes: {total_vote}" + "\n")
    text.write("------------------------------\n")
    text.write(f"Winner: {winner}" + "\n")