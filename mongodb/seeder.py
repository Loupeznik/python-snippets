#!/usr/bin/python3
import pymongo

'''
Read a text file and seed it's contents into a collection
'''

uri = 'mongodb+srv://user:password@host'
client = pymongo.MongoClient(uri)
collection = client.collectionname

# Insert one record into the collection
def seed(content, category):
    collection.insert_one(
        {
            "category": category,
            "content": content
        }
    )

file = open('test.txt', 'r').read().splitlines()

# Seed file contents
for item in file:
    seed(item, 'test')
