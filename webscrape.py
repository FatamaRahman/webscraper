#import libraries
import urllib2
import gzip
import StringIO
from bs4 import BeautifulSoup

home_page = "http://billboardinsider.com/page/70/?s=company+of+the+day"

home_page_req = urllib2.Request(home_page)
home_page_response = urllib2.urlopen(home_page_req)
home_page_html = home_page_response.read()
try:
    home_page_data = StringIO.StringIO(home_page_html)
    home_gzip = gzip.GzipFile(fileobj=home_page_data)
    home_page_html = home_gzip.read()
except:
    pass
home_page_response.close()

home_soup = BeautifulSoup(home_page_html, 'html.parser')
aTags = home_soup.select('h2.entry-title a')
for a in aTags:
    print a.get('href')

# specify the url
    quote_page = a.get('href')

# query the website and return the html to the variable 'page'
    page = urllib2.Request(quote_page)
    response = urllib2.urlopen(page)
    html = response.read()
    try:
        data = StringIO.StringIO(html)
        gzipper = gzip.GzipFile(fileobj=data)
        html = gzipper.read()
    except:
        pass
    response.close()

# parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(html, 'html.parser')

# Take out the <div> of name and get its value
    pTags = soup.find('div', attrs={'class': 'pf-content'}).find_all('p')
    shouldBreak = False
    for p in pTags:
        if shouldBreak:
            break
        if 'Email' in p.text or 'Phone' in p.text or 'Company' in p.text or 'Markets' in p.text:
            print p.text

# name = name_box.text.strip() # strip() is used to remove starting and trailin
