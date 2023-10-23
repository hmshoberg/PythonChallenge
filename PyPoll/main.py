#3 Columns : "Voter ID", "County", "Candidate" Calculate the following:
#Total number of votes cast
#Percentatge of votes each candidate won
#Total number of votes each candidate won
#Winner of the election based on popular vote

import os
import csv


budget_csv = os.path.join("Pypoll", "Resources","election_data.csv")


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")