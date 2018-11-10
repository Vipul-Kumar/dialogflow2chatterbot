# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:23:56 2018

@author: vipkumar
"""
from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
#chatterbot = ChatBot("Small_talk",read_only=True)
agent_name=input("Please enter the name of your Agent you want to train-->" )

chatterbot = ChatBot("dialogflow")
#chatterbot = ChatBot("Small_talk",logic_adapters=[
#        {
#            "import_path": "chatterbot.logic.BestMatch",
#            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
#            "response_selection_method": "chatterbot.response_selection.get_first_response"
#        }
#    ]
#)
chatterbot.set_trainer(ChatterBotCorpusTrainer)
#chatterbot.train("chatterbot.corpus.english.approval_bot.help","chatterbot.corpus.english.approval_bot.greetings","chatterbot.corpus.english.approval_bot.show_list")
chatterbot.train("./Agents/"+agent_name+"/intents/")
