# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:41:20 2018

@author: vipkumar
"""
import uuid
import datetime
import time
from chatterbot import ChatBot
from resolver import resolver
import pickle
import pprint
import random
chatterbot = ChatBot("Approval_engine",read_only=True
                         ,logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.50,
                'default_response': 'I am sorry, but I do not understand.'
            }
        ])
class Agent():
    out={}
    def listen(self,user_say,user_id,agent_name):
#        query=''
#        agent_name=input("Please enter the agent name -->")
        resolve_ob=resolver()
#        while(query!="n"):
#            query=input("You-->")
#            resolved_query=resolve_ob.resolve(query,agent_name)
#            response=chatterbot.get_response(resolved_query['resolved_query'])
#            print("response---->",response)
#            print("resolved_query-->",resolved_query)
        self.out['id']=str(uuid.uuid4())
        ts = time.time()
        timestamp=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.out['timestamp']=timestamp
        self.out['lang']="en"
        self.out['result']={}
        self.out['result']['source']=agent_name
        self.out['result']['resolvedQuery']=user_say
        
        resolved_query=resolve_ob.resolve(user_say,agent_name)
        intentName=chatterbot.get_response(resolved_query['resolved_query'])#passing resolved query for the brain to classify intent name
        print("intentName:",intentName)
        pickle_filename4intents=str("./Agents/"+agent_name+"/"+agent_name+"_intents.pickle")
        pickle_in = open(pickle_filename4intents,"rb")
        agent_intents = pickle.load(pickle_in)
        pp = pprint.PrettyPrinter(indent=2,depth=6)
#        pp.pprint(agent_intents)
        if intentName in agent_intents:
            self.out['result']['score']=intentName.confidence
            if "actionNparam" in agent_intents[intentName]:
                self.out['result']['action']=agent_intents[intentName]['actionNparam']['action']
            else:
                self.out['result']['action']=""
            self.out['result']['parameters']={}
            self.out['result']['contexts']=[]
            self.out['result']['metadata']={}
            self.out['result']['fulfillment']={}
            msg={}
            self.out['result']['fulfillment']['messages']=[]
#            self.out['result']['metadata']['intentId']=agent_intents[intentName]['intentId']
#            self.load_action_n_param()
            if agent_intents[intentName]["fulfillment"]["enable_webhook_4_intent"]==True:
                self.out['result']['metadata']['webhookUsed']=True
            else:
                self.out['result']['metadata']['webhookUsed']=False
            if agent_intents[intentName]["fulfillment"]["enable_webhook_4_slot_filling"]==True:
                self.out['result']['metadata']['webhookForSlotFillingUsed']=True
            else:
                self.out['result']['metadata']['webhookForSlotFillingUsed']=False
            self.out['result']['metadata']['intentName']=str(intentName)
            if agent_intents[intentName]["fulfillment"]=='y':
                
                self.out['result']['fulfillment']['speech']=""
                
                
                msg['type']=0
                msg['speech']=""
                self.out['result']['fulfillment']['messages'].append(msg)
            else:
                #check required parameters
                '''fetch response for the triggered intent in a random fashion if it contains
                a required param deal with the prompt'''
                self.out['result']['fulfillment']['speech']=(random.choice(agent_intents[intentName]['responses']))
                msg['speech']=self.out['result']['fulfillment']['speech']
                self.out['result']['fulfillment']['messages'].append(msg)
#            status={}
            
            
            pp.pprint(self.out)
ob=Agent()
ob.listen("hello","vipkumar","test103")      
