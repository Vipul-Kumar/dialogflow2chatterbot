# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:02:37 2018

@author: vipkumar
"""

import json

json_data=open("json_format.json").read()
json_data={
  "id": "a537ab91-9f63-42f0-a217-aa3858480b01",
  "timestamp": "2018-03-15T06:00:57.894Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "what can you do",
    "action": "",
    "actionIncomplete": False,
    "parameters": {
      "soft": ""
    },
    "contexts": [
      {
        "name": "server",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 4
      },
      {
        "name": "s4",
        "parameters": {
          "soft.original": "",
          "soft": ""
        },
        "lifespan": 5
      },
      {
        "name": "app",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 4
      },
      {
        "name": "s5",
        "parameters": {
          "soft.original": "",
          "soft": ""
        },
        "lifespan": 5
      },
      {
        "name": "software",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 4
      },
      {
        "name": "name",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 3
      },
      {
        "name": "start",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 4
      },
      {
        "name": "login",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 4
      },
      {
        "name": "other",
        "parameters": {
          "given-name.original": "",
          "soft.original": "",
          "initial-username.original": "vipul",
          "given-name": "",
          "initial-username": "Vipul",
          "soft": ""
        },
        "lifespan": 4
      },
      {
        "name": "s1",
        "parameters": {
          "soft.original": "",
          "soft": ""
        },
        "lifespan": 5
      },
      {
        "name": "s2",
        "parameters": {
          "soft.original": "",
          "soft": ""
        },
        "lifespan": 5
      },
      {
        "name": "s3",
        "parameters": {
          "soft.original": "",
          "soft": ""
        },
        "lifespan": 5
      }
    ],
    "metadata": {
      "intentId": "909005ef-47f8-4f86-ae9a-60e81df93823",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "software_issue"
    },
    "fulfillment": {
      "speech": "Software Issues: 1. Installation Issue 2. Software not responding 3. Screen freeze problem 4. Compatibility problem 5. Other",
      "messages": [
        {
          "type": 1,
          "platform": "slack",
          "title": "Software issues",
          "subtitle": "Can you share a little bit more info about your Software issue?",
          "buttons": [
            {
              "text": "Installation issue",
              "postback": ""
            },
            {
              "text": "Software not responding",
              "postback": ""
            },
            {
              "text": "Screen freeze problem",
              "postback": ""
            }
          ]
        },
        {
          "type": 1,
          "platform": "slack",
          "buttons": [
            {
              "text": "Compatibility problem",
              "postback": ""
            },
            {
              "text": "Any other",
              "postback": ""
            }
          ]
        },
        {
          "type": 0,
          "speech": "Software Issues:\n1. Installation Issue\n2. Software not responding\n3. Screen freeze problem\n4. Compatibility problem\n5. Other"
        }
      ]
    },
    "score": 0.33000001311302185
  },
  "status": {
    "code": 200,
    "errorType": "success",
    "webhookTimedOut": False
  },
  "sessionId": "6b3e3a98-129e-4a9d-a6fd-6fd47408e269"
}
print (type(json_data))
empty_dict={}
for key,value in json_data.items():
    print("----------------",key,"--------------------")
    try:
        if value.items():
            for inner_value in value.items():
                print("\n",inner_value,"\n")
    except:
        continue


print("****************************************************")
temp={}
temp["key"]=None
print(temp)





