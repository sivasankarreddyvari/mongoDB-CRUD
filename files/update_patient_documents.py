#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
client = MongoClient("mongodb+srv://sxr31390:avihsshiva@demo-byqmn.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db = client.get_database('ucmo')
records=db.patients
records.count_documents({})


# In[68]:


list(records.find())


# In[73]:


update = {"Name" : "Kiran Updated", "Phone": "8123123123"}
records.update_one({"PID":13}, {'$set':update})


# In[74]:


records.find_one({"PID":13})


# In[75]:


update = {"Name" : "Ravi Updated", "Phone": "8876876876"}
records.update_one({"PID":12}, {'$set':update})


# In[76]:


records.find_one({"PID":12})


# In[77]:


myquery = { "Phone": { "$regex": "^9" } }
newvalues = { "$set": { "Name": "Name Updated" } }
records.update_many(myquery, newvalues)


# In[78]:


list(records.find())


# In[ ]:




