#!/usr/bin/python3
from mysql import connect, actions

'''
Basic usage example for modules in /mysql directory
'''

connection = connect.connect('localhost', 'test', 'test', 'test')

actions.insert(connection, 'test')
actions.update(connection, 'test', 2)
print(actions.select(connection, 'test'))
actions.delete(connection, 'test', 1)

connection.close()
