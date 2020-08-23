import os
import csv

csvpath = os.path.join('..','PyBank','budget_data.csv')

#create list holders for data
total_months = []
total = []
average_change = []

# CSV reader specifies delimiter and variable that holds contents
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Read the header row first
    csv_header = next(csvreader)
#Read through each row of data after header
    for row in csvreader:

        total_months.append(row[0])
        total.append(int(row[1]))

    for i in range(len(total)-1):
#Difference between two months and append to monthly profit change
        average_change.append(total[i+1]-total[i])
#Use max for profit and min for losses
max_increase_value = max(average_change)
max_decrease_value = min(average_change)

#count +1
max_increase_month = average_change.index(max(average_change))+1
max_decrease_month = average_change.index(min(average_change))+1

#print
print("Financial Analysis")
print (f"--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total)}")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")       

f = open('Pybank-output.txt', 'w')
print("Financial Analysis", file=f)
print (f"--------------------------")
print(f"Total Months: {len(total_months)}",file=f)
print(f"Total: ${sum(total)}",file=f)
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}",file=f)
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})",file=f)
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})",file=f)       
f.close()
