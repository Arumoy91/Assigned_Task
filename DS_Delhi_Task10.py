#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[3]:


from selenium import webdriver


# In[4]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[5]:


driver.get(r'https://www.monsterindia.com/')


# In[6]:


search_job=driver.find_element_by_id('SE_home_autocomplete')
search_job.send_keys("Data Scientist")
search_location=driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']")
search_location.send_keys("Delhi")


# In[7]:


url="https://www.monsterindia.com/srp/results?query=Data%20Scientist&locations=Delhi"


# In[8]:


driver.get(url)

