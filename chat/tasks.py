import speech_recognition as sr


def speech_to_text(speech_file):
    '''
    Convert speech to text using Google Speech Recognition
    '''
    # r = sr.Recognizer()
    # with sr.AudioFile(speech_file) as source:
    #     audio = r.record(source)
    # try:
    #     text = r.recognize_google(audio)
    # except sr.UnknownValueError:
    #     text = "Google Speech Recognition could not understand audio"
    # except sr.RequestError as e:
    #     text = "Could not request results from Google Speech Recognition service; {0}".format(
    #         e)
    # return text
    print("Speech to text")
