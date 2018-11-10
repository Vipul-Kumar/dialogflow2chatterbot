Module Description:
AgentAttributes.py -
Function :- to define the attributes of each agent
Dependency- No dependency

Bot_maker.py-
Function :- To Create or Load an agent.
Dependency - Agent name,Agent Path,<class>AgentAttributes
Logic-
1.	To create a new agent make all the required directories for the new agent.
2.	To load all the contents of the pickle file of a previously created agent.
To do:-
1.	Add option to add new information to a previously created Agent.We can only view the dict values of an agent in the load agent option as on now(9th April 2018).
2.	Add class to the script

Intent_generator.py -
Function:-an accelerator to read dialogflow files and give the output in our required format.
Dependency:- path of the dialogflow exported files.
Logic-
1.	Read the json file exported from Dialogflow.
2.	Fetch information from those files and return it in the format required for our inhouse NLP platform.
To do:-
            Having an option to directly feed data to our Agent from the exported Dialogflow files.

HLtoBLparser.py- (High Level to Brain Level Parser)
Function:-
•	A parser that parses all the intents and entities values stored in the agent’s pickle file and makes intents and entities yml files in the respective folders in agent’s directory for its  consumption by Chatterbot.
Dependency -
•	Agent name, agent path, pickle files to feed to the parser.

Resolver.py-
Function- 
•	Gets user_say from the <class>brain_interface and resolves the entities value and sys values in order to save important information out of the given user say as well as transforms the query into generic sentence to increase the accuracy of the brain for effective classification.
Dependency-entities extractor
Logic-refer code 
To do-
•	Have the final result generation in the resolver code rather than entities_extractor.
•	Make the @sys regex available for effective information extraction

Entities_extractor.py-
Function
•	To extract the information related to user defined entities
Dependency -agent name,pickle files to get the list of entities
Logic-refer code
To do-
•	Transforming of the userquery is presently done in entities_extractor but it should be done in resolver.py
Bot_brain_trainer.py-
Function- to start the training of brain with the intents of a particular agent.
Dependency-agent name, yml files for intents,
Logic-go through chatterbot docs
Todo-
•	Find a way to train individual agents on their respective intents file

Brain_interface.py-
Function- it acts as an interface between the end user and the chatterbot brain
Dependency- agent name,threshold value,fallback intent,db.sqlite3 file of trained brain.
Logic- refer code

Postman.py-
Function - a module to send post requests to a specific url
Dependency - url to hit,json values that needs to be sent to the url
Logic- refer code
Todo-
•	To integrate this module with the NLP framework



 

