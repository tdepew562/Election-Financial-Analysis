import os
import csv
from collections import Counter

file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

def print_results(total_votes, vote_count, winner):
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")

    for candidate, votes in vote_count.items():
        percent = (votes / total_votes) * 100
        print(f'{candidate}: {percent:.3f}% ({votes})')

    print("-------------------------")
    print(f'The winner is: {winner}')
    print("-------------------------")

count = 0
candidatelist = []

with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1
        candidatelist.append(row[2])

# Use Counter to count votes
vote_count = Counter(candidatelist)

# Calculate total votes
total_votes = len(candidatelist)

# Find the winner
winner = vote_count.most_common(1)[0][0]

# Print results
print_results(total_votes, vote_count, winner)

# Print to a text file: election_results.txt
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f'Total Vote: {total_votes}\n')
    text.write("---------------------------------------\n")

    for candidate, votes in vote_count.items():
        percent = (votes / total_votes) * 100
        text.write(f'{candidate}: {percent:.3f}% ({votes})\n')

    text.write("---------------------------------------\n")
    text.write(f'The winner is: {winner}\n')
    text.write("---------------------------------------\n")

