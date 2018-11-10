import re
#import yaml
import pickle
#import pprint
class entities_extractor:
    def get_entities(self,query,agent_name):
        pickle_filename4entities=str("./Agents/"+agent_name+"/"+agent_name+"_entities.pickle")
        pickle_in = open(pickle_filename4entities,"rb")
        agent_entities= pickle.load(pickle_in)
#        pp = pprint.PrettyPrinter(indent=2,depth=6)
#        pp.pprint(agent_entities)
        resolved_query=query
        
        entity_resolver={}
        entity_resolver['entity']={}
        entity_resolver['query']=query
        entity_resolver['resolved_query']=resolved_query
        for k,v in agent_entities.items():
            value_list=[]
            for x in v:
                if x!='':
                    
                    for syn in agent_entities[k][x]['synonym']:
                        if re.search(syn.lower(),resolved_query.lower()):
                            entity_resolver['entity'][k]={}
                            
#                            entity_resolver[k]['value']=x
                            value_list.append(x)
                            #print("entity_resolver[k]['value']=x-->",entity_resolver[k]['value'])
                            if resolved_query.find(syn)>-1:
                                resolved_query=resolved_query.replace(syn,("|"+k+"|"))
                                resolved_query=re.sub(' +',' ',resolved_query)
                                entity_resolver['resolved_query']=resolved_query
                                entity_resolver['entity'][k]['value']=value_list
#                if (re.search(x.lower(),resolved_query.lower())and x!=''):
#                    print("value of x-->",agent_entities[k][x]['synonym'])
#                    #print("Found the text-->",x)
#                    #print ('"%s" key found in the entered text '%(k))
#                    entity_list.append(k)
#                    #print("entity list-->",entity_list)
#                    #hit=input("hit-->")
                    
        return(entity_resolver)
