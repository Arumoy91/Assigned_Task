#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imdb 


# In[2]:


ia = imdb.IMDb() 


# In[3]:


search = ia.get_top250_movies() 


# In[4]:


import selenium


# In[5]:


from selenium import webdriver


# In[6]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[7]:


driver.get(r'https://www.imdb.com/india/top-rated-indian-movies/')


# In[8]:


url='https://www.imdb.com/india/top-rated-indian-movies/'


# In[9]:


driver.get(url)


# In[10]:


from bs4 import BeautifulSoup
import requests
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")


# In[11]:


page.content


# In[12]:


print(soup.prettify())


# In[13]:


mov_list=soup.find('tbody',class_='lister-list').find_all('td',class_='titlecolumn')


# In[14]:


for i in mov_list:
    title.append(i.find('a').get_text())
    year.append(i.find('spam').get_text())


# In[15]:


rat_list=soup.find('tbody',class_='lister-list').find_all('td',class_='ratingColumn imdbRating')


# In[16]:


for i in mov_list:
    rating.append(i.find('b').get_text())
    rating.append(i.find('strong').get_text())


# In[17]:


year_list=soup.find('tbody',class_='lister-list').find_all('td',class_='secondaryInfo')


# In[18]:


for i in mov_list:
    year.append(i.find('c').get_text())
    year.append(i.find('span').get_text())


# In[19]:


url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
import re


# In[20]:


movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []


# In[21]:


for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)


# In[22]:


for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])
    


# In[23]:


all_tables=soup.find_all("table")
all_tables


# In[24]:


right_table=soup.find('table')
right_table


# In[25]:


A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll('tr'):
    cells=row.find_all('td')
    if len(cells)==5:
        e=cells[1].find(text=True)
        if e!='Not Assigned\n':
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            


# In[26]:


import pandas as pd
df=pd.DataFrame(A,columns=['place'])

df['movie_title']=B
df['year']=C
df['Starring']=D
df['star_cast']=E


# In[ ]:




