import time
import speech_recognition as sr

# Phase 1:
# def speech_to_text(speech_text):
#     '''
#     Convert speech to text using Google Speech Recognition
#     '''

#     time.sleep(10)
#     print(speech_text)


def speech_to_text(speech_file):
    '''
    Convert speech to text using Google Speech Recognition
    '''

    r = sr.Recognizer()
    with sr.AudioFile(speech_file) as source:
        audio_text = r.listen(source)
        text = r.recognize_google(audio_text)
        print(text)
