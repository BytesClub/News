import sys
import bs4 as bs
import requests

base_url = 'https://www.telegraphindia.com/'

def frontpage():
	req = requests.get(base_url)
	html = req.text
	soup = bs.BeautifulSoup(html, 'lxml')

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



def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == '-fp' or '--frontpage':
			frontpage()
	else:
		print "Usage: python news.py [OPTIONS]"

if __name__ == "__main__":
	main()