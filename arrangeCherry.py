'''
Created on Mar 30, 2016

@author: Akash.Gupta17
'''
class Card:
    def arrange(self,s,one,two,three):
        for k in range(0,15,3):
            one.append(s[k])
        for l in range(1,15,3):
            two.append(s[l])
        for m in range(2,15,3):
            three.append(s[m])
        return one,two,three
    
    def insert(self,one,new_one):
        for temp in range(5):
            new_one.append(one[temp])
        return new_one