#!/usr/bin/env python
# coding: utf-8

# # Day 4 Assignment

# In[1]:


num1 = 1042000
num2 = 702648265

for num in range(num1, num2 + 1):
    order = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    if num == total:
        print(num)
        break


# In[ ]:




