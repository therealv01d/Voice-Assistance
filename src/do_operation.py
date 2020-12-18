#!/usr/bin/python3

from src.voice_recognize import VoiceAssitance 

vAssist = VoiceAssitance()

def do_operation():
    voice_text = vAssist.convert_voice_to_text()
    while(True):
        if "open facebook" in voice_text.lower():
            print("opening facebook")
            vAssist.open_in_browser("facebook")
            do_operation()

        if "open twitter" in voice_text.lower():
            print("opening twitter")
            vAssist.open_in_browser("twitter")
            do_operation()

        if "open youtube" in voice_text.lower():
            print("opening youtube")
            vAssist.open_in_browser("youtube")
            do_operation()

        if "open instagram" in voice_text.lower():
            print("opening instagram")
            vAssist.open_in_browser("instagram")
            do_operation()

        elif "quit" in voice_text.lower():
            quit()