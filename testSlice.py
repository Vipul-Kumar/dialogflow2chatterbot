# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:22:51 2018

@author: vipkumar
"""
import itertools
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
phrase="hello |@hell||@kasdjls|vipul is vipul |@nice|"
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
x=[]
#for x in (permutations(entity,2)):
#    print("x::::",x[0])
#    print("y",x[1])
##    print("v::::",v)
##    print("z::::",z)
      
#print(phrase[22:32])
uk_rock_stars=[1,2]
uk_pop_stars=[10,11,13]
us_stars=[22,34,44,7,33]
sakshi=["vipul","vidhi","sakshi","deep"]
#print(list(itertools.product(uk_rock_stars, uk_pop_stars,us_stars,sakshi)))
for combination in itertools.product(uk_rock_stars, uk_pop_stars,us_stars,sakshi):
    print (combination[0])

indexlist=[0,1,2]
