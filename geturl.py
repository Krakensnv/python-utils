# Scrap url links from HTML file
from bs4 import BeautifulSoup
html = open("cplusplus.html").read()
soup = BeautifulSoup(html)
for a in soup.findAll('a'):
    print (a(['href'])
