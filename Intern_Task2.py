#!/usr/bin/env python
# coding: utf-8

# Task 1:

# In[1]:


from urllib.request import urlopen


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


html=urlopen('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


bs=BeautifulSoup(html,"html.parser")


# In[5]:


titles=bs.find_all(['h1','h2','h3','h4','h5','h6'])


# In[6]:


print('List all the header tags :', *titles, sep='\n\n')


# Task 2:

# In[7]:


from bs4 import BeautifulSoup
import requests
import re


# In[8]:


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


# In[9]:


movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []


# In[10]:


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


# In[11]:


for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])


# In[12]:


all_tables=soup.find_all("table")
all_tables


# In[13]:


right_table=soup.find('table')
right_table


# In[14]:


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
            
             
                


# In[15]:


import pandas as pd
df=pd.DataFrame(A,columns=['place'])

df['movie_title']=B
df['year']=C
df['Starring']=D
df['star_cast']=E

