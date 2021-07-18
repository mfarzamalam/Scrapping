import requests
from bs4 import BeautifulSoup
import re
from bs4.element import NavigableString

base = open("Alice_in_wonderland.html", "r")
output = open("learning_BeautifulShop.html", "w")

# Converting the document in html file and then convert it into another file
soup = BeautifulSoup(base, "html.parser")
# output.write(soup.prettify())     -less

# print the title
result = soup.title

# print the tag of title
result = soup.title.name

# print the text of title
result = soup.title.string

# print the first p in the document
result = soup.p

# print all the p in documents
result = soup.find_all('p')

# print the class of first p in the document
result = soup.p['class']

# print the first anchor tag in the document 
result = soup.a

# print the all anchor tag in the document
result = soup.find_all('a')

# print the single element with having the id in the document
result = soup.find(id="link3")

# extracting all the URLs found within a page with <a> tags
for link in soup.find_all('a'):
    result = link.get('href') + "\n"

# print all the text from a page
result = soup.get_text()

# print the first bold tag in the document
result = soup.b

# print the type of the tag
result = type(result)

# print the name of the tag
result = soup.p.name

# change the tag name
result = soup.p.name
result = 'blockquote'

# print element all attributes using dictionary
result = soup.a.attrs

# add and modify a tag’s attributes.
result['class'] = ['sister', 'sister1']
result['name']  = "Elsie"
result['value'] = 47

# remove a tag's attributes.
del result['value']
# result = result['value']
    # or
result = result.get('value')

# Multi-valued attributes¶
result = soup.a['class']

# changing tag value
result = soup.a['class']
soup.a['class'] = ['sister2', 'sister3']
result = soup.a

# String in a tag
result = soup.p.string

# replace a string with new string
footer = "Here's the footer coming from a script\n"
soup.find(text="Footer is missing").replace_with(footer)
result = soup.prettify()

# A tag’s children are available in a list called .contents:
result = soup.find('p').contents
# print(len(result))
# result = soup.find('p').contents[0]
# result = soup.find('p').contents[1]
# result = soup.find('p').contents[2].contents
# result = soup.find('p').contents[4].name

# print a sting in a tag using .children method
for child in soup.find('title').children:
    result = child

# count the first generation of child only. space is also consider child
result = len(list(soup.find('a').children))

# count all the generations of child. space is also consider child
result = len(list(soup.find('p').descendants))

# if a child tag has strings only and no other tags and attrs. then parent tag can access the same string
result = soup.head.contents
result = soup.head.string

# convert all the document in a string with whitespaces
for string in soup.strings:
    result = repr(string)

# convert all the document in a string and remove whitespaces
for string in soup.stripped_strings:
    result = repr(string)

# .parent tag get first generation upward
result = soup.title.string.parent

# .parents tag get all the generation upward
result = soup.a
for all_parents in result.parents:
    result = all_parents.name+"\n"

# siblings of the same parent
result = soup.a.next_sibling.next_sibling
result = soup.a.previous_sibling.previous_sibling

# iteration on siblings
for sibling in soup.find(id='link3').previous_siblings:
    result = repr(sibling)

# next_element and previous_element 
result = soup.find(id='link3').next_element.next_element.next_element.next_element
result = soup.find(id='link3').previous_element.previous_element.previous_element.previous_element.previous_element

# find_all method with regular expression
result = soup.find_all('b')

for tag in soup.find_all(re.compile("^b")):     # regular expression for a letter start with b
    result = tag.name+"\n"

for tag in soup.find_all(re.compile("t")):
    result = tag.name+"\n"

# find_all method with a list
result = soup.find_all(["a", "p"])

# passing true argument in find_all will give all the tag in the document
for tag_name in soup.find_all(True):
    result = tag_name.name+"\n"

# declaring custom function for more personalize results
def has_class_not_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

result = soup.find_all(has_class_not_id)

# function that search for all the href in document with regular expression
def ignore_elsie(href):
    return href and not re.compile("elsie").search(href)

result = soup.find_all(href=ignore_elsie)

# A function that returns True if a tag is surrounded by string objects  -  not working properly
def return_tag_with_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(return_tag_with_strings):
    result = str(tag.name)+"\n"

# find all the tags with href
result = soup.find_all(href=True)

# using dictionary to find the attr in tags
result = soup.find_all(attrs={'name':'Elsie'})

# search with class
result = soup.find_all("a", class_="sister")

def has_six_character(styling):
    return styling is not None and len(styling) == 6

result = soup.find_all(class_=has_six_character)
result = soup.select("sister3.sister2")

# search with strings
result = soup.find_all(string="Elsie")
result = soup.find_all(string=re.compile("Dormouse"))
result = soup.find_all("a", string=re.compile("Lacie"))

# Limit the results
result = soup.find_all("a", limit=2)

# find parents of first generation and upwards
result = soup.find(string="Lacie").find_parent().find_parent()
result = soup.find(string="Lacie").parent.parent

# find children of first generation and downwords
result = soup.a.find_next_siblings()
result = soup.find("a", id="link3").find_previous_siblings()
link   = soup.a
for tag in link.next_siblings:
    result = str(tag)+"\n"

# find single and all the elements next
result = soup.a.find_all_next()
result = soup.a.find_all_next(string=True)
result = soup.a.find_next()
result = soup.a.find_next(string=True)
result = soup.a.find_next("p")

result = soup.a.find_all_previous()
result = soup.a.find_all_previous(string=True)
result = soup.a.find_previous()
result = soup.a.find_previous(string=True)
result = soup.find("a", id="link3").find_all_previous("p")
output.write(str(result))