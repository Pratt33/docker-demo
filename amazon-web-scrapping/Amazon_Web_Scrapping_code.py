#importing python libraries for making dataset, for scrapping, for requesting information
import pandas as pd
from bs4 import BeautifulSoup
import requests

#storing scrapping link in url
url='https://www.amazon.in/s?bbn=1389396031&rh=n%3A976419031%2Cn%3A1389375031%2Cn%3A1389396031%2Cn%3A15747864031&dc&qid=1708977151&rnid=1389396031&ref=lp_1389396031_nr_n_0'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

#giving headers will tell receiver that information fetcher is not bot or robot
webpage=requests.get(url, headers=headers).text

#soup for reading html code
soup=BeautifulSoup(webpage, 'html.parser')

#getting one main wrapper pocket in which all the information is stored
product=(soup.find_all('div', class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small'))

#creating empty list for storing various parameters
name=[]
rating=[]
recent_sell=[]
price=[]
peoples=[]


#running loop to ieterate over each wrapper poket to fetch information from each one
#again appending them into empty lists
for i in product:
    name.append(i.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip())
    rating.append(i.find('span', class_='a-icon-alt').text.strip())
    recent_sell.append(i.find('span', class_='a-size-base a-color-secondary').text.strip())
    price.append(i.find('span', class_='a-price-whole').text.strip())
    peoples.append(i.find('span', class_='a-size-base s-underline-text').text.strip())

#creating dictionary to store obtained information
d={'Name of Product':name, 'Price':price, 'Ratings':rating, 'Total Users':peoples, 'Recentnly Purchased':recent_sell}

#using pandas for making dataframe of information 
df=pd.DataFrame(d)

#displaying final result
#print(df)

#creating csv file
df.to_csv('Amazon_Televisions.csv', index=False)
print(pd.read_csv('Amazon_Televisions.csv'))