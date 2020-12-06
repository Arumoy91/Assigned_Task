#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install IMDbPY


# In[2]:


import imdb 


# In[3]:


ia = imdb.IMDb() 


# In[4]:


search = ia.get_top250_movies() 


# In[5]:


for i in range(100): 
    print(search[i]['title'])
    


# In[6]:


from bs4 import BeautifulSoup
import requests


# In[7]:


url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'


# In[8]:


page=requests.get(url)


# In[9]:


soup=BeautifulSoup(page.text,"html.parser")


# In[10]:


page.content


# In[11]:


print(soup.prettify())


# In[12]:


mov_list=soup.find('tbody',class_='lister-list').find_all('td',class_='titlecolumn')


# In[13]:


for i in mov_list:
    title.append(i.find('a').get_text())
    year.append(i.find('spam').get_text())


# In[14]:


rat_list=soup.find('tbody',class_='lister-list').find_all('td',class_='ratingColumn imdbRating')


# In[15]:


for i in mov_list:
    rating.append(i.find('b').get_text())
    rating.append(i.find('strong').get_text())


# In[16]:


year_list=soup.find('tbody',class_='lister-list').find_all('td',class_='secondaryInfo')


# In[17]:


for i in mov_list:
    year.append(i.find('c').get_text())
    year.append(i.find('span').get_text())


# In[18]:


page.content


# In[19]:


print(soup.prettify())


# In[20]:


for i in range(100): 
    print(search[i]['title'])


# In[ ]:




