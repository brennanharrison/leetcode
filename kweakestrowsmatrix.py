#!/usr/bin/env python
# coding: utf-8

# In[37]:


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

k = 3

f = {}
e = []
o = 0

for i in mat:
    count = sum(map(lambda x: x == 1, i))
    f[o] = count
    count = 0
    o+=1
    
u = {k: v for k, v in sorted(f.items(), key=lambda item: item[1])}

for i in list(u)[0:k]:
    e.append(i)
    
print(e)


# In[ ]:




