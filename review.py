import requests
from bs4 import BeautifulSoup
from requests.api import request
import pandas as pd


url='https://www.amazon.in/Apple-iPhone-7-32GB-Black/product-reviews/B01LZKSVRB'

page=requests.get(url,timeout=10)
page.content

soup=BeautifulSoup(page.content,'html.parser')
#print(soup)

revname=soup.find_all('span',class_="a-profile-name")
#print(revname)

cust_name=[]

for item in range(0,len(revname)):
    cust_name.append(revname[item].get_text())

#print(cust_name)
cust_name.pop(0)
cust_name.pop(1)
print(cust_name)

title=soup.find_all('a',class_="review-title-content")
#print(title)


review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
#print(review_title)

review_title[:]=[titles.lstrip('\n') for titles in review_title]
review_title[:]=[titles.rstrip('\n') for titles in review_title]

print(review_title)

rating=soup.find_all('i',class_="review-rating")

product_rating=[]
for i in range(0,len(rating)):
    product_rating.append(rating[i].get_text())

product_rating.pop(0)
product_rating.pop(1)

print(product_rating)

review_content=soup.find_all('span',class_="review-text-content")

review_content1=[]

for i in range(0,len(review_content)):
    review_content1.append(review_content[i].get_text())

review_content1[:]=[titles.lstrip('\n') for titles in review_content1]
review_content1[:]=[titles.rstrip('\n') for titles in review_content1]

print(review_content1)

# converting data into dataframes

df=pd.DataFrame()

df['Customer Name']=cust_name
df['Title']=review_title
df['Ratings']=product_rating    
df['Reviews Content']=review_content1



df.to_csv(r"C:\Users\Acer\Documents\WebScraping\reviews.csv", index=True)

print(df)

page.close()