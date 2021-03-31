total_votes = 0

import csv
file_path = "./Resources/election_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    VoterID = csv_header.index('Voter ID')
    County = csv_header.index('County')
    Candidate = csv_header.index('Candidate')
    candz = []

    for row in csvreader:
        #Count votes
        total_votes = total_votes + 1
        
        #Count candidates and add to list
        candz.append(str(row[Candidate]))

    #Return only unique values from candz list
    unique_candz = list(set(candz))

    #Count candidates from candz list
    cand1 = unique_candz[0]
    cand1_count = candz.count(cand1)

    cand2 = unique_candz[1]
    cand2_count = candz.count(cand2)

    cand3 = unique_candz[2]
    cand3_count = candz.count(cand3)

    cand4 = unique_candz[3]
    cand4_count = candz.count(cand4)

    #Find percentages
    cand1_percent = round((cand1_count / total_votes)*100)
    cand2_percent = round((cand2_count / total_votes)*100)
    cand3_percent = round((cand3_count / total_votes)*100)
    cand4_percent = round((cand4_count / total_votes)*100)

    #Find winner
    maxList = [cand1_percent, cand2_percent, cand3_percent, cand4_percent]
    Winning = max(maxList)
    if Winning == cand1_percent:
        Winner = cand1
    elif Winning == cand2_percent:
        Winner = cand2
    elif Winning == cand3_percent:
        Winner = cand3
    elif Winning == cand4_percent:
        Winner = cand4

    
    #Print results
    print(f"Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"{cand1}: {cand1_percent}.000% ({cand1_count})")
    print(f"{cand2}: {cand2_percent}.000% ({cand2_count})")
    print(f"{cand3}: {cand3_percent}.000% ({cand3_count})")
    print(f"{cand4}: {cand4_percent}.000% ({cand4_count})")
    print("-------------------------")
    print(f"Winner: {Winner}")
    print("-------------------------")

out_file = "./Analysis/output.txt"
with open(out_file, 'w') as outputFile:
    outputFile.write(f"Election Results")
    
    outputFile.write("-------------------------")
    
    outputFile.write(f"Total Votes: {total_votes}")
    
    outputFile.write("-------------------------")
    
    outputFile.write(f"{cand1}: {cand1_percent}.000% ({cand1_count})")
    
    outputFile.write(f"{cand2}: {cand2_percent}.000% ({cand2_count})")
    
    outputFile.write(f"{cand3}: {cand3_percent}.000% ({cand3_count})")
    
    outputFile.write(f"{cand4}: {cand4_percent}.000% ({cand4_count})")
    
    outputFile.write("-------------------------")
    
    outputFile.write(f"Winner: {Winner}")
    
    outputFile.write("-------------------------")