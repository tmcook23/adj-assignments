# Tracy Cook; Final Project (Missourian Weather Scraper)

import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.open('http://www.columbiamissourian.com/weather/?weather_zip=65201')
#Change ZIP code in URL to switch locations

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

weather = soup.find('div',
	{'class': 'weather-right-now-temp',
})

for x in weather:
	if x.string:
		print 'Temperature right now: ' + x.string.strip()

condition = soup.find('div',
	{'class': 'weather-right-now-condition'
})

for x in condition:
	if x.string:
		print 'Condition right now: ' + x.string.strip()

# end of file
