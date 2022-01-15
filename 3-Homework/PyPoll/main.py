# Main PyBank Code
# Modules
import os
import csv
import sys
import shutil


# Set path for file
election_csv = os.path.join( "Resources", "election_data.csv")


#set variables
num_votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0
khan = []
candidates = []
votes = []
poll_data = []



with open(election_csv) as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter = ',')

    for row in csvreader:
        num_votes += 1
        
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
            

with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)



#The total number of votes cast

    for row in csv_reader:
       

        if (row[2] == candidates[0]):
            khan_count += 1
        
        elif (row[2] == candidates[1]):
            correy_count += 1

        elif (row[2] == candidates[2]):
            li_count += 1

        else:
            otooley_count += 1

kahn_percentage = round((khan_count / num_votes),2)*100
correy_percentage = round((correy_count / num_votes),2)*100
li_percentage = round((li_count / num_votes),2)*100
otooley_percentage = round((otooley_count / num_votes),2)*100


#The winner of the election based on popular vote.

if kahn_percentage >= correy_percentage and li_percentage and otooley_percentage:
    winner = "Khan"
elif correy_percentage >= li_percentage and otooley_percentage and kahn_percentage:
    winner = "Correy"
elif li_percentage >= correy_percentage and otooley_percentage and kahn_percentage:
    winner = "Li"
else: 
    winner = "O'Tooley"
#print sequence

    #for vote in csv_reader:

        # Create list of first column in CSV
        #votes.append(vote[0])

        # Create list of third column in CSV
        #candidates.append(vote[2])


print(f"Election Results")
print("---------------------")
print (f"Total Votes:  {num_votes}")
print("---------------------")
print(f"{candidates[0]}: {kahn_percentage}% ({khan_count})")
print(f"{candidates[1]}: {correy_percentage}% ({correy_count})")
print(f"{candidates[2]}: {li_percentage}% ({li_count})")
print(f"{candidates[3]}: {otooley_percentage}% ({otooley_count})")
print("---------------------")
print(f"Winner: {winner}")

#export results to txt file


sys.stdout = open("results.txt", "w")

print(f"Election Results")
print("---------------------")
print (f"Total Votes:  {num_votes}")
print("---------------------")
print(f"{candidates[0]}: {kahn_percentage}% ({khan_count})")
print(f"{candidates[1]}: {correy_percentage}% ({correy_count})")
print(f"{candidates[2]}: {li_percentage}% ({li_count})")
print(f"{candidates[3]}: {otooley_percentage}% ({otooley_count})")
print("---------------------")
print(f"Winner: {winner}")

sys.stdout.close()

shutil.move('/Users/61430/OneDrive/Desktop/Data Analytics/Coursework/03-Python/3-Homework/PyPoll/results.txt','C:/Users/61430/OneDrive/Desktop/Data Analytics/Coursework/03-Python/3-Homework/PyBank/Analysis/results.txt')
