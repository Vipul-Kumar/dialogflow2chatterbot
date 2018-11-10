# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:36:37 2018

@author: vipkumar
"""
# importing the requests library
import requests
import json
# api-endpoint
URL = "https://voice-enginev3.herokuapp.com/webhook"
 
# location given here
location = "delhi technological university"
 
# defining a params dict for the parameters to be sent to the API
PARAMS ={
"id": "95c3bf5c-f07e-47d3-831b-82d13e60f8ac",
"timestamp": "2018-03-26T07:43:22.673Z",
"lang": "en",
"result": {
"source": "agent",
"resolvedQuery": "lms",
"speech": "",
"action": "erp_and_date",
"actionIncomplete": "false",
"parameters": {
"erp_with_date": "lms",
"date": "0000-00-00/0000-00-00",
"hours": "1000",
"number_of_days": "0",
"continue": "null",
"onebyone": "false",
"comp_parameter": "equal"
},
"contexts": [
{
"name": "ctx_erp",
"parameters": {
"date": "0000-00-00/0000-00-00",
"comp_parameter.original": "",
"hours": "1000",
"number_of_days": "0",
"date.original": "",
"onebyone.original": "",
"onebyone": "false",
"erp_with_date": "lms",
"number_of_days.original": "",
"erp_with_date.original": "lms",
"continue": "null",
"hours.original": "",
"continue.original": "",
"comp_parameter": "equal"
},
"lifespan": 5
}
],
"metadata": {
"intentId": "1d051048-582e-47ce-8357-c7bc153aa745",
"webhookUsed": "true",
"webhookForSlotFillingUsed": "false",
"intentName": "07.erp.and.date"
},
"fulfillment": {
"speech": "",
"messages": [
{
"type": 0,
"speech": ""
}
]
},
"score": 1.0
},
"status": {
"code": 200,
"errorType": "success",
"webhookTimedOut": "false"
},
"sessionId": "9e874bea-8ebc-48e0-9a0d-e0e2b0b7e6db"
}

print(PARAMS) 
print("*********************************************************************************")
# sending get request and saving the response as response object
r = requests.post(url = URL, data=json.dumps(PARAMS))
print(r.status_code)
# extracting data in json format
data = r.json()
print(data) 
# 
## extracting latitude, longitude and formatted address 
## of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
#formatted_address = data['results'][0]['formatted_address']
# 
## printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#      %(latitude, longitude,formatted_address))
#
