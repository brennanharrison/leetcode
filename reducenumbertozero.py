#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = 123

x=0

while num!=0:
    if num%2==0:
        num=num/2
        x+=1
    else:
        num=num-1
        x+=1
        
print(x)

