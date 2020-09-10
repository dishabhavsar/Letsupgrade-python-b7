#!/usr/bin/env python
# coding: utf-8

# # BATCH 7 DAY 3 ASSIGNMENT

# Question 1

# In[ ]:


for altitude in range(1000,10000):
    altitude=int(input('enter altitude'))
    if altitude ==1000:
        print('plane is safe to land')
    elif altitude > 1000 and altitude < 5000:
        print('bring the plane down to 1000 ft')
    else:
        print('turn around and try later')


# Question 2

# In[1]:


num1 = 0
num2 = 200
for n in range(num1, num2 + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n) 


# In[ ]:




