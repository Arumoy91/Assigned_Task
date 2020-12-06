#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


import pandas as pd


# In[3]:


from selenium import webdriver


# In[4]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[5]:


driver.get(r'https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[6]:


url='https://www.icc-cricket.com/rankings/mens/team-rankings/odi'


# In[7]:


driver.get(url)


# In[8]:


driver.get(r'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')


# In[9]:


url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'


# In[10]:


driver.get(url)


# In[11]:


driver.get(r'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[12]:


url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'


# In[13]:


driver.get(url)


# In[14]:


driver.close()

