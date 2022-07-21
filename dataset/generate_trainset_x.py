#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = []
l+=[1]
l+=[2]
print(l)


# In[6]:


import numpy as np

def generate(n):
    index = np.array(range(1,n+1))
    names = []
    for i in index:
        str_build = "img (" + str(i) + ")"
        names += [str_build]
    return names


# In[7]:


names = generate(4)
print(names)


# In[ ]:




