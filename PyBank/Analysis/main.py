import os
import csv

#set path
budgetpath = os.path.join('Resources','budget_data.csv')
textpath= os.path.join("Resources", "Analysis")

#initiate values
total  =0
average_change = 0
total_rows = 0
greatest_increase = 0
greatest_decrease = 0


with open(budgetpath, newline='') as csvfile:  
        csvreader = csv.reader(csvfile, delimiter=',')
        #'next' to skip first row
        next(csvreader)  

        for row in csvreader:
                #Count Rows
                total_rows += 1
                #Sum of all profits/losses
                total = total+int(row[1])
                previous=int(row[1])

                if (greatest_increase < int(row[1])):
                        greatest_increase = int(row[1])        
                        Positive_Month = row[0]

                if (greatest_decrease > int(row[1])):
                        greatest_decrease = int(row[1])
                        Negative_Month = row[0]

                monthly_change=(int(row[1])+1)-previous
                previous=int(row[1])
                all_changes = average_change+int(row[1])
                average = all_changes / total_rows

#Print to terminal

output=(
"Financial Analysis")
"---------------------------"
f"Total Months: {total_rows}\n"
f"Total:${total}\n"
f"Average Change: ${average}\n"
f"Greatest Increase in Profits: {Positive_Month} ${greatest_increase}\n"
f"Greatest Decrease in Profits: {Negative_Month} ${greatest_decrease}\n"

print(output)

#Write to the text path
with open(textpath, "w") as txt_file:
    txt_file.write(output)