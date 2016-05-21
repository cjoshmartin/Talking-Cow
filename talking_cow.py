import os #make calls to OS
from gtts import gTTS # package from google's TTS api

file_name ="output_audio.mp3" #file name of audio file

#gits users input
user_input = raw_input("What would you like the cow to say? ") #prompts user for input
output_string ="Cow says '" + str(user_input) +"'."

os.system('cowsay ' + user_input) #grenates a cow

#makes text to speech and save to mp3
tts =gTTS(text=output_string, lang ='en') #imports text into google's API
tts.save(file_name) #creates audio file


os.system('mpg321 '+ file_name) #plays audio using the command line and mpg321



