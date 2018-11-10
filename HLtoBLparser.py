# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:13:19 2018

@author: vipkumar
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:18:51 2018

@author: vipkumar
"""
import pickle
import pprint
import yaml
#import re
#import itertools

def find_substring(substring, string):
    """ 
    Returns list of indices where substring begins in string

    >>> find_substring('me', "The cat says meow, meow")
    [13, 19]
    """
    indices = []
    index = -1  # Begin at -1 so index + 1 is 0
    while True:
        # Find next index of substring, by starting search from index + 1
        index = string.find(substring, index + 1)
        if index == -1:  
            break  # All occurrences have been found
        indices.append(index)
    return indices
agent_name=input("Enter the name of the agent you want to load-->")
pickle_filename4intents=str("./Agents/"+agent_name+"/"+agent_name+"_intents.pickle")
pickle_filename4entities=str("./Agents/"+agent_name+"/"+agent_name+"_entities.pickle")
#print(pickle_filename4entities)
pickle_in = open(pickle_filename4intents,"rb")
agent_intents = pickle.load(pickle_in)
pp = pprint.PrettyPrinter(indent=2,depth=6)
#pp.pprint(agent_intents)
pickle_in = open(pickle_filename4entities,"rb")
agent_entities= pickle.load(pickle_in)
pp = pprint.PrettyPrinter(indent=2,depth=6)
pp.pprint(agent_entities)
'''for k,v in agent_intents.items():
    
    print(agent_intents[k]['training_phrases'])
    dataMap={}
    dataMap["intent_name"]=k
    dataMap["conversations"]=[]
    for phrase in agent_intents[k]['training_phrases']:
        indices=find_substring('|',phrase)
        if len(indices)>1:
            entity=[]
            size=len(indices)-1
            for i in range(0,size):
                if i%2==1:
                    continue
                #print(i)
                entity.append(phrase[(indices[i]+1):indices[i+1]])
            print(entity)
            combination_list=[]
            for val in entity:
                complete_list=[]
                for values in agent_entities[val].items():
                    print("values==",values[1]['synonym'])
                    for syn in values[1]['synonym']:
                        complete_list.append(syn)
#                print("complete list=",complete_list)
                combination_list.append(complete_list)
            print ("combination list",combination_list)
            print("*combination list",*combination_list)
            for combination in itertools.product(*combination_list):
                print ("combination",combination)
                
                phrase1=phrase
                for syn in combination:
                    print("syn-->",syn)
                    print("value of phrase 1 before any operation",phrase1)
                    for ent in entity:
                        print(phrase1.find(("|"+ent+"|")))
                        if phrase1.find(("|"+ent+"|"))>-1:
                            print("value of ent is",ent)
                            print("change before exec",phrase1)
                            phrase1=phrase1.replace(("|"+ent+"|"),(' '+syn+' '))
                            phrase1=re.sub(' +',' ',phrase1)
                            print("change after exec",phrase1)
                            break                 
                            
                print("phrase1 after entity block=",phrase1)
                sub_list=[]
                sub_list.append(phrase1)
                sub_list.append(k)
                dataMap["conversations"].append(sub_list)
                    
                        
                        
#                for syn in agent_entities[ent]:
#                    phrase1=phrase.replace(("|"+ent+"|"),(' '+syn+' '))
#                    phrase1=re.sub(' +',' ',phrase1)
#                    sub_list=[]
#                    sub_list.append(phrase1)
#                    sub_list.append(k)
#                    dataMap["conversations"].append(sub_list)
#                #phrase=phrase1
            
                    
        else:    
            sub_list=[]
            sub_list.append(phrase)
            sub_list.append(k)
            dataMap["conversations"].append(sub_list)
    
    file="./Agents/"+agent_name+"/intents/"+k+".yml"
    f= open(file,"w+")
    yaml.dump(dataMap, f, default_flow_style=False)
    f.close()'''
#****************************************************************
for k,v in agent_intents.items():
    
    print(agent_intents[k]['training_phrases'])
    dataMap={}
    dataMap["intent_name"]=k
    dataMap["conversations"]=[]
    for phrase in agent_intents[k]['training_phrases']:
        sub_list=[]
        sub_list.append(phrase)
        sub_list.append(k)
        dataMap["conversations"].append(sub_list)
    file="./Agents/"+agent_name+"/intents/"+k+".yml"
    f= open(file,"w+")
    yaml.dump(dataMap, f, default_flow_style=False)
    f.close()
if agent_entities:
    for k in agent_entities:
        datamap={}
        datamap[k]=agent_entities[k]
        pp.pprint(datamap)
        file="./Agents/"+agent_name+"/entities/"+k+".yml"
        f= open(file,"w+")
        yaml.dump(datamap, f, default_flow_style=False)
        f.close()
            
#    for x in v:
#        #if re.search(x.lower(),response.lower()):
#        print(k['training_phrases'])
#            
#       # print ('"%s" key found in the entered text '%(val))
#        #entity_list.append(k)



print("\nData load successful :)")
