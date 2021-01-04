#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import os

poll_input = os.path.join("election_data.csv")
poll_output = os.path.join("poll_analysis.txt")

# initial values
total_votes = 0
candidates_list = []
candidate_votes = { }
winner_candidate = ""
winner_votes = 0

with open(poll_input) as poll_data:
    reader = csv.reader(poll_data)
    
    header = next(reader)
    
    for row in reader:
        
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_votes[candidate] = 0
            
        candidate_votes[candidate] += 1

with open(poll_output, "w") as txt_file:
    
    count_output = (
        f"\n\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    # print(count_output, end = "")
    
    txt_file.write(count_output)
    
    for candidate in candidate_votes:
        
        number_votes = candidate_votes.get(candidate)
        vote_percent = (float(number_votes) / float(total_votes)) * 100
        
        if (number_votes > winner_votes):
            winner_votes = number_votes
            winner_candidate = candidate
            
        candidate_output = f"{candidate}: {vote_percent:.3f}% ({number_votes})\n"
        
        # print(candidate_output, end = "")
        
        txt_file.write(candidate_output)
        
    winner_candidate_info = (
        f"-----------------\n"
        f"Winner: {winner_candidate}\n"
        f"-----------------\n"
    )
    
    print(winner_candidate_info)
    
    txt_file.write(winner_candidate_info)
        




# In[ ]:




