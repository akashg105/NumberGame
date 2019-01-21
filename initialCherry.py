'''
Created on Mar 30, 2016

@author: Akash.Gupta17
'''
import json
import random

class Practice2:
    
    def initial(self):
        one=[1,4,7,10,13]
        two=[2,5,8,11,14]
        three=[3,6,9,12,15]
        random.shuffle(one)
        random.shuffle(two)
        random.shuffle(three)
        final=one+two+three
        return json.dumps(final)