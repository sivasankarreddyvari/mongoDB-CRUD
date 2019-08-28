#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
client = MongoClient("mongodb+srv://sxr31390:avihsshiva@demo-byqmn.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db = client.get_database('ucmo')
records=db.patients
records.count_documents({})


# In[9]:


list(records.find())


# In[10]:


records.find_one({"PID":11})


# In[11]:


records.find_one({"Name":"Muni"})


# In[ ]:




