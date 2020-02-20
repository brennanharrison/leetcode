#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        y = [len(list(filter(lambda u: (u < 0), x))) for x in grid]
        
        return sum(y)

