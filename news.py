import sys
import bs4 as bs
import requests
from collections import defaultdict

base_url = 'https://www.telegraphindia.com/'

data = defaultdict(dict)
req = requests.get(base_url)
html = req.text
soup = bs.BeautifulSoup(html, 'lxml')

def link_datasets():
	u_lists = soup.find_all('ul', class_ = 'nav nav-list')

	for lists in u_lists:
		list = lists.find_all('li')

		for link in list:
			links = link.find_all('a')

			for sub_link in links:
				sub_url_text = sub_link.text
				sub_url = base_url + str(sub_link.get('href'))
				data[sub_url_text] = sub_url

def frontpage():
	table = soup.find_all('table', class_ = 'story-table')

	for te in table:
		td = te.find('td')
		print td.text
		print "\n\n\n\n"
		link = td.find('a')

		sub_url = 'https://www.telegraphindia.com/' + str(link.get('href'))
		sub_req = requests.get(sub_url)
		sub_html = sub_req.text
		sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

		story = sub_soup.find_all('td', class_ = 'story')
		
		for paragraphs in story:
			p = paragraphs.find_all('p')
			for i in p:
				print i.text
		print "\n\n\n\n"

def getData(category):
	url = data[category]
	request = requests.get(url)
	html = request.text
	soup = bs.BeautifulSoup(html, 'lxml')

	category_story = soup.find_all('td',class_ ='story')

	for links in category_story:
		link = links.find('a')

		sub_url = url[:-9]+str(link.get('href'))
		sub_req = requests.get(sub_url)
		sub_html = sub_req.text
		sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

		filtr=sub_soup.find_all('table',cellpadding='0',align='center')
		for sub_filter in filtr:
			story = sub_filter.find_all('td', class_ = 'story')

			for paragraphs in story:
				p = paragraphs.find_all('p')
				for line in p:
					print line.text

		print "\n\n\n\n"

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == '-fp' or sys.argv[1] == '--frontpage':
			frontpage()
		elif sys.argv[1] == '-n' or sys.argv[1] == '--nation':
			getData('Nation')
		elif sys.argv[1] == '-f' or sys.argv[1] == '--foreign':
			getData('Foreign')
		elif sys.argv[1] == '-c' or sys.argv[1] == '--calcutta':
			getData('Calcutta')
		elif sys.argv[1] == '-b' or sys.argv[1] == '--bengal':
			getData('Bengal')
		elif sys.argv[1] == '-bsns' or sys.argv[1] == '--business':
			getData('Business')
		elif sys.argv[1] == '-s' or sys.argv[1] == '--sports':
			getData('Sports')
		else:
			print "Wrong Argument"
	else:
		print "Usage: python news.py [OPTIONS]"

if __name__ == "__main__":
	link_datasets()
	main()