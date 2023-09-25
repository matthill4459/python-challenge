import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Veriables needed to be defined
total_votes = 0
candidates = {}

#This will read the csv file 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # this will iterate through the csv file
    for row in csvreader:

            # this will incrementally count the total_votes  for each row
            total_votes += 1

            #This will extract the candidates name from the row.
            #also update each candidates vote count and incrementaly count it
            candidate_name = row[2]
            if candidate_name not in candidates:
                candidates[candidate_name] = 1
            else:
                candidates[candidate_name] += 1
    #This will calculate the percentages and store the in a directory
    percentages = {}
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        percentages[candidate] = percentage

    # Findes the winner
    winner = max(candidates, key=candidates.get)

    #this prints the election results. incluing total number of votes for each candidate and there percentage 
    #as compared to the others
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # this creates a textfile of the results from above
    with open('election_results.txt', 'w') as textfile:
        textfile.write("Election Results\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("-------------------------\n")
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("-------------------------\n")
