#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

csvpath = os.path.join("../Resources/budget_data.csv")
totals = 0
changes = 0
change = 0
previous = 0

increase = ["",0]
decrease = ["",999999999999999]


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#The total number of months included in the dataset
    rowcount = sum(1 for row in csvreader)
    print(rowcount)
    csvfile.seek(0)
    next(csvreader)

#The net total amount of "Profit/Losses" over the entire period
    total = sum(int(row[1]) for row in csvreader)
    print(total)
    
    
    csvfile.seek(0)
    next(csvreader)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#The average of the changes in "Profit/Losses" over the entire period
    for row in csvreader:
        change = (int(row[1])) - previous
        
        changes = changes + change

        previous = (int(row[1]))
        
        if (change > increase[1]):
            increase[1] = change
            increase[0] = row[0]
        if (change < decrease[1]):
            decrease[1] = change
            decrease[0] = row[0]
    
    average = (changes)/(rowcount - 1)        
    
    print(average)
        #changes.append(int(row[1]))
    #print(sum(changes))
    #average = (sum(changes) / len(changes))
    #print(str(average))  

        #changes.append(change)
    
    #print(previous)
    

    
      

        #maxium = True 
        #if change == max(changes):
        #    maxium = True
        #print(change)
    
    

    