#!/usr/bin/env python
# coding: utf-8

# In[41]:


nums = [1,2,3,4]

import itertools


x = 1
l = []

for i,j in zip(nums[:-1], nums[1:]):
    if x%2==1:
        x+=1
        u = [j for x in range(i)]
        l.append(u)
    else:
        x+=1
        continue
    

z = list(itertools.chain(*l))

print(z)

