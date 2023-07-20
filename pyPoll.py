import csv

# Path to the CSV file
csv_path = "PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csv_path, "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    
    # Skip the header row
    header = next(csv_reader)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Extract the candidate's name for the current row
        candidate = row[2]

        # Calculate the total number of votes
        total_votes += 1
        
        # Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Find the winner of the election
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate the percentage of votes for each candidate obtained
percentage_votes = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = percentage

# Print the analysis data
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
out = open("output.txt", "w")

# Print the analysis data
out.write("Election Results\n")
out.write("-------------------------\n")
out.write(f"Total Votes: {total_votes}\n")
out.write("-------------------------\n")

for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    out.write(f"{candidate}: {percentage:.3f}% ({votes})")
out.write("-------------------------\n")
out.write(f"Winner: {winner}\n")
out.write("-------------------------\n")

out.close()