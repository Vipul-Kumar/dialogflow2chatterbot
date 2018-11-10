# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:00:01 2018

@author: vipkumar
"""
import pprint
import json
pp = pprint.PrettyPrinter(indent=2,depth=6)
filename=input("enter intent name-->")
response_filename=filename+"_usersays_en.json"
filename="C:/Users/vipkumar/Downloads/My_Office_Assistant/intents/"+filename+".json"
response_filename="C:/Users/vipkumar/Downloads/My_Office_Assistant/intents/"+response_filename
f=open(response_filename,"rb")
json_user_say=json.load(f)
f.close()
#print(json_user_say)
intents=""
entities=[]
for ele in json_user_say:
    if len(ele["data"])>1:
        for text in ele["data"]:
            if "meta" in text:
                intents=intents+"|"+text["meta"]+"|"
                
            else:
                intents=intents+" "+text["text"]
        intents=intents+";"
    elif "meta" in ele["data"][0]:
                intents=intents+"|"+ele["data"][0]["meta"]+"|"        
    else:
        intents=intents+ele["data"][0]["text"]+";"
print("intents-->",intents)
f=open(filename,"rb")
json_user_say=json.load(f)
f.close()
#print("parameter values:   ",json_user_say['responses'])

response=""
#print(json_user_say['responses'][0]['messages'][0]['speech'])
for res in json_user_say['responses']:#['messages'][0]['speech']:
    for res1 in res['messages']:
        #print("res1 length len(res1['speech']-->",type(res1['speech']))
        #if len(res1['speech'])>:
        if type(res1['speech']) is list:
            for val in res1['speech']:
                response=response+val+';'
        else:
            response=res1['speech']
                
            
        
#        for res2 in res1:
#            response=response+res2['speech']+";"
        
    #response=response+res+";"

print("\n\nresponse-->",response)

print("****************entities generator***********")

while(1):
    load_entity=input("do you want to load entity[y/n]-->")
    if load_entity=='n':
        break
    filename=input("enter entity name-->")
    filename="C:/Users/vipkumar/Downloads/My_Office_Assistant/entities/"+filename+"_entries_en.json"
    f=open(filename,"rb")
    entity_dict=json.load(f)
    f.close()
    value_string=""
    syn_list=[]
    syn_string=""
    for dicts in entity_dict:
        value_string=value_string+dicts['value']+';'
        syn_list.append(dicts['synonyms'])
    print("value_list-->",value_string)
    for syn_set in syn_list:
        for item in syn_set:
            syn_string=syn_string+item+';'
        print("synonyms-->",syn_string)
        syn_string=""
    load_entity=input("do you want to load more entity[y/n]-->")
    if load_entity=='y':
        continue
    else:
        break
if 'action' in json_user_say['responses'][0]:
    print ("\n \n ************************************ action and para")
    print("action name->",json_user_say['responses'][0]['action'])
if 'parameters' in json_user_say['responses'][0]:
    for para in json_user_say['responses'][0]['parameters']:
        pp.pprint(para)
        hit=input("press enter to get next parameter")
            
    
        

