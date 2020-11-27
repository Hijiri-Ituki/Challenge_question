#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


a = "Arizona: 479,501,870. California: 209,213,650."


# In[3]:


b = re.findall("\d",a,re.IGNORECASE)


# In[4]:


print(b)


# In[ ]:





# In[ ]:




