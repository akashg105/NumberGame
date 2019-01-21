'''
Created on Mar 30, 2016

@author: Akash.Gupta17
'''
import random
import json
from arrangeCherry import Card
class Practice:
    def shuffle(self,temp1):
        res=json.loads(temp1)
        one=res[0]
        two=res[1]
        three=res[2]
        value=res[3]
        final=res[4]
        if value==3:
            final=one+three+two            
        elif value==1:
            final=two+one+three    
        else:
            final=one+two+three    
        one=[]
        two=[]
        three=[]
        re1=Card().arrange(final,one,two,three)    
        one=re1[0]
        two=re1[1]
        three=re1[2]
        re2=Card().insert(one, [])
        re3=Card().insert(two,[])
        re4=Card().insert(three,[])
        random.shuffle(re2)
        random.shuffle(re3)
        random.shuffle(re4)
        return json.dumps(one+two+three+re2+re3+re4)
        #return json.dumps(Practice.one+Practice.two+Practice.three)