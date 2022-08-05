import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

#variables    
total_profits = 0.0
cnt = 0
change=[]
greatest_increase=["",0]
greatest_decrease=["",9999999999]
prev=0.0

#Open and Read CSV
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Read the header row and print
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")


    first_row = next(csv_reader)
    cnt = cnt+1
    total_profits += int(first_row[1])
    prev = int(first_row[1])


#Net total of "Profit/Losses"
    for row in csv_reader:
        date = row[0]
        profits_losses = int(row[1])
        cnt = cnt+1
        
        
        
#Count number of months in data
        total_profits += int(row[1])

#Changes in Profits/Losses
        change_now = int(row[1])-prev
        change += [change_now]
        prev = int(row[1])
        

        if change_now > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=change_now
        if change_now < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=change_now

        

    
    

#Average of Changes in "Profit/Losses"
average = sum(change)/len(change)

#Greatest increase in profits (date and amount) (ARE MAX AND MIN REAL FUNCTIONS???)

#Greatest decrease in profits (date and amount)
#greatest_decrease = min(change)
#print analysis to terminal
#print(f"Total Months: {cnt}")
print(f"Total: {total_profits}")
#print(f"Change: {change}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")

#Set variable for output file
output_file = os.path.join("pybank_final.csv")

#Export text file of analysis
with open(output_file, 'w') as txtfile:
    writer = csv.writer(txtfile)

    # Write the header row
    writer.writerow([f"Total Months: {cnt}"])
    writer.writerow([f"Total: $ {total_profits}"])     
    writer.writerow([f"Average Change: $ {average}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase}"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease}"])
        #  )
        #  txtfile.write(change)