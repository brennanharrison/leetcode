#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
    
        while head:
            binary.append(head.val)
            head = head.next

        x = 0
        binary=binary[::-1]

        for i, e in list(enumerate(binary)):
            if e == 1:
                x = x + 2**i
        
        return x

