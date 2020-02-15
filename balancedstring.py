#!/usr/bin/env python
# coding: utf-8

# In[20]:


x = 0
rc = 0
lc = 0

for i in s:
    if rc == lc and (rc>0 and lc>0):
        x+=1
        rc=0
        lc=0
        
    if i == 'R':
        rc+=1
    else:
        lc+=1
        
if rc == lc and (rc>0 and lc>0):
    x+=1
    

