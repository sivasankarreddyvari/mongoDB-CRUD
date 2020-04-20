# mongoDB-CRUD
This repository contains mongoDB CRUD operations with Python

MongoDB Atlas NoSQL Database Access
a. Create a Mongo DB Atlas account
b. Create a cluster and Load some sample data
c. Load the JSON code you created in homework 2 into MongoDB
d. Using any programming langue to create an application to connect the Mongo Atlas account
e.  Show MongoDB CRUD Operations with sample data in your code


Step1: Created a Mongo DB Atlas account on cloud:

![alt text](Outputs/pic1.png "Description goes here")

Step2: Created cluster and loaded sample data as below:

![alt text](Outputs/pic2.png "Description goes here")

Step3:Created database called ‘ucmo’ and created collection ‘patients_sample’ and loaded sample data which is created in assignment 2 via shell.

![alt text](Outputs/pic3.png "Description goes here")

Loaded sample data from patients_sample collection showing on cloud mongo (GUI)

![alt text](Outputs/pic4.png "Description goes here")

Step4:
4.1. Install Python3.7 (via Anaconda3), pymongo19.0,
Python is the programming language which will be installed on the machine and on top of that different IDEs and packages can be installed. Anaconda installs IDEs and several important packages like NumPy, Pandas, and so on, and this is a really convenient package. I am using jupyter here.

![alt text](Outputs/pic5.png "Description goes here")

4.2. Create database and collection on mongoDB atlas

![alt text](Outputs/pic6.png "Description goes here")

4.3. Connect to mongoDB database via python(using connection string from mongoDB atlas)

![alt text](Outputs/pic7.png "Description goes here")

Connecting to mongoDB using above connection string from python:

![alt text](Outputs/pic8.png "Description goes here")

Step5: MongoDB CRUD Operations with sample data:
5.1. Insert documents into patients collection
  5.1.1 Insert single document into patients collection as shown below:
  Code executing from python:

![alt text](Outputs/pic9.png "Description goes here")

  5.1.2. Insert multiple documents into patients collection as shown below:
  Code executing from python:
  
  ![alt text](Outputs/pic10.png "Description goes here")
  
  
    Output on mongoDB atlas:
   ![alt text](Outputs/pic11.png "Description goes here")
   
  5.2. listing documents from patients collection.
  5.2.1 Find all documents from patients collection

![alt text](Outputs/pic12.png "Description goes here")

  5.2.2. Find single document from patients collection
  
  ![alt text](Outputs/pic13.png "Description goes here")
  
  5.3. Update documents from patients collection
  5.3.1. Update single document from patients collection

  ![alt text](Outputs/pic14.png "Description goes here")
  
    5.3.2. Update multiple documents from patients collection
    
    ![alt text](Outputs/pic15.png "Description goes here")
    
    Output from mongoDB atlas:
  
    ![alt text](Outputs/pic16.png "Description goes here")
    
    5.4. Delete documents from patients collection
  5.4.1. Delete single document from patients collection
  Code executing from python:

    ![alt text](Outputs/pic17.png "Description goes here")
    
      5.4.2. Delete multiple document from patients collection
      
      ![alt text](Outputs/pic18.png "Description goes here")

![alt text](Outputs/pic19.png "Description goes here")



