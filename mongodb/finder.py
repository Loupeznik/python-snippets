#!/usr/bin/python3
import pymongo
import random

'''
Read data from collection
'''

uri = 'mongodb+srv://user:password@host'
client = pymongo.MongoClient(uri)

# Get a random record from a collection and read it's 'attr' field
def getContent():
    collection = client.collectionname
    content = list(collection.find())
    return random.choice(content)["attr"]
