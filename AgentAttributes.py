# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:41:33 2018

@author: vipkumar
"""
#

import datetime
import time
import uuid
class bot_agent:
    entities={}
    intents={}
    name=""
    def __init__(self,name):
        self.name=name
        print("Agent created")
    def find_substring(self,substring, string):
        """ 
        Returns list of indices where substring begins in string
    
        >>> find_substring('me', "The cat says meow, meow")
        [13, 19]
        """
        indices = []
        #substring=str(substring)
        #print("substring=",substring)
        index = -1  # Begin at -1 so index + 1 is 0
        while True:
            # Find next index of substring, by starting search from index + 1
            index = string.find(substring, index + 1)
            if index == -1:  
                break  # All occurrences have been found
            indices.append(index)
        return indices

    def create_intent(self):
        name=input("Please name your intent-->")
        self.intents[name]={}
        ts = time.time()
        timestamp=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.intents[name]['creation_timestamp']=timestamp
        self.intents[name]['lang']="en"
        self.intents[name]['intentId']=str(uuid.uuid4())
        context=input("Enter the values as input context for this intent(semicolon-seperated)-->")
        input_context=context.split(';')
        self.intents[name]['input_context']=input_context
        context=input("Enter the [semicolon-seperated] values as output context for this intent with [comma-seperated] lifespan(defaultValue=5) eg.[ app,5;lms,3  ]-->")
        output_context=context.split(';')
        self.intents[name]['output_context']=output_context
        self.intents[name]['events']=input("[Optional] way to trigger intent without the need for matched text or spoken input.\n Use predefined platform specific events or define your custom ones.-->")
        self.intents[name]['training_phrases']=input("Phrases you can expect from users, that will trigger the intent.(semicolon seperated)\nIf your training phrases have some entities which are to be linked with some words replace the word with '@entity_name' enclosed within '|'-->").split(';')
        for phrase in self.intents[name]['training_phrases']:
            indices=self.find_substring('|',phrase)
            if len(indices)>1:
                entity=[]
                size=len(indices)-1
                for i in range(0,size):
                    if i%2==1:
                        continue
                    #print(i)
                    entity.append(phrase[(indices[i]+1):indices[i+1]])
                print(entity)
                for ent in entity:
                    if ent in self.entities:
                        continue
                    else:
                        self.entities[ent]={}
                        key_values=input("Enter the val of "+ent+" entity [semicolon seperated]").split(';')
                        print("key values:-",key_values)
                        for resolution in key_values:
                            self.entities[ent][resolution]={}
                            self.entities[ent][resolution]['synonym']=input("Enter the synonyms for "+resolution+" resolution [semicolon seperated]").split(';')
                            self.entities[ent][resolution]['synonym'].append(resolution)
                        #self.entities[ent].append(ent)
        action_param=input("Actions are sent to fulfillment, once an intent is triggered. \nParameters are specific words or phrases you’re trying to collect from users, in order to complete a task.\nDo you want to set action?(y/n)-->")
        if action_param=='y':
            self.intents[name]['actionNparam']={}
            self.intents[name]['actionNparam']['parameters']={}
            
            self.intents[name]['actionNparam']['action']=input("Actions are sent to fulfillment,Enter an action name-->")
            while(True):
                param_name=input("Enter the name of the parameter-->")
                self.intents[name]['actionNparam']['parameters'][param_name]={}
                self.intents[name]['actionNparam']['parameters'][param_name]['required']=input("Enter 'y' if the intent can’t be complete without corresponding parameter.-->")
                self.intents[name]['actionNparam']['parameters'][param_name]['entity']=input("Specify a system or a developer entity corresponding to this parameter.-->")
                self.intents[name]['actionNparam']['parameters'][param_name]['value']=input("Value of the parameter i.e variable name-->")
                self.intents[name]['actionNparam']['parameters'][param_name]['isList']=input("Enter 'y' for getting a list of values for the corresponding parameter.-->")
                if self.intents[name]['actionNparam']['parameters'][param_name]['required']=='y':
                    self.intents[name]['actionNparam']['parameters'][param_name]['prompts']=input("Type questions that the agent will ask your users, if a request doesn't contain this parameter[semicolon seperated]").split(';')
                self.intents[name]['actionNparam']['parameters'][param_name]['default_value']=input("Enter default value for "+param_name)    
                cont=input("Do you want to add more parameters (y/n)")
                if cont=='y':
                    continue
                else:
                    break
        self.intents[name]['responses']=input("Text, spoken and media rich responses the agent will deliver to a user.(semicolon seperated)-->").split(';')
        self.intents[name]['end_of_conversation']=False
        self.intents[name]['ml_enabled']=False
        self.intents[name]["fulfillment"]={}
        fulfillment=input("Do you want to enable Fulfillment \n[y/n]-->")
        if fulfillment=='y':
            webfulfillment=input("Do you want to enable webhook for intent \n[y/n]-->")
            if webfulfillment=='y':
                self.intents[name]["fulfillment"]["enable_webhook_4_intent"]=True
            else:
                self.intents[name]["fulfillment"]["enable_webhook_4_intent"]=False 
            slotfulfillment=input("Do you want to enable webhook for slot filling \n[y/n]-->")
            if slotfulfillment=='y':
                self.intents[name]["fulfillment"]["enable_webhook_4_slot_filling"]=True
            else:
                self.intents[name]["fulfillment"]["enable_webhook_4_slot_filling"]=False
        else:
            self.intents[name]["fulfillment"]["enable_webhook_4_intent"]=False
            self.intents[name]["fulfillment"]["enable_webhook_4_slot_filling"]=False
        self.intents[name]["default_fallback"]=False
        self.intents[name]["priority"]=500000
    
    