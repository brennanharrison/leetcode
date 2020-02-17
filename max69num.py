#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))

        if '6' not in num:
            x = ''.join(num)
        else:
            num.insert(num.index('6'),'9')
            num.pop(num.index('6'))
            x = ''.join(num)
    
        return x

