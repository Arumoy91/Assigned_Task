#!/usr/bin/env python
# coding: utf-8

# In[5]:


import selenium


# In[6]:


from selenium import webdriver


# In[7]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[8]:


driver.get(r'https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[9]:


url='https://www.icc-cricket.com/rankings/womens/team-rankings/odi'


# In[10]:


driver.get(url)


# In[11]:


driver.get(r'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[12]:


url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting'


# In[13]:


driver.get(url)


# In[14]:


driver.get(r'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling')


# In[15]:


url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling'


# In[16]:


driver.get(url)


# In[17]:


driver.close()

