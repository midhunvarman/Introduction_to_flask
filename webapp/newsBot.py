import requests
from bs4 import BeautifulSoup

def newsScraper(link,keywords):
  markup = requests.get(link).text
  soup = BeautifulSoup(markup, 'html.parser')
  links = soup.findAll('a', limit=170)
  saved_links = []
  saved_linksTexts = []
  for link in links:
    for keyword in keywords:
      if keyword in link.text:
        saved_links.append(link)
  for link in saved_links:
    saved_linksTexts.append(link.text)

  return saved_links,saved_linksTexts

links,linksTexts = newsScraper('https://economictimes.indiatimes.com/news/coronavirus',['Coronavirus','pandemic','COVID-19','infection','Wuhan'])

print(linksTexts)
