#!/usr/bin/env python
# coding: utf-8

# # List and its function

# In[2]:


lst= ['Disha',27,54.60,[5,6,7]]
lst


# In[7]:


lst.append('abc')
lst


# In[8]:


lst[0]


# In[10]:


lst.count('abc')


# In[11]:


lst.index(27)


# In[12]:


lst.remove('abc')


# In[13]:


lst


# In[18]:


lst.pop(1)
lst


# # Dictionary and its functions

# In[19]:


dit={"name":"disha","age":"21","blood group":"o+ve"}
dit


# In[21]:


dit.get('age')


# In[23]:


dit.keys()


# In[24]:


dit.items()


# In[25]:


dit.pop('age')


# In[26]:


dit


# # Sets

# In[27]:


s={2,4,"Disha","abc",8,5,5,9}
s


# In[28]:


s.copy()


# In[29]:


s1={2,'abc'}
s1


# In[30]:


s1.issubset(s)


# In[31]:


s.intersection(s1)


# # tuples

# In[32]:


t=('disha','bhavsar','@','gmail.com')
t


# In[33]:


t.count('@')


# In[34]:


t.index('@')


# # strings

# In[35]:


name="disha"
type(name)


# In[37]:


name1="bhavsar"
type(name1)


# In[40]:


name + " " + name1


# In[ ]:




