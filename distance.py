#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:16:45 2019

@author: divyanshisingh
"""

a=int(input("enter distance in feet"))
b=int(input("enter distance in inch"))
c=int(input("enter another distance in feet"))
d=int(input("enter another distance in inch"))
e=a+c;
f=b+d;
if f>=12:
    h=f%12;
    g=f//12;
    i=e+g;
    print("feet=",i,"inch=",h)
else:
    print("feet=",e,"inch=",f)
