# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:39:57 2023

@author: louis
"""


## Exercice 1

import math

def cone_droit(r,h):
    V = (1/3)*math.pi*h*(r**2)
    
    return V
    
## Exercice 2

def prix(HT):
    HT0=HT
    while HT<(HT0*1.2):
        HT+=1
    TTC = HT
    return TTC

## Exercice 3

import random

def suite(n):  #n est le range du random
    L=list()
    C=0
    S=0
    ajout=random.randrange(-5,n)
    print(ajout)
    while ajout>0:
        #L = L + [ajout]
        L.append(ajout)
        S+=ajout
        if ajout>100:
            C+=1
        ajout=random.randrange(-5,n)
    return ('La somme est',S,'et le nombre>100 est',C,
            'La liste est',L)
   
## Exercice 4

def parite(n):
    if n%2==0:
        return ('PAIR')
    return ('IMPAIR')
    
## Exercice 5

def parite_nb(n):
    nb=0
    while n%2==0:
        nb+=1
        n=n//2
    return nb
    
## Exercice 6


def diviseurs():
    n = int(input('Veuillez saisir un entier supérieur à 1 : '))
    div=[]
    for i in range(2,n+1):
        if n%i==0:
            if i not in div:
                div.append(i)
    if len(div)==1:
        return ('Aucun ! Il est premier')        
    return('Diviseurs propres sans répétitions de',n,':',div)

  
    
    
    
    
    
    
    
    
    
    