import os
import csv

#rename csv file as variable
election_data_csv = os.path.join("Resources", "election_data.csv")

#Open and read CSV file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Read the header
    csv_header = next(csv_reader)

#Lists to store data
    count=0
    candidate_list = []
    charles=0.0
    diana=0.0
    raymon=0.0
    new_list = []

    for row in csv_reader:
        ballot_id = row[0]
        county = row[1]
        candidate = row [2]
        count = count(+1)
#list of candidates
        candidate_list=[name for name in candidate]

#total number of votes per candidate
        if candidate == "Charles Casper Stockham":
            charles(+1)
        if candidate == "Diana DeGette":
            diana(+1)
        if candidate == "Raymon Anthony Doane":
            raymon(+1)



#percentage of votes per candidate
charles_percentage = charles/count
diana_percentage = diana/count
raymon_percentage = raymon/count

#winner of election based on popular vote


#print analysis to terminal (HOW TO ADD PERCENT SIGN AND PARENTHESES TO PRINTING)
# print("Election Results")
# print(f"Total Votes: {str(count)}")
# print(f"Charles Casper Stockham: {str(charles_percentage)} % ( {str(charles)} )")


#Set variable for output file
output_file = os.path.join("pypoll_final.csv")

#Export text file of analysis
with open(output_file, 'w') as txtfile:
    writer = csv.writer(txtfile)

    # Write the header row
    writer.writerow([f"Election Results"])
    writer.writerow([f"Total Votes: {count}"])     
    writer.writerow([f"Charles Casper Stockham: {charles_percentage} % {charles}"])
    writer.writerow([f"Diana DeGette: {diana_percentage} % {diana}"])
    writer.writerow([f"Raymon Anthony Doane: {raymon_percentage} % {raymon}"])
    writer.writerow([f"Winner: Diana DeGette"])
    