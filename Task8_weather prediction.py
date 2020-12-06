#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


from selenium import webdriver


# In[3]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[4]:


driver.get(r'https://www.weather.gov/')


# In[5]:


driver.get(r'https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.X8zgZ9gzZPY')


# In[6]:


url='https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.X8zgZ9gzZPY'


# In[7]:


driver.get(url)

