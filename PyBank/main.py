#Create a Python script to analyse the financial records of PyBank as follows
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv


budget_csv = os.path.join("Pybank", "Resources","budget_data.csv")

#Lists to store data
date = []
profit = []

MonthCount = 0
currentprofit = 0
totalprofit = 0
totalchange = 0
initalprofit = 0
avgchange = 0
proflos = 0


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    #Read the headers/Skip headers
    csv_header = next(csvreader)

    first_row = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Count months
    MonthCount +=1 
    #print(MonthCount)

    #Track profits
    totalprofit += int(first_row[1])
    proflos = int(first_row[1])

    for row in csvreader:
        #print(row, type(row))
        
        #Get dates and track

        date.append(row[0])

        #Track changes
        totalchange = int(row[1])-proflos
        profit.append(totalchange)
        proflos = int(row[1])

        MonthCount += 1
        
        #Total net amount of Profits/Losses
        totalprofit = totalprofit + int(row[1])

    #Find greatest increase in profits (date and amount)
    greatestinc = max(profit)
    greatestdec = min(profit)

    greatest_index = profit.index(greatestinc)
    greatestdate = date[greatest_index]
    lowest_index = profit.index(greatestdec)
    lowestdate = date[lowest_index]

    avgchange = (totalchange)/(MonthCount - 1)
    

    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months: " +str(MonthCount))
    print("Total: " + "$" + str(totalprofit))
    print(str(f"Average Change: ${avgchange}"))
    print(str(f"Greatest Increase in Profits: {greatestdate} (${str(greatestinc)})"))
    print(str(f"Greatest Decrease In Profits: {lowestdate} (${str(greatestdec)})"))

#Export results to a text file
Results = os.path.join("Analysis", "PyBank.txt")

with open("Results", "w") as text: 

    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------\n")
    text.write("Total Months: " +str(MonthCount) + "\n")
    text.write("Total: " + "$" + str(totalprofit) + "\n")
    text.write(str(f"Average Change: ${avgchange}") + "\n")
    text.write(str(f"Greatest Increase in Profits: {greatestdate} (${str(greatestinc)})") + "\n")
    text.write(str(f"Greatest Decrease In Profits: {lowestdate} (${str(greatestdec)})") + "\n")
    