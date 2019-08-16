#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:33:49 2019

@author: divyanshisingh
"""

l=[]
ch=1
while ch!=0:
    m=int(input("enter the score"))
    l.append(m)
    ch=int(input("enter your choice<0/1>"))
n=max(l)
l.remove(n)
print(max(l))