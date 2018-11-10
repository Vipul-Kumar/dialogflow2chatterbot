# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:37:38 2018

@author: vipkumar
"""
#class intent:
#    def __init__(self,name,input_node):
#        self.name=name
#        self.input_node=input_node
#    def show_linking(self):
#        print (self.input_node)
#
#first=intent("greeting",[8,7,8])   
#first.show_linking()

import speech_recognition as sr
r = sr.Recognizer()                 # get audio from the microphone                                                                                 
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)        #saving what you speak
try:
     print("You said " + r.recognize_google(audio))     #printing what you spoke
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
        