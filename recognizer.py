#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:43:11 2019

@author: divyanshisingh
"""

import speech_recognition as sr
m=sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything: ")
    audio=m.listen(source)
    try:
        text=m.recognize_google(audio)
        print("you spoke:{}".format(text))
    except:
        print("sorry cant recognise")