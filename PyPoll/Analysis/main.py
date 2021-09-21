#import os module and reading csv
import os
import csv

#path to collect data from resources folder
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

#variables

candidate = []
winning_votes = []
candidate_votes = 0
winning_candidates = []
voter_ID = []
county = []
candidate_name = []
vote_results = []
winner_date = {}

#read CSV
with open(election_data_csv) as csv_file:

    # add CSV reader
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip headers
    csv_header = next(csv_file)

    for row in csv_reader:

        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # loop through candidae list
for name in set(candidate):

    # add candidate name to list 
    candidate_name.append(set(candidate))

    #count candidate votes
    candidate_votes = candidate.count(name)

    winning_votes.append(candidate_votes)
    winning_candidates.append(name)

#combine list into tuple
vote_results = list(zip(winning_candidates, winning_votes))
vote_results.sort(key=lambda x:x[1], reverse = True)

#print(vote_percentage)


#print(winning_votes)
#print(winning_candidates)


# print final
print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {len(candidate)}")
print(f"-----------------------")

for i in range(len(winning_candidates)):


    print(f"{vote_results[i][0]}: {vote_results[i][1]/len(candidate)*100} / {vote_results[i][1]}")


print(f"-----------------------")
print(f"Winner: {vote_results[0][0]}")
print(f"-----------------------")

#export to txt file
output_path = os.path.join("..", "Analysis", "Election_Results.txt")

with open(output_path, 'w', newline="") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"-----------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(candidate)}")
    file.write("\n")
    file.write(f"-----------------------")
    file.write("\n")

    for i in range(len(winning_candidates)):

        file.write(f"{vote_results[i][0]}: {vote_results[i][1]/len(candidate)*100} / {vote_results[i][1]}")
        file.write("\n")
    
    file.write("\n")
    file.write(f"-----------------------")
    file.write("\n")
    file.write(f"Winner: {vote_results[0][0]}")
    file.write("\n")
    file.write(f"-----------------------")
