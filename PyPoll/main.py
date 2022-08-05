import os
import csv

#rename csv file as variable
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

#Open and read CSV file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Read the header
csv_header = next(csv_reader)

#Lists to store data
count=0.0
candidate_list = []
charles=0.0
diana=0.0
raymon=0.0
new_list = []

for row in csv_reader:
        ballot_id = row[0]
        county = row[1]
        candidate = row [2]
        count(+1)
#list of candidates (HOW TO MAKE THIS CONDITIONAL?)
        candidate_list=[name for name in candidate]

#total number of votes per candidate
        if candidate == "Charles Casper Stockham":
            charles(+1)
        else: candidate == "Diana DeGette"
            diana(+1)
        else: candidate == "Raymon Anthony Doane"
            raymon(+1)



#percentage of votes per candidate
charles_percentage = charles/count
diana_percentage = diana/count

#winner of election based on popular vote

#print analysis to terminal (HOW TO ADD PERCENT SIGN AND PARENTHESES TO PRINTING)
print("Election Results")
print(f"Total Votes: {str(count)}")
print(f"Charles Casper Stockham: {str(charles_percentage)} % ( {str(charles)} )")

#export text file with results
with open(output_path, 'w') as txtfile:
         txtwriter = txtfile.write(
            ("Election Results")
            (f"Total Votes: {str(count)}")
            (f"Charles Casper Stockham: {str(charles_percentage)} % ( {str(charles)} )")
         )