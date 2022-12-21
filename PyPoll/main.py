import os
import csv

# Print header
print()
print(f'Election Results')
print()
print(f'-------------------------------')
print()

election_csv = os.path.join("./Resources/" "election_data.csv")

candidate = []      #an empty list to store the candidate name output from election results
charles_counter = 0     #counting votes for charles c. stockham
diana_counter = 0           #counting votes for diana degette
raymon_counter = 0              #counting votes for raymon a. doane

#open file and read into dictionary
with open(election_csv, newline='') as csvfile:
    results = csv.DictReader(csvfile)

    #while going through each row, add all candidate names into a list of candidates
    for row in results:
        candidate.append(row['Candidate'])

        #if the row contains a vote for charles, add that to the charles vote counter
        if row['Candidate'] == 'Charles Casper Stockham':
            charles_counter = charles_counter + 1

        #if the row contains a vote for diana, add that to the diana vote counter
        elif row['Candidate'] == 'Diana DeGette':
            diana_counter = diana_counter + 1

        #if the row contains a vote for raymon, add that to the raymon vote counter
        elif row['Candidate'] == 'Raymon Anthony Doane':
            raymon_counter = raymon_counter + 1


    totalvotes=len(candidate)       #count the number of total votes by counting the number of entries found in candidate list
    charles_percentage = round((charles_counter/totalvotes)*100,3)  #calculate the percentage of votes for charles
    diana_percentage = round((diana_counter/totalvotes)*100,3)      #calculate the percentage of votes for charles
    raymon_percentage = round((raymon_counter/totalvotes)*100,3)    #calculate the percentage of votes for charles

    #if charles has more votes than both diana and raymon, declare him winner
    if charles_counter > diana_counter and charles_counter > raymon_counter:

        winner = 'Charles Casper Stockham'
    
    #if diana has more votes than both charles and raymon, declare him winner
    elif diana_counter > charles_counter and diana_counter > raymon_counter:

        winner = 'Diana DeGette'

    #if charles or diane are not the winners, then the winner is raymon
    else:

        winner = 'Raymon Anthony Doane'

#print analysis results to terminal
    print(f'Total Votes: {totalvotes}')
    print()
    print(f'-------------------------------')
    print()
    print(f'Charles Casper Stockham: {charles_percentage}% ({charles_counter})')
    print()
    print(f'Diana DeGette: {diana_percentage}% ({diana_counter})')
    print()
    print(f'Raymon Anthony Doane: {raymon_percentage}% ({raymon_counter})')
    print()
    print(f'-------------------------------')
    print()
    print(f'Winner: {winner}')
    print()
    print(f'-------------------------------')


#print analysis results to a txt file inside analysis folder
lines = [f'Election Results', "", '-------------------------------', "",f'Total Votes: {totalvotes}',"",'-------------------------------',""
        ,f'Charles Casper Stockham: {charles_percentage}% ({charles_counter})',"",f'Diana DeGette: {diana_percentage}% ({diana_counter})',""
        ,f'Raymon Anthony Doane: {raymon_percentage}% ({raymon_counter})',"",'-------------------------------',f'Winner: {winner}',"",'-------------------------------']


#write 
with open('./analysis/election data analysis.txt', 'w') as f:
    f.write('\n'.join(lines))