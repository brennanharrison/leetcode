#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np

n = 234

u = list(str(n))

i = [int(x) for x in u]

r = np.prod(np.array(i)) 

print(r)

