import fbchat, random
from init import initializeUser

'''
Set up a listener which reacts to specific messages sent to the bot
'''

# Login and establish connection to a room
session, user = initializeUser()
# Set up a listener (for listening for messages and other chat events)
listener = fbchat.Listener(session=session, chat_on=False, foreground=False)
# Set up a client (for example for sending files)
fb_client = fbchat.Client(session=session)

# Send an image file to the room
# WARNING: A correct MIME type needs to be specified as the third argument
# of the list in fb_client_upload() function!
def sendFile():
    with open('files/hello.png') as file:
        file = fb_client.upload([('image.png', file, 'image/png')])
    user.send_files(file)

# Send a random quote from a list of quotes
# It might be a good idea to pull such data from a database,
# for example a MongoDB instance (snippets for such use case)
# are awailable in the /mongodb directory
def sendQuote():
    quotes = [
        'Quote one',
        'Quote two',
        'Quote three'
    ]
    return random.choice(quotes)

# Main listener logic
for event in listener.listen():
    if isinstance(event, fbchat.MessageEvent):
        if event.author.id != session.user.id:
            if ('hello' in event.message.text):
                user.send_text('hello')
            elif (event.message.text == '!file'):
                sendFile()
            elif (event.message.text == '!quote'):
                user.send_text(sendQuote())
