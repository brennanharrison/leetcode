#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        import operator

        x = 0
        l = []

        for i in points[:-1]:
            t = list(map(operator.sub,points[x],points[x+1]))
            u = abs(max(t,key=abs))
            l.append(u)
            x+=1
            
        l = sum(l)
        
        return l

