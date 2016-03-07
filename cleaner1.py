# Your code goes here
# Tracy Cook; Assignment 1; March 5, 2016

import csv

# Open our input and output files
csvfile = open('cleanme.csv', 'r')
outfile = open('cleanme-clean.csv', 'w')

# Now a DictReader and DictWriter
# DictReader and DictWriter are imported libraries
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

# DictWriter writes to outfile
# reader.fieldname refers to the headers

# Write headers
writer.writeheader()

# Everything above this is setup
# Clean and write the data to output
for row in reader:
	#print row['first_name']
	# We are overwriting something that already exists
    row['first_name'] = row['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    row['city'] = row['city'].replace('&nbsp;', ' ')
    if row['amount']>1000.00: print row
    
    print row
    writer.writerow(row)
    
