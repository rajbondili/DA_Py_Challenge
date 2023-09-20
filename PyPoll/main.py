import os
import csv

# Lists to store data
candidate_list = []
candidate_votes ={}
candidate_results ={}

#initialize variables
number_of_votes = 0
winning_votes = 0
winning_percentage = 0

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
print(csvpath)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #next(csvreader, None)
    # Read the header row first
    csv_header = next(csvfile)

    # Loop through looking for the budget data for total months
    for row in csvreader:
         number_of_votes += 1
         #candidates who received votes
         candidate_list.append(row[2])
    
    #sort the candidates in ascending order
    candidate_list.sort()

    #count votes per candidate
    for vote in  candidate_list:
        if vote not in  candidate_votes:
              candidate_votes[vote] = 0
              candidate_votes[vote] +=1
        else:
             candidate_votes[vote] +=1     
   
    # calculate the percentage of votes for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        candidate_percentage = float(candidate_votes[candidate])/ float(number_of_votes) * 100
        candidate_results[candidate] = (f":{candidate_percentage:.3f}% ({votes:,})")
        if votes > winning_votes and  candidate_percentage > winning_percentage:
            winning_votes = votes
            winning_percentage = candidate_percentage
            winner = candidate

    # Print the output to the console
    print(" ******** Election Analysis *************** ")
    print("---------------------------------------------")
    print(f"Total votes : {number_of_votes}")
    print("---------------------------------------------")
    print("Candidate results:")
    print("------------------")
    #printing the values from the candidate results
    for candidate in candidate_results:
        print ((candidate), candidate_results[candidate])
    print("----------------------------------------------")
    print(f"Winner :{winner}")    
    print("----------------------------------------------")     

# write the output into the file
# Set path for the output file
txtpath = os.path.join("analysis", "election_output.txt")

# Open the CSV using the UTF-8 encoding
with open(txtpath, 'w', newline='') as output_file:
   # Write the output into the output file
   output_file.write(" *********** Election Analysis ***************\n")
   output_file.write("----------------------------------------------\n")
   output_file.write(f"Total votes:  {number_of_votes}\n")
   output_file.write("----------------------------------------------\n")
   #writing the values from the candidate results
   for candidate in candidate_results:
        output_file.write (f"{(candidate)}, {candidate_results[candidate]}\n")
   output_file.write("----------------------------------------------\n")     
   output_file.write(f"Winner :{winner}\n")
   output_file.write("----------------------------------------------")  