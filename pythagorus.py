#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:55:07 2019

@author: divyanshisingh
"""

a=float(input("enter first side of triangle"))
b=float(input("enter second side of triangle"))
c=float(input("enter third side of triangle"))
if a>b and b>c:
    if (a**2)==((b**2)+(c**2)):
        print("pythagoras triplet")
    else:
        print("not a pythagorus triplet")
elif b>c and c>a:
    if (b**2)==((a**2)+(c**2)):
        print("pythagoras triplet")
    else:
        print("not a pythagorus triplet")    
else:
    if (c**2)==((a**2)+(b**2)):
        print("pythagoras triplet")
    else:
        print("not a pythagorus triplet")
        
    
