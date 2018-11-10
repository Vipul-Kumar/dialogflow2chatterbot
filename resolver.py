# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:35:20 2018

@author: vipkumar
"""

from entities_extractor import entities_extractor
class resolver():
    def resolve(self,text2resolve,agent_name):
#        agent_name=input("Enter the name of the agent you want to load-->")
#        text2resolve=input("Enter the user says-->")
        obj=entities_extractor()
        return(obj.get_entities(text2resolve,agent_name))

