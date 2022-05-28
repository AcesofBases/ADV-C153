# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:01:02 2022

@author: Ace
"""

from tkinter import *
import random

root=Tk()

root.title("Random Password Generator")
root.geometry("400x400")

entry=Entry(root)
label=Label(root,text="Guessed Password: ")
label1=Label(root,text="Generated Password: ")

entry_var=entry
label_var=label

array_3d=[[
    [1,2,3,4,5,6],
    ["You","Me"],
    ["A","B","C","D","E","F","G","H"]
    ],[
    ["*","%","@","&","$"],
    ["Bowl","Cup"],
    ["T","P","D","H","B"]
    ]
    ]


def new_password():
    guessed_password=entry.get()
    label["text"]="Generated Password: " +str(guessed_password)
    random_number1=random.randint(0,5)
    random_number2=random.randint(0,1)
    random_number3=random.randint(0,7)
    
    random_number4=random.randint(0,4)
    random_number5=random.randint(0,1)
    random_number6=random.randint(0,4)
    letter1=str(array_3d[0][0][random_number1])
    letter2=(array_3d[0][1][random_number2])
    letter3=(array_3d[0][2][random_number3])
    
    letter4=(array_3d[1][0][random_number4])
    letter5=(array_3d[1][1][random_number5])
    letter6=(array_3d[1][2][random_number6])
    
    
    label1["text"]=letter1+letter2+letter3+letter4+letter5+letter6

btn=Button(root,text="Generate Random Password",command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.4,anchor=CENTER)
entry.place(relx=0.5,rely=0.3,anchor=CENTER)
label1.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()