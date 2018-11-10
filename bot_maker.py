# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:48:16 2018
@author: vipkumar
"""
import pickle
import AgentAttributes
import pprint
#from pathlib import Path
import os 
print("---------------Welcome to the Dev console of Bot Builder----------------\n")

user_choice=input("Please input \n '1' to build a new agent.\n '2' to load/modify an old agent. \n >>" )
if user_choice=='1':
    i=0
    agent_name=input("Please enter the name of your Agent -->" )
    new_agent_obj=AgentAttributes.bot_agent(agent_name)
#    path = Path('./Agents/hjh')
#    path.parent.mkdir(parents=True, exist_ok=True)
    newpath = "./Agents/"+agent_name+"/" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "./Agents/"+agent_name+"/intents/" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = "./Agents/"+agent_name+"/entities/" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    pickle_filename4intents="./Agents/"+agent_name+"/"+agent_name+"_intents.pickle"
    pickle_filename4entities="./Agents/"+agent_name+"/"+agent_name+"_entities.pickle"
    while(True):
        new_agent_obj.create_intent()
#        i=i+1
        pickle_out = open(pickle_filename4intents,"wb")
        pickle.dump(new_agent_obj.intents, pickle_out)
        pickle_out.close()
        pickle_out = open(pickle_filename4entities,"wb")
        pickle.dump(new_agent_obj.entities, pickle_out)
        pickle_out.close()
        cont=input("Do you want to create another intent?\n[y/n]")
        if cont=='y':
            continue
        else:
            break        
elif user_choice=='2':
    agent_name=input("Enter the name of the agent you want to load-->")
    pickle_filename4intents=str("./Agents/"+agent_name+"/"+agent_name+"_intents.pickle")
    pickle_filename4entities=str("./Agents/"+agent_name+"/"+agent_name+"_entities.pickle")
    #print(pickle_filename4entities)
    pickle_in = open(pickle_filename4intents,"rb")
    agent_intents = pickle.load(pickle_in)
    pp = pprint.PrettyPrinter(indent=2,depth=6)
    pp.pprint(agent_intents)
    pickle_in = open(pickle_filename4entities,"rb")
    agent_entities= pickle.load(pickle_in)
    pp = pprint.PrettyPrinter(indent=2,depth=6)
    pp.pprint(agent_entities)
    
    print("\nData load successful :)")
    
#approval_bot=bot_builder.bot_agent()
#i=0

#print(approval_bot.intents)
#pickle_out = open("bot.pickle","wb")
#pickle.dump(approval_bot.intents, pickle_out)
#pickle_out.close()