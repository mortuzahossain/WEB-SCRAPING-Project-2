from bs4 import BeautifulSoup
import requests
import urllib2

url = 'https://www.imdb.com/chart/moviemeter?sort=ir,desc&mode=simple&page=1'

openurl = urllib2.urlopen(url)
html = openurl.read()
openurl.close()

soup = BeautifulSoup(html,'lxml')

tbody = soup.find('tbody' , class_ ='lister-list')
all_movie_name = tbody.find_all('td',class_= 'titleColumn')
all_image_url = tbody.find_all('td',class_ = 'posterColumn')
for x in xrange(len(all_movie_name)):
	file_name = all_movie_name[x].text.replace('\n','').encode('utf-8')
	file_name = 'output/' + file_name + '.jpg'
	my_replace = all_image_url[x].find('img')['src'].split('@')[-1]
	image_url = all_image_url[x].find('img')['src'].replace(my_replace,'._V1_SY1000_CR0,0,705,1000_AL_.jpg')
	print file_name

	f = open(file_name,'wb')
	f.write(requests.get(image_url).content)
	f.close()

