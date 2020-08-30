import requests 
from bs4 import BeautifulSoup

# Print Data for cards
def printData(id, soup):
    title = soup.find(id="thumbnail_img_carte-vo-" + id).get_text()
    titleFr = soup.find(id="thumbnail_img_carte-fr-" + id).get_text()
    url = soup.find(id="thumbnail_img_carte-fr-" + id).get('href')
    print(title + " - " + titleFr + " => " + url)

# Get all card from edition
def getCardFromEdition(editionUrl):
    URL = editionUrl
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    f = open('workfile.html', 'w+', encoding="utf-8")
    f.write(soup.prettify())

    itemNumber = 1
    id = ""
    while True:
        id = "241-"+str(itemNumber)
        itemNumber+=1
        if(soup.find(id="thumbnail_img_carte-vo-" + id) == None):
            break
        printData(id, soup)

#getCardFromEdition("http://www.magiccorporation.com/gathering-cartes-edition-241-ikoria-la-terre-des-behemoths.html")

URL = "http://www.magiccorporation.com/gathering-cartes-edition.html"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.div['block'])


