import sys
import bs4 as bs
import requests
from collections import defaultdict
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

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
                print (td.text)
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
                                print (i.text)
                print "\n\n\n\n"

def getData(category,c):
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
                                frame1 = Frame(0, 0, 8*inch, 8*inch, showBoundary=1)
                                styles = getSampleStyleSheet()
                                for line in p:
                                        print line.text
                                        story = [Paragraph(str(line.text.encode('utf-8')), styles['Normal'])]
                                        story_inframe = KeepInFrame(8*inch, 8*inch, story)
                                        frame1.addFromList([story_inframe], c)
                                        
                c.showPage()            

                print "\n\n\n\n"
        c.save()        

def main(c):
        if len(sys.argv) > 1:
                if sys.argv[1] == '-fp' or sys.argv[1] == '--frontpage':
                        frontpage()
                elif sys.argv[1] == '-n' or sys.argv[1] == '--nation':
                        getData('Nation',c)
                elif sys.argv[1] == '-f' or sys.argv[1] == '--foreign':
                        getData('Foreign',c)
                elif sys.argv[1] == '-c' or sys.argv[1] == '--calcutta':
                        getData('Calcutta',c)
                elif sys.argv[1] == '-b' or sys.argv[1] == '--bengal':
                        getData('Bengal',c)
                elif sys.argv[1] == '-bsns' or sys.argv[1] == '--business':
                        getData('Business',c)
                elif sys.argv[1] == '-s' or sys.argv[1] == '--sports':
                        getData('Sports',c)
                else:
                        print "Wrong Argument"
        else:
                print "Usage: python news.py [OPTIONS]"

if __name__ == "__main__":
        link_datasets()
        c = canvas.Canvas("todaynews"+sys.argv[1]+".pdf")
        main(c)
