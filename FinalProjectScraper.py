# Tracy Cook; Final Project (Missourian Weather Scraper)

import csv, mechanize
from bs4 import BeautifulSoup

output = open('FinalWeather_v2.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.set_handle_robots(False)
br.open('http://www.columbiamissourian.com/weather/?weather_zip=65201') #performs action

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

#Submit form
#br.select_form(nr=3) #fills out form
#br.form['weather_zip'] = ['65201']
#br.submit('btn btn-default')
#br.submit('weather_zip') #submits form

weather = soup.find('div',
	{'class': 'weather-right-now-temp',
	#'class': 'fa fa-refresh'
	#'class': 'weather-right-now-details'
})

#print weather

for x in weather:
	if x.string:
		print 'Temperature right now: ' + x.string.strip()

condition = soup.find('div',
	{'class': 'weather-right-now-condition'
})

#print condition

for x in condition:
	if x.string:
		print 'Condition right now: ' + x.string.strip()

# end of file
