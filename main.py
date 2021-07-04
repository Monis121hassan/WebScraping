import requests

from bs4 import BeautifulSoup

url ="https://www.codewithharry.com/"

# Get the HTML content from the site

r= requests.get(url)

htmlcontent=r.content

# parse the HTML content

soup=BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify())

# scraping all the html paragraphs in the site

paras=soup.find_all('p')
#print(paras)


#print(soup.find('p')['class']) # provides the first element alon with the class

# to find the all the elements that has a class as lead

   #print(soup.find_all('p',class_='lead'))

#print(soup.find('p').get_text()) # returns the first paragraph with only text

# scraping all the html anchors in the site
anchors=soup.find_all('a')
all_link=set()
#print(anchors)
for link in anchors: 
    if(link.get('href')!= '#'):         # return all the links in an html page
        all_link.add("https://www.codewithharry.com/" +link.get('href'))
#print(all_link)

navbarcontent=soup.find(id='navbarSupportedContent')
#for elem in navbarcontent.stripped_strings:
    #print(elem)

#for item in navbarcontent.parents:  # to find the parent of the tags    parents: it will return as a generator so it can be iterate 
    #print(item.name)

#print(navbarcontent.previous_sibling)

# CSS selector

elemt=soup.select('.modal-footer')
print(elemt)
