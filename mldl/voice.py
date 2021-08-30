import cv2
import matplotlib.pyplot as plt

import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

'''
pip install speechrecognition
pip install playsound 
pip install gtts
음성 -> text 
text -> 음성
'''
def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

speak("3시 41분 입니다. 45분에 시작하죠")