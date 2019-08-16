#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:20:19 2019

@author: divyanshisingh
"""

import re
pattern='^([a-z]|[A-Z]|[0-9])+\.*\_*([a-z]|[A-Z]|[0-9])*\@{1}([a-z]|[A-Z])+\.{1}([a-z])+$'
test_string=str(input("enter the email"))
result=re.match(pattern,test_string)
if result:
    print("search successful: valid email")
else:
    print("search unsuccessful: invalid email")
