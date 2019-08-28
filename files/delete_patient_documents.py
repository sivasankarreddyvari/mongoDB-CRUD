#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
client = MongoClient("mongodb+srv://sxr31390:avihsshiva@demo-byqmn.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db = client.get_database('ucmo')
records=db.patients
records.count_documents({})


# In[51]:


list(records.find())


# In[52]:


records.delete_one({"PID":10})


# In[53]:


list(records.find())


# In[54]:


myquery = { "Phone": {"$regex": "^8"} }
records.delete_many(myquery)


# In[55]:


list(records.find())


# In[ ]:




