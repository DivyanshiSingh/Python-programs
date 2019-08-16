#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:21:10 2019

@author: divyanshisingh
"""

a=int(input("enter birth DD"))
b=int(input("enter birth MM"))
c=int(input("enter birth YY"))
d=int(input("enter current DD"))
e=int(input("enter current MM"))
f=int(input("enter current YY"))
g=((e*30)-(b*30))
i=d-a
h=g%30
j=i+h
k=g//30
l=f-c
print("age:",l,"years",k,"months",j,"days")

