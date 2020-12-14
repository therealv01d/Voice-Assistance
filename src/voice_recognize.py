#!/usr/bin/python3

import speech_recognition as sr

class VoiceAssitance():
    def __init__(self):
        self.mic = sr.Microphone()
        self.recognizer = sr.Recognizer()

    def convert_voice_to_text(self):
        with self.mic as source:
            try:
                print("Speak !!!")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
            except:
                raise Exception("Couldn't understand you try again")
        return text

    def do_operation(self):
        voice_text = self.convert_voice_to_text()
        while(True):
            if "facebook" in voice_text.lower():
                print("opening facebook")
                self.do_operation()
            elif "quit" in voice_text.lower():
                quit()