#!/usr/bin/python3

import speech_recognition as sr
import webbrowser

class VoiceAssitance():
    def __init__(self):
        self.mic = sr.Microphone()
        self.recognizer = sr.Recognizer()

    def convert_voice_to_text(self):
        with self.mic as source:
            try:
                print("Speak !!!")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, phrase_time_limit=5)
                text = self.recognizer.recognize_google(audio)
            except:
                raise Exception("Couldn't understand you try again")
        return text
    
    def open_in_browser(self, keyword):
        webbrowser.open(f"https://{keyword}.com/")