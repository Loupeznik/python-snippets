import fbchat
import logging

'''
Initializes chatbot instance via fbchat library
'''

# Set chatroom and Facebook credentials
room = '' # ID of the chatroom (for instance '100000938XXXX46')
username = '' # Username for the bot's Facebook account
password = '' # Password for the bot's Facebook account

# Setup logging
logging.basicConfig(filename='/tmp/fb-chatbot.log', level=logging.INFO)

# Chat with a specific user
def initializeUser():
    session = fbchat.Session.login(username,  password)
    user = fbchat.User(session=session, id=room)
    
    return session, user

# Chat with a specific group
def initializeGroup():
    session = fbchat.Session.login(username,  password)
    group = fbchat.Group(session=session, id=room)

    return session, group
