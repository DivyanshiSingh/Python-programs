#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:07:26 2019

@author: divyanshisingh
"""

from tkinter import *

op1=""
op2=""
op=""
k=0

def calc():
    global op1,op2,op
    a=float(op1)
    b=float(op2)
    c=0
    if op=="+":
        c=a+b
    elif op=="-":
        c=a-b
    elif op=="/":
        c=a/b
    else :
        c=a*b
    t1.delete(0,"end")
    t1.insert(0,"%.2f" % c)
    
    
def onClick(event):
    global op1,op2,op,k
    b=event.widget
    if b==b0 or b==b1 or b==b2 or b==b3 or b==b4 or b==b5 or b==b6 or b==b7 or b==b8 or b==b9:
        if k==0:
            t1.delete(0,"end")
            t1.insert(0,b.cget("text"))
            k=1
        else:
            t1.insert("end",b.cget("text"))
    elif b==bplus or b==bmin or b==bdiv or b==bmul:
        op1=t1.get()
        op=b.cget("text")
        k=0
    elif b==bequal:
        op2=t1.get()
        calc()

from tkinter import *
root=Tk()
root.geometry("200x300")
root.title("Cal")
t1=Entry(width="10",font=("bold",20))
b0=Button(bg="#F0E68C",text="0",width="2",font=("bold",10))
b1=Button(bg="#F0E68C",text="1",width="2",font=("bold",10))
b2=Button(bg="#F0E68C",text="2",width="2",font=("bold",10))
b3=Button(bg="#F0E68C",text="3",width="2",font=("bold",10))
b4=Button(bg="#F0E68C",text="4",width="2",font=("bold",10))
b5=Button(bg="#F0E68C",text="5",width="2",font=("bold",10))
b6=Button(bg="#F0E68C",text="6",width="2",font=("bold",10))
b7=Button(bg="#F0E68C",text="7",width="2",font=("bold",10))
b8=Button(bg="#F0E68C",text="8",width="2",font=("bold",10))
b9=Button(bg="#F0E68C",text="9",width="2",font=("bold",10))
bplus=Button(bg="#F0E68C",text="+",width="2",font=("bold",10))
bdiv=Button(bg="#F0E68C",text="/",width="2",font=("bold",10))
bmin=Button(bg="#F0E68C",text="-",width="2",font=("bold",10))
bmul=Button(bg="#F0E68C",text="*",width="2",font=("bold",10))
bequal=Button(bg="#F0E68C",text="=",width="2",font=("bold",10))
bdot=Button(bg="#F0E68C",text=".",width="2",font=("bold",10))
t1.place(x=10,y=30)
b7.place(x=10,y=80)
b8.place(x=50,y=80)
b9.place(x=90,y=80)
bplus.place(x=130,y=80)
b4.place(x=10,y=120)
b5.place(x=50,y=120)
b6.place(x=90,y=120)
bmin.place(x=130,y=120)
b3.place(x=10,y=160)
b2.place(x=50,y=160)
b1.place(x=90,y=160)
bdiv.place(x=130,y=160)
b0.place(x=10,y=200)
bdot.place(x=50,y=200)
bequal.place(x=90,y=200)
bmul.place(x=130,y=200)

b0.bind("<Button-1>",onClick)
b1.bind("<Button-1>",onClick)
b2.bind("<Button-1>",onClick)
b3.bind("<Button-1>",onClick)
b4.bind("<Button-1>",onClick)
b5.bind("<Button-1>",onClick)
b6.bind("<Button-1>",onClick)
b7.bind("<Button-1>",onClick)
b8.bind("<Button-1>",onClick)
b9.bind("<Button-1>",onClick)
bplus.bind("<Button-1>",onClick)
bmin.bind("<Button-1>",onClick)
bdiv.bind("<Button-1>",onClick)
bmul.bind("<Button-1>",onClick)
bdot.bind("<Button-1>",onClick)
bequal.bind("<Button-1>",onClick)

root.configure(bg="#FF6347")
root.mainloop()