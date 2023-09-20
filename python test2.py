# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:29:47 2023

@author: louis
"""
import random

a, b = 0, 1
d=dict()
while a < 10000:
    d[a]=str(a)+' puis'
    print(a,'puis', end = ' ')
    a, b = b, a+b
    

def anon_in_d(d,name):
    if len(d.keys())>d['clef']:
        print('ERROR: d is full')
        return
    isnotok=True
    while isnotok:
        key=random.randrange(0,d['clef'])
        isnotok = (key in [d[k] for k in d.keys()])
        
    d[name]=key
        
    return key

def create_d_anon (l=100):
    d=dict()
    d['clef']=l
    return d