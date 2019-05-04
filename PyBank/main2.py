import os
import csv

csvpath = os.path.join("../Resources/budget_data.csv")

rowcount = 0
total = 0

previous = 0
change = 0 

increase = ["",0]
decrease = ["", 9999999]

changes = -867884
average = 0


with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        rowcount = rowcount + 1
        total = total + int(row[1])
        
        if total != 1:
            change = int(row[1])- previous 

        changes = changes + change



        previous = int(row[1])

        if (change > increase[1]):
            increase[1] = change
            increase[0] = row[0]
        
        if (change < decrease[1]):
            decrease[1] = change
            decrease[0] = row[0]

        

    average = (changes)/(rowcount - 1)

    print("--------------------")
    print("Financial Analysis")
    print("____________________")
    print(f"Total Months: {str(rowcount)}")
    print(f"Total: {str(total)}")
    print(f"Average Change: {average}")
    print(f"Greatest Increase: {str(increase[0])} by {str(increase[1])}")
    print(f"Greatest Decrease: {str(decrease[0])} by {str(decrease[1])}")
    