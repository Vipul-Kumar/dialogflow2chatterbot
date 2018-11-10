# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:07:58 2018

@author: vipkumar
"""
from chatterbot import ChatBot
from resolver import resolver
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
query=''
agent_name=input("Please enter the agent name -->")
resolve_ob=resolver()
while(query!="n"):
    query=input("You-->")
    resolved_query=resolve_ob.resolve(query,agent_name)
    response=chatterbot.get_response(resolved_query['resolved_query'])
    print("response---->",response)
    print("resolved_query-->",resolved_query)
