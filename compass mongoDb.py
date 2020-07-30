# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:25:32 2020

@author: Kahar's
"""

import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Employee']
information = mydb.Employee

record = [{
    "firstname":"Ankit",
    "lastname":"Prasad",
    "age":"11",
    "phone":8759444991,
    "location":"Bangalore"
    },{
    "firstname":"Aniket",
    "lastname":"Paddu",
    "age":"31",
    "location":"Kolkata"
    },{
    "firstname":"Sadguru",
    "lastname":"Choubey",
    "age":"41",
    "location":"Barcelona"
    }]

information.insert_many(record)

#for finding the First One in the DB
information.find_one()

for record in information.find():
    print(record)
    
for record in information.find({'firstname':'Ankit','lastname':'Prasad'} ):
    print(record)    

#name in type query     
for record in information.find({ "firstname":{'$in':['Aniket','Ankit']},"lastname":"Paddu"}):
    print(record) 
        
    
#age greater than query    
for record in information.find({ "lastname":"Paddu","age":{'$lt':'35'}}):
    print(record) 
        
    information.update_one(filter, update)
  information.update_one({'firstname':'Ankit'},{'$inc':{'lastname':'King'},'$currentDate':{'last Modified':True}})      