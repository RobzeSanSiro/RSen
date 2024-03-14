#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict = {'name':'Robin','age':27,'city':'London'}

print("Name:", my_dict['name'])
print("Age: ", my_dict['age'])
print("City: ", my_dict['city'])

my_dict['gender'] = 'male'

my_dict['age'] = 28

del my_dict['city']

for key,value in my_dict.items():
    print(key,": ",value)


# In[ ]:




