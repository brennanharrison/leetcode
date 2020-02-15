#!/usr/bin/env python
# coding: utf-8

# In[3]:


J = "z" 
S = list("ZZ")


t = 0

for i in J:
    t = t + S.count(i)
    
print(t)

