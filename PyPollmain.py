# import modules
import csv
import os



# name variables
total_votes = 0
candidate_list = []
candidate = []
vote_count = []
vote_perctage = []
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# create file path
file_path = 'Resources/election_data.csv'

# open path and get row count
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)
    row_count = sum(1 for row in csvreader)

# loop for counts on votes for cadidates
    for row in csvreader:
        candidate_list = row[2]
        if candidate is not candidate_list:
            candidate_list.append(candidate)
            vote_count[candidate]=+1

# write results

with open(csvreader,"w") as file:
# Print the final vote count to the terminal.
    election_results = (
        f"Election Results"
        f"-------------------------"
        f"Total Votes: {total_votes:,}"
        f"-------------------------")
    print(election_results, end="")


# Save the final vote count to the next file.
    file.write(election_results)
    for candidate in vote_count:
        votes = vote_count[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
#  Save the candidate results to our text file.
        file.write(candidate_results)
    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    file.write(winning_candidate_summary)


