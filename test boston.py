#!/usr/bin/env python
# coding: utf-8

# In[24]:


def bilangan(n):
    if n%15==0:
        print("Frontend Backend")
    elif n%5==0:
        print("Backend")
    elif n%3==0:
        print("Frontend")
    else:
        print(n)
[bilangan(n) for n in range(50)]


# In[ ]:




