from gtts import gTTS

import os

f=open('1.text')
x=f.read()

# with open('1.text', 'r', encoding='utf-8') as file:
#     text = file.read()

# Define the language as Hindi
language = 'en'

audio = gTTS(text,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")


