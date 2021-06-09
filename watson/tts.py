from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import random, string

'''
Convert a textfile to an audio file via IBM Watson API
'''

# Setup Watson API access
authenticator = IAMAuthenticator('yourapikey')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('watson-instance-url')

# Parse textfile for TTS
text = open("test.txt", "r").read()

# Generate random filename for saving TTS result audio
file = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

# Actual TTS
with open('mp3/' + file + '.mp3','wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(text,voice='en-US_MichaelV3Voice',accept='audio/mp3').get_result().content)
