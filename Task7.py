#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


from selenium import webdriver


# In[3]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[4]:


driver.get(r'https://www.amazon.in/')


# In[5]:


driver.get(r'https://www.amazon.in/s?k=mobile+phone+under+20000+rupees&i=electronics&crid=3TYHX1OYXCV4V&sprefix=mobiles+phones+under+20000%2Caps%2C372&ref=nb_sb_ss_i_2_26')


# In[6]:


url='https://www.amazon.in/s?k=mobile+phone+under+20000+rupees&i=electronics&crid=3TYHX1OYXCV4V&sprefix=mobiles+phones+under+20000%2Caps%2C372&ref=nb_sb_ss_i_2_26'


# In[7]:


driver.get(url)

