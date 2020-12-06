#!/usr/bin/env python
# coding: utf-8

# In[5]:


import selenium


# In[6]:


from selenium import webdriver


# In[7]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[8]:


driver.get(r'https://bookpage.com/reviews')


# In[9]:


url='https://bookpage.com/reviews'


# In[10]:


driver.get(url)


# In[11]:


driver.get('https://bookpage.com/reviews/25633-john-grisham-time-mercy-mystery-suspense#.X8zj49gzZPY')


# In[12]:


url='https://bookpage.com/reviews/25633-john-grisham-time-mercy-mystery-suspense#.X8zj49gzZPY'


# In[13]:


driver.get(url)


# In[14]:


driver.get('https://bookpage.com/reviews/25710-homeira-qaderi-dancing-mosque-nonfiction#.X8zkRNgzZPY')


# In[15]:


url='https://bookpage.com/reviews/25710-homeira-qaderi-dancing-mosque-nonfiction#.X8zkRNgzZPY'


# In[16]:


driver.get(url)


# In[17]:


driver.get('https://bookpage.com/reviews/25507-alyssa-cole-when-no-one-watching-mystery-suspense#.X8zkbNgzZPY')


# In[18]:


url='https://bookpage.com/reviews/25507-alyssa-cole-when-no-one-watching-mystery-suspense#.X8zkbNgzZPY'


# In[19]:


driver.get(url)


# In[20]:


driver.get('https://bookpage.com/reviews/25740-lisa-feldman-barrett-seven-half-lessons-about-brain-nonfiction#.X8zk5tgzZPY')


# In[21]:


url='https://bookpage.com/reviews/25740-lisa-feldman-barrett-seven-half-lessons-about-brain-nonfiction#.X8zk5tgzZPY'


# In[22]:


driver.get(url)


# In[23]:


driver.get('https://bookpage.com/reviews/25715-ijeoma-oluo-mediocre-nonfiction#.X8zlQtgzZPY')


# In[24]:


url='https://bookpage.com/reviews/25715-ijeoma-oluo-mediocre-nonfiction#.X8zlQtgzZPY'


# In[25]:


driver.get(url)

