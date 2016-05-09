# Tracy Cook; Final Project (Missourian Weather Scraper)

import urllib2, csv, mechanize
from bs4 import BeautifulSoup

output = open('FinalWeather.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser() #set up
html = urllib2.urlopen('http://www.columbiamissourian.com/weather/?weather_zip=65201').read()

print html

br = mechanize.Browser()
br.set_handle_robots(False)
br.open('http://www.columbiamissourian.com/weather/?weather_zip=65201') #performs action


html = br.response().read()
soup = BeautifulSoup(html, "html.parser")


#Submit form
br.select_form(nr=1) #fills out form
br.form['form-control'] = ['65201']
#br.form['weather_zip'] = ['65201']
br.submit('btn btn-default')
#br.submit('weather_zip') #submits form


html = br.response().read()
soup = BeautifulSoup(html, "html.parser")


weather = soup.find('select',
	{'id': 'weather-refresh-ico',
	'class': 'fa fa-refresh'
	#'class': 'weather-right-now-details'
})

print output

#weather_values = weather.find('option')

for temp in 'weather-right-now-temp':
	temp_value = temp.text
	print temp['value']
	###county_id = county['value']

	main_table = soup.find('table',
		{'class': 'weather-now-container'
	})

	print main_table
	print output
	writer.writerow(data)
        
# end of file