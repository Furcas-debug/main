# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 03:56:17 2020

@author: Furcas
"""

str1 = '`' 
str2 = ''
def soll(res):
    lsWord = {}

    for key in res:
        key = key.lower()
        if key in lsWord:
            value = lsWord[key]
            lsWord[key]=value+1
        else:
            lsWord[key]=1
        
    return sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)       

def main(str1, str2):
    if str1 == '' and str2 == '':
        return True
    if soll(str1) == soll(str2):
        return False
    
    return len(soll(str1))==len(soll(str2))
    
print(main(str1, str2))