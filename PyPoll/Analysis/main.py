import os
import csv

#set path
electionpath = os.path.join('Resources','election_data.csv')

total_votes=0
candidates=0

with open(electionpath, newline='') as csvfile:  
        csvreader = csv.reader(csvfile, delimiter=',')
        #'next' to skip first row
        next(csvreader)  

        for row in csvreader:
            total_votes += 1
            candidate=row["Candidate"]

print("candidate")

print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------") 




print("------------------------------") 

print("------------------------------") 



# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------