import requests
from bs4 import BeautifulSoup


URL = 'https://www.codewithharry.com/'

r = requests.get(url=URL)

htmlcontent  =  r.content
# print(htmlcontent)


soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)


title = soup.title
# print(title)
# print(title.string)


paragraph = soup.find_all('p')
# print(paragraph)


anchor_tag = soup.find_all('a')
# print(anchor_tag)

all_link  = set()
for link in anchor_tag:
    if link != "#":
        linktext = "https://www.codewithharry.com" +link.get('href')
        all_link.add(linktext)
        # print(linktext)
        # print(link)


# print(soup.find('p'))   # to get the first para in page
# print(soup.find('p')['class'])
# print(soup.find('p')['id'])
# print(soup.find_all("p", class_="lead"))
# print(soup.find('p').get_text())
