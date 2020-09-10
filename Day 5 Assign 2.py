#!/usr/bin/env python
# coding: utf-8

# In[69]:


def isPrime(n):
    for i in range(2,n):
        if n % i ==0:
            return False
    else:
        return True


# In[70]:


isPrime(7)


# In[71]:


isPrime(8)


# In[72]:


pno = []


# In[73]:


lst = list(range(0,2500))


# In[74]:


for item in lst:
    if isPrime(item):
        pno.append(item)


# In[75]:


print(pno)


# In[76]:


lst_prime_no = filter(isPrime,lst)


# In[77]:


print(list(lst_prime_no))


# In[ ]:




