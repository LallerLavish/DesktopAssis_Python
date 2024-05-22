import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 

engine=pyttsx3.init("nsss")
voices=engine.getProperty("voices")
print(len(voices))
engine.setProperty('voice',voices[80].id)
engine.setProperty('rate',150)
# adjusting the rate or speed of talk


def speak(text):
    """Text to Speech(return voice) Converter Function
    type of (args) is:
    String
    """
    engine.say(text)
    engine.runAndWait()



# speech recognition  function
def voice():
    """Voice to Text(return text) Converter Function"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        # The pause_threshold value is the number of seconds the system will take 
        # to recognize the voice after the user has completed their sentence.
        audio=r.listen(source)

        try:
            print("Recognizing ....")
            query=r.recognize_google(audio,language="en-in")
            print(f"User Said : {query}\n")
        except Exception as error:
            print("Say That Again Please")
            return "Say That Again Please"
    return query
text=voice()
speak(text)