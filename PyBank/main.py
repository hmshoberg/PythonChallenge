#Create a Python script to analyse the financial records of PyBank as follows
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

budget_csv = os.path.join("..", "Resources","budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



