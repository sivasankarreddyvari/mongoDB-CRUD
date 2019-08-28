#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pymongo import MongoClient
client = MongoClient("mongodb+srv://sxr31390:avihsshiva@demo-byqmn.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db = client.get_database('ucmo')
records=db.patients
records.count_documents({})


# In[15]:


patients_data={"PID":10, "Name":"Logesh","Phone":"9132287771","Email":"logesh@gmail.com","Username":"logesh","Password":"l12345"}
records.insert_one(patients_data)


# In[16]:


list(records.find())


# In[17]:


insert_many=[{"PID":11,"Name":"Muni","Phone":"9135085555","Email":"muni@gmail.com","Username":"muni","Password":"muni12345"},
{"PID":12, "Name":"Ravi","Phone":"9132384444","Email":"ravi@gmail.com","Username":"ravi","Password":"ravi12345"},
{"PID":13, "Name":"Kiran","Phone":"9132386444","Email":"kiran@gmail.com","Username":"kiran","Password":"kiran12345"}]
records.insert_many(insert_many)


# In[18]:


list(records.find())


# In[ ]:




