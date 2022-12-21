import os
import csv

# Print header
print(f'Financial Analysis')
print()
print(f'-------------------------------')
print()

budget_csv = os.path.join("./Resources/" "budget_data.csv")

list_of_months=[]    #an empty list to store the months in the first column
list_of_p_l=[]       #an empty list to store the profits and losses in the second column

#open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)                  #skip header row
    number_of_months = int(len(list(csvreader)))     #count the number of months (non-header rows) found in the csv file

print(f'Total Months: {number_of_months}')
print()

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",") #read csv without the header row

    for row in csvreader:
        list_of_months.append(row['Date'])   #add each month to the list of months
        list_of_p_l.append(int(row['Profit/Losses']))    #add each monetary value to the list of profits/lossess

net_total=sum(list_of_p_l)      #sum of all the values found in the list of profits and losses
print(f'Total: ${net_total}')
print()

changes=[]                 #an empty list of changes in monetary value

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    
    
    for i in range(number_of_months):
        difference=list_of_p_l[i]-list_of_p_l[i-1]      #find the difference between the value in one row and the value in the row following it
        changes.append(int(difference))                      #add each difference value found above to the list of changes

net_changes=sum(changes)-changes[0]                     #add up all the changes from one month to the other, since we started counting with the very first number, we will subtract that one
average_changes=net_changes/(number_of_months-1)        #to find the average change, we divide the total change value by the number of times the values changed, which is one less than the number of months
average_changes_rounded=round(average_changes,2)        #round the average to two decimal places
print(f'Average Change: ${average_changes_rounded}')
print()


max_value = max(changes)                                            #find the maximum changes in the changes list
max_index = changes.index(max_value)                                #determine the index of the max change in that list
max_month = list_of_months[max_index]                               #find the value of the matching index in the list of months
print(f'Greatest Increase in Profits : {max_month} (${max_value})')
print()

min_value = min(changes)                                            #find the minimum changes in the changes list
min_index = changes.index(min_value)                                #determine the index of the min change in that list
min_month = list_of_months[min_index]                               #find the value of the matching index in the list of months
print(f'Greatest Decrease in Profits: {min_month} (${min_value})')

#write reults into a textfile inside analysis folder

lines = [f'Financial Analysis', "", '-------------------------------', "",f'Total Months: {number_of_months}', "", f'Total: ${net_total}', "",f'Average Change: ${average_changes_rounded}', "",f'Greatest Increase in Profits : {max_month} (${max_value})', "", f'Greatest Decrease in Profits: {min_month} (${min_value})' ]

with open('./analysis/financial analaysis result.txt', 'w') as f:
    f.write('\n'.join(lines))