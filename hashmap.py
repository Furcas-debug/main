# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 02:41:45 2020

@author: Furcas
"""
from itertools import groupby
import pandas as pd
import bisect
#import vlc
import numpy as np
import pygame 
import playsound
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
         "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
         "..-","...-",".--","-..-","-.--","--.."]


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = ["gin", "zen", "gig", "msg"]
def main(words):
    
    return len(set([trans(word) for word in words]))


def trans(word):
    morse = []
    WtoM = {'a': '.-', 'b': '-...', 'c': '-.-.',
                   'd': '-..', 'e': '.', 'f': '..-.',
                   'g': '--.', 'h': '....', 'i': '..',
                   'j': '.---', 'k': '-.-', 'l': '.-..',
                   'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                   'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                   'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                   'y': '-.--', 'z': '--..'}
    print(len(WtoM))
    for ch in word:
        morse.append(WtoM[ch])
    return ''.join(morse)
    

nums = [3,7]

ars = {i:j for i , j in zip(range(len(nums)), nums)}
from collections import Counter
def lord(nums):
    aims = []
    aims.append(max(nums))
    nums.remove(max(nums))
    aims.append(max(nums))
    nums.remove(max(nums))
    return (aims[0]-1)*(aims[1]-1)
#print (lord(nums))'
def all_the_same(elements):
    return len(set(elements)) <= 1

def arr(num):
    stor = []
    
    for i in range(num):
        stor.append((2*i)+1)
    
    
    
    return stor
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

source = paths[0][0]
graph = {source: destination for source, destination in paths}
#print(graph)
current = source
while current in graph:
    current = graph[current]
    #print(current)
#print(current)
nums = [-1, 0, 1, 2, -1, -4]
t_nums = {i:j for i, j in zip(nums, range(len(nums)))}
#print(t_nums)
def kir(nums):
    res = []
    for i in nums:
        for j in nums:
            for k in nums:
                if i!= j and j != k and k != j and j!=k and i+j+k ==0:
                    res.append([i, j , k])
    ctr = Counter(frozenset(x) for x in res)
    b = [ctr[frozenset(x)] == 1 for x in res]    
    #print((res[0])==(res[1]))
    resd= pd.DataFrame(res).drop_duplicates().to_dict()
    new_x = [el for el, _ in groupby(res)]
    return new_x
#print(kir(nums))
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

for i in range(n):
    nums1.pop()
for i in nums2:
    bisect.insort(nums1,i) 
    
#print(nums1)

A = [-4,-1,0,3,10]
B = []
import math
num = 8

    
B.sort()
def sm(num):
    
    return(int(math.sqrt(int(num))))
def myPow(x: float, n: int):
    return round(pow(x, n), 5)
#print(myPow(2.10000, 3))
#playsound.playsound('boom.mp3', True)
#playsound.playsound('foo.mp3', True)
def Morse(strk):
    for i in strk:
        if i == '.':
           playsound.playsound('boom.mp3', True) 
        else:
           playsound.playsound('foo.mp3', True)
           return 'Done!'
print(Morse(trans('hi')))

#sd.play(np.array(trans('help')), 44100)

