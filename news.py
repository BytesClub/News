import sys
import bs4 as bs
import requests
from collections import defaultdict 

data = defaultdict(dict)
base_url = 'https://www.telegraphindia.com/'
req = requests.get(base_url)
html = req.text
soup = bs.BeautifulSoup(html, 'lxml')

def linkdataset():

        ulist=soup.find_all('ul',class_ ='nav nav-list')
        for lists in ulist:
    
            ulists=lists.find_all("li")
            for link in ulists:
        
                links=link.find_all("a")
                for linki in links:
                        
                    sub_url_text=linki.text
                    sub_url = 'https://www.telegraphindia.com/' + str(linki.get("href"))
                    data[sub_url_text]=sub_url

        
                    
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

def nation():
        url=data['Nation']
        req=requests.get(url)
        html=req.text
        soup=bs.BeautifulSoup(html,'lxml')

        nationstory=soup.find_all('td',class_ ='story')
        for links in nationstory:
                link=links.find('a')
                sub_url=url[:-9]+str(link.get('href'))
                sub_req = requests.get(sub_url)
                sub_html = sub_req.text
                sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

                filtr=sub_soup.find_all('table',cellpadding='0',align='center')
                for sub_filter in filtr:
                        
                        story = sub_filter.find_all('td', class_ = 'story')

                        for paragraphs in story:
                                p = paragraphs.find_all('p')
                                for i in p:
                                        print i.text
                print "\n\n\n\n"                

def international():
        url=data['Foreign']
        req=requests.get(url)
        html=req.text
        soup=bs.BeautifulSoup(html,'lxml')

        nationstory=soup.find_all('td',class_ ='story')
        for links in nationstory:
                link=links.find('a')
                sub_url=url[:-9]+str(link.get('href'))
                sub_req = requests.get(sub_url)
                sub_html = sub_req.text
                sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

                filtr=sub_soup.find_all('table',cellpadding='0',align='center')
                for sub_filter in filtr:
                        
                        story = sub_filter.find_all('td', class_ = 'story')

                        for paragraphs in story:
                                p = paragraphs.find_all('p')
                                for i in p:
                                        print i.text
                print "\n\n\n\n"             


def calcutta():
        url=data['Calcutta']
        req=requests.get(url)
        html=req.text
        soup=bs.BeautifulSoup(html,'lxml')

        nationstory=soup.find_all('td',class_ ='story')
        for links in nationstory:
                link=links.find('a')
                sub_url=url[:-9]+str(link.get('href'))
                sub_req = requests.get(sub_url)
                sub_html = sub_req.text
                sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

                filtr=sub_soup.find_all('table',cellpadding='0',align='center')
                for sub_filter in filtr:
                        
                        story = sub_filter.find_all('td', class_ = 'story')

                        for paragraphs in story:
                                p = paragraphs.find_all('p')
                                for i in p:
                                        print i.text
                print "\n\n\n\n"

def bengal():
        url=data['Bengal']
        req=requests.get(url)
        html=req.text
        soup=bs.BeautifulSoup(html,'lxml')

        nationstory=soup.find_all('td',class_ ='story')
        for links in nationstory:
                link=links.find('a')
                sub_url=url[:-9]+str(link.get('href'))
                sub_req = requests.get(sub_url)
                sub_html = sub_req.text
                sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

                filtr=sub_soup.find_all('table',cellpadding='0',align='center')
                for sub_filter in filtr:
                        
                        story = sub_filter.find_all('td', class_ = 'story')

                        for paragraphs in story:
                                p = paragraphs.find_all('p')
                                for i in p:
                                        print i.text
                print "\n\n\n\n"

def business():
        url=data['Business']
        req=requests.get(url)
        html=req.text
        soup=bs.BeautifulSoup(html,'lxml')

        nationstory=soup.find_all('td',class_ ='story')
        for links in nationstory:
                link=links.find('a')
                sub_url=url[:-9]+str(link.get('href'))
                sub_req = requests.get(sub_url)
                sub_html = sub_req.text
                sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

                filtr=sub_soup.find_all('table',cellpadding='0',align='center')
                for sub_filter in filtr:
                        
                        story = sub_filter.find_all('td', class_ = 'story')

                        for paragraphs in story:
                                p = paragraphs.find_all('p')
                                for i in p:
                                        print i.text
                print "\n\n\n\n"

def sports():
        url=data['Sports']
        req=requests.get(url)
        html=req.text
        soup=bs.BeautifulSoup(html,'lxml')

        nationstory=soup.find_all('td',class_ ='story')
        for links in nationstory:
                link=links.find('a')
                sub_url=url[:-9]+str(link.get('href'))
                sub_req = requests.get(sub_url)
                sub_html = sub_req.text
                sub_soup = bs.BeautifulSoup(sub_html, 'lxml')

                filtr=sub_soup.find_all('table',cellpadding='0',align='center')
                for sub_filter in filtr:
                        
                        story = sub_filter.find_all('td', class_ = 'story')

                        for paragraphs in story:
                                p = paragraphs.find_all('p')
                                for i in p:
                                        print i.text
                print "\n\n\n\n"


                

def main():
	if len(sys.argv) > 1:
                arg = sys.argv[1]
	        if arg == '--foreign':
                        international()
                elif arg == '--sports':
                        sports()
                elif arg == '--national':
                        national()
                elif arg == '--calcutta':
                        calcutta()
                elif arg == '--bengal':
                        bengal()
                elif arg == '--business':
                        business()
                elif arg == '-fp' or '--frontpage':
                        frontpage()
                else:
                        print "enter correct option"
                
	else:
		print "Usage: python news.py [OPTIONS]"

if __name__ == "__main__":
        linkdataset()
	main()
