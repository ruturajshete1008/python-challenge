
import os
import csv

file_path = os.path.join('..', 'PyPoll', 'election_data.csv')
output_file = open('/Users/ruturajshete/Desktop/python-challenge/PyPoll/Polling_data_results.txt', 'w')

Counter = 0
Candidates = {}
candidates_percent = {}
winner = ""
Candidate_count = 0

with open(file_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    for row in csvreader:
        Counter += 1
        if row[2] in Candidates.keys():
            Candidates[row[2]] += 1
        else:
            Candidates[row[2]] = 1

for key, value in Candidates.items():
    candidates_percent[key] = round((value/Counter) * 100, 2)

for key in Candidates.keys():
    if Candidates[key] > Candidate_count:
        winner = key
        Candidate_count = Candidates[key]

#The total number of votes cast

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(Counter))
print("-------------------------------------")

# A complete list of candidates who received votes and
# The percentage of votes each candidate won
# The total number of votes each candidate won

for key, value in Candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")

# The winner of the election based on popular vote.

print("Winner: " + winner)
print("-------------------------------------")


output_file.write("Election Results \n")
output_file.write("------------------------------------- \n")
output_file.write("Total Votes: " + str(Counter) + "\n")
output_file.write("------------------------------------- \n")
for key, value in Candidates.items():
    output_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
output_file.write("------------------------------------- \n")
output_file.write("Winner: " + winner + "\n")
output_file.write("------------------------------------- \n")