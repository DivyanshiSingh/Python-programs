#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: divyanshisingh
"""
from tkinter import *
def disp():
    a=float(t1.get())
    b=float(t2.get())
    c=a+b
    t3.delete(0,"end")
    t3.insert(0,c)
root=Tk()
root.title("ADD")
root.geometry("400x400")
root.configure(bg="blue")
t1=Entry(width="30",bg="white",fg="red",font=("bold",20))
t2=Entry(width="30",bg="white",fg="red",font=("bold",20))
t3=Entry(width="30",bg="white",fg="red",font=("bold",20))
b=Button(text="Add",width="30",bg="black",font=("bold",20),command=disp)
t1.place(x=10,y=50)
t2.place(x=500,y=50)
t3.place(x=10,y=150)
b.place(x=60,y=300)
root.mainloop()

