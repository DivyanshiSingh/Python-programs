#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:22:27 2019

@author: divyanshisingh
"""

for i in range(1,6):
    for j in range(1,2):
        if i==2:
            print("\U0001f600\U0001f600"," ","\U0001f600\U0001f600",end="")
        elif i==3:
            print("\U0001f600"" ","\U0001f600"," ","\U0001f600",end="")
        else:
            print("\U0001f600"," "," "," ","\U0001f600",end="")
        
    print()
    
