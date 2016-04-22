# Tracy Cook; Assignment 3 (API);  April 22, 2016

#Use the Sunlight Foundation's OpenStates API to do two things:
	#Loop over all the bills in Missouri this legislative session
	#Print out each bill's title and the name of its primary sponsor (you'll need to use the bill detail endpoint we discussed in class for this).
#Tips:
	#When you pass the bill number to the bill detail endpoint, you will need to process it to remove the space. When we looked at this in class, in our browsers, we didn't have to worry about it because modern browsers do that for us. Python doesn't. You'll see an example of this, which uses the urllib.quote() method in the api_example.py file in this directory.
	#Remember that what comes back from these endpoints, once they're processed, is a combination of lists and dictionaries. You'll have to pay close attention as you process the output so that you know which lookup syntax to use (output['whatever'] vs. output[0]).

# API Key: 1f366e0712bd4ad6b079afe3bb993434

import urllib, urllib2, json

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&fields=title,sponsors').read()

data = json.loads(response)

for bill in data:
    encoded_bill_id = urllib.unquote(bill['sponsors'][0]['name']).encode('utf-8')
    encoded_bill_id2 = urllib.unquote(bill['title']).encode('utf-8')
    print encoded_bill_id, encoded_bill_id2
    # writer.writerow(data)