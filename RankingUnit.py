#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:50:53 2020

@author: zobaed
"""

import sys
import pandas as pd 
import math
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

dataset=config['DEFAULT']['dataset']

def idf(w,ab):
    cnt=0
    for a in ab:
        f= open ("./Dataset/"+dataset+"/" + a +".txt", "r" )
        reader=f.readlines()
        lineholder=""
        
        for line in reader:
            lineholder+= " " +line
        lineholder=lineholder.lower()
        if w in lineholder:
            cnt+=1
    return math.log2(len(ab)/(cnt+1))  
    
query = config['DEFAULT']['query'] #Demo query. Demo files are obtained based on this query.

initial_ranking_file=config['DEFAULT']['initial_ranking_file']
f=open(initial_ranking_file, "r") # res will be created by the union of the resultant files from the expanded query set
a=f.readlines()
f.close()

ab=[]
for i in a:
    bb=i.split(",")
    if (bb[-1] == "\n"):
        bb.remove("\n")
        
    for b in bb:
        if " " or "\n" in b:
            b=b.replace(" ", "")
            b=b.replace("\n", "")
            ab.append(b)
        else:
            ab.append(b)
            
ab=ab[:ab.index('')]

kendra_mama=[]

with open(config['DEFAULT']['Weighted_query'],"r") as f:
    af=f.readlines()
    for i in af:
        kendra_mama.append(i[:i.index(":")])


my_result_from_new_research={}

with open(config['DEFAULT']['Weighted_query'],"r") as f:
    ax=f.readlines()
    for a in ax:
        a=a.replace("\n", "")
    
        v1=a[: a.index(":")]
        v2=float(a[a.index(":")+1:] )
    
        my_result_from_new_research[v1]=v2

kendra_score_dict={}
   
for a in ab:
    f= open ("./Dataset/"+dataset+"/" + a +".txt", "r" )
    reader=f.readlines()
    lineholder=""
    for line in reader:
        lineholder+= " " +line
    lineholder=lineholder.lower()
    totWords=len(lineholder)
    cnt=0
    for km in kendra_mama:
        if km in lineholder:
            cnt+= ((lineholder.count(km)/totWords)* idf(km,ab)*my_result_from_new_research[km])
            #print(km,lineholder.count(km))
    kendra_score_dict[a]=cnt


    
import operator

sorted_dic = sorted(kendra_score_dict.items(), key=operator.itemgetter(1))
        
        
sorted_dic.reverse()

top_n=0
for key,val in sorted_dic:
    if top_n<10:
        print(key)
        top_n+=1
   
