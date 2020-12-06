#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


from selenium import webdriver


# In[3]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[4]:


driver.get(r'https://www.monsterindia.com/')


# In[5]:


search_job=driver.find_element_by_id('SE_home_autocomplete')
search_job.send_keys("Software Developer")


# In[6]:


url="https://www.monsterindia.com/srp/results?query=Software%20Developer"


# In[7]:


driver.get(url)


# In[ ]:




