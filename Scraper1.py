# Tracy Cook; Assignment 2; DUE MONDAY, APRIL 11

#Your scraper should:
	#Loop over each county listed in the "counties" dropdown
 	#Scrape results ONLY for the five active candidates: Clinton, Sanders, Cruz, Kasich and Trump
	#Display that information (either printed to the terminal or as CSV) in a format resembling this:

	#```
	#county, clinton_pct, sanders_pct, cruz_pct, kasich_pct, trump_pct
	#Adair,  40.745%,     58.797%,     33.487%,  14.758%,     40.391%
	#etc.
	#``` 

import csv, mechanize
from bs4 import BeautifulSoup

output = open('Scraper1Results.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser() #set up
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx') #performs action
br.select_form(nr=0) #fills out form
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Loop through counties by 2
for x in xrange(0, 114, 2):
	# Everything from here should be indented
	# You must re-select the form with the line below
	br.select_form(nr=0)

	# then determine the value to assign to the 'select' statement
	if (x+1) < 10:
		br.form['ctl00$MainContent$cboCounty'] = ['00' + str(x+1)]
	else:
		if (x+1) < 100:
			br.form['ctl00$MainContent$cboCounty'] = ['0' + str(x+1)]
		else:
			br.form['ctl00$MainContent$cboCounty'] = [str(x+1)]

	# NEED TO ADD LINE TO MAKE SCRAPE STOP AFTER 300 (or whatever it is)

	# Figure out what the "align" and "class" attributes are
	# Then figure out how to only get the top 5 candidates
	# GET THE COUNTY NAMES

	# correct form element has been accessed 
	# now we can submit with the next line
	br.submit('ctl00$MainContent$btnCountyChange')

	# now the table has appeared, we can access the data

	# read the tables and put it into a variable
	html = br.response().read()
	
	soup = BeautifulSoup(html, "html.parser") #Transform the HTML into a BeautifulSoup object. Use BeautifulSoup to parse the html.

	# Find the main table using both the "align" and "class" attributes
	main_table = soup.find('table',
		{'id': 'MainContent_dgrdResults'
	})

	# Now get the data from each table row
	for row in main_table.find_all('tr'):
		#data = [cell.text for cell in row.find_all('td')]
		data = [cell.text.replace(u'\xa0', ' ') for cell in row.find_all('td')] #on the right we have the loop
		#print data
		writer.writerow(data)

# SAME CONCEPT AS COUNTIES BUT FOR CANDIDATE
#		 if data:
#            if data[0] in ['Hillary Clinton', 'Ted Cruz', 'Donald J. Trump', 'Bernie Sanders', 'John R. Kasich']: 
#                print option_values[i], data[0], data[3]
#         writer.writerow(data)
		#end of loop 2
	# end of loop 1



#TO ADD KANSAS CITY:
#br.select_form(nr=0)
#br.form['ctl00$MainContent$cboCounty'] = ['095A']
#br.submit('ctl00$MainContent$btnCountyChange')
#html = br.response().read()
#soup = BeautifulSoup(html, "html.parser")

# end of file