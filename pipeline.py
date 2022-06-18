import os
import speech_recognition as sr
import openai
from gtts import gTTS
from function_sound_file import function_sound
from datetime import datetime
import time
from scipy.io import wavfile
import sys
from sys import stdin
from os import isatty


# openai.api_key = "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"
openai.api_key = "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"

# print('\n\n\nWelcome to Remy AI :) Start your conversation by asking a question (Ctrl-C to quit):\n\n')

recorded_audio = sys.argv[1]
# print("Audio Input:", sys.argv[1])

'''
Step 1/2: User Speech Input, speech to text
'''
# audio_found = False
# #while(audio_found == False):
# with sr.Microphone() as source:
#     print("Speak Anything :")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         audio_found = True
#         print("You said : {}".format(text))
#     except:
#         print("Sorry could not recognize what you said\n\n")
#         text = ""
'''
READING IN .WAV FILE FROM GUI
'''
#filename = './user_output.wav'
filename = recorded_audio
#audio_data = sr.AudioFile('./user_output.wav')
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)




'''
Step 3: GPT-3 Response
'''
# if text == "":
#     continue

response = openai.Completion.create(
 engine="text-davinci-002",
 prompt=text,
 temperature=0.7,
 max_tokens=256,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0
)


GPT3_answer = response["choices"][0]["text"]

# print(GPT3_answer)
# print('\n')

'''
Step 4: GPT-3 text to audio
'''

cwd = os.getcwd()
if(os.path.exists(os.path.join(cwd, 'gpt3_responses'))):
    print("Directory exists")
else:
    os.mkdir(os.path.join(cwd, 'gpt3_responses'))
    print("Made directory")

language = 'en'
myobj = gTTS(text=GPT3_answer, lang=language, slow=False)
dt = datetime.today()
file_name_res = 'gpt3_responses/' + str(dt.timestamp()) + '.mp3'
myobj.save(file_name_res)
print(file_name_res)

# Option 1: play audio by opening mp3 windows application
#os.system("start welcome.mp3")
  
# Option 2: play audio directly from cmd prompt
#function_sound( file_name_res)
