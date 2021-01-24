import os
import csv

#set path
electionpath = os.path.join('Resources','election_data.csv')
textpath= os.path.join("Resources", "Analysis")


candidates=[]
votes=[]
percentage=[]
candidate_votes=[]
total_votes=0

with open(electionpath, newline='') as csvfile:  
        csvreader = csv.reader(csvfile, delimiter=',')
        #'next' to skip first row
        next(csvreader)  

        for row in csvreader:
            total_votes += 1

            if row[2] not in candidates:
                candidates.append(row[2])
            votes.append(row[2])

        for candidate in candidates:
            candidate_votes.append(votes.count(candidate))
            percentage.append(round(votes.count(candidate)/total_votes*100,3))

        winner=candidates[candidate_votes.index(max(candidate_votes))]
          
#print on terminal
# print("{candidates}")

# print("Election Results")
# print("------------------------------")
# print(f"Total Votes: {total_votes}")
# print("------------------------------") 
# for i in range(len(candidates)):
#     print(f'{candidates[i]}: {percentage[i]}% {candidate_votes[i]}')
# print("------------------------------") 
# print("------------------------------") 

#print to text file
#could not figure out how to print "for i" to text file so I inpunt them individually
output=(
"Election Results\n"
"---------------------------\n"
f"Total Votes: {total_votes}\n"
"---------------------------\n"
f"{candidates[0]} " f"{percentage[0]}% " f"{candidate_votes[0]}\n"
f"{candidates[1]} " f"{percentage[1]}% " f"{candidate_votes[1]}\n"
f"{candidates[2]} " f"{percentage[2]}% " f"{candidate_votes[2]}\n"
f"{candidates[3]} " f"{percentage[3]}% " f"{candidate_votes[3]}\n"
"---------------------------\n"
f"Winner: {winner}\n"
"---------------------------\n"
)
print(output)

#Write to the text path
with open(textpath, "w") as txt_file:
    txt_file.write(output)



