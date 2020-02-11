#!/usr/bin/env python
# coding: utf-8

# In[14]:


nums = [12,345,2,6,7896]


x=0
for i in nums:
    if len(str(i))%2==0:
        x+=1
    else:
        continue
        
print(x)

