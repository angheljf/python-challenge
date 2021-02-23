# Import Modules
import os
import csv

# Set Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set path for file
csvpath = '../git/python-challenge/PyPoll/Resources/election_data.csv'
# Open and Read file
with open (csvpath) as csvfile:
    # Found new way to read file using .DictReader
    csvreader = csv.DictReader(csvfile)
   
    for row in csvreader:
        # Calculate total votes
        total_votes += 1
        # Calculate votes for each candidate
        if (row["Candidate"] == "Khan"):
            khan_votes += 1
        elif (row["Candidate"] == "Correy"):
            correy_votes += 1
        elif (row["Candidate"] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

# Calculate % of vote for each candidate
khan_percent = khan_votes / total_votes
correy_percent = correy_votes / total_votes
li_percent = li_votes / total_votes
otooley_percent = otooley_votes / total_votes

# Find out who won
winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

if winner == khan_votes:
    winner_name = "Khan"
elif winner == correy_votes:
    winner_name = "Correy"
elif winner == li_votes:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"

# Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Create new text file of Analysis
output_file = '../git/python-challenge/PyPoll/Analysis/poll_analysis.txt'

with open(output_file, 'w',) as txtfile:

# Write Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
