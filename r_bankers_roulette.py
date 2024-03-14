#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

names_string = "Robin,Harry,Zayn"

names = names_string.split(",")

num_items = len(names)
random_choice = random.randint(0,num_items-1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " will pay the bill...")


# In[ ]:




