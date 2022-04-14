from tkinter import *
from tkinter import font
import random
import time
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd
from tkinter import messagebox



plt.style.use('ggplot')

root = Tk()
root.title("Typing Speed Test")
root.geometry("290x150")
root.iconbitmap('E:\py.ico')


MODES = [
    ("Easy","Easy"),
    ("Medium","Medium"),
    ("Hard","Hard"),
    ("Coding","Coding")
    ]

initial = StringVar()
initial.set("Easy")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=initial,value=mode).pack(anchor=W)


def accuracy(s,t):
    flag = 0
    count = 0
    if len(s) < len(t):
         high = len(s)
        
         for i in range(0,high):
             if s[i] != t[i]:
                 flag += 1
                 
         subtract = len(t) - len(s)
         flag += subtract
                 
         count = 1
                 
    elif len(s) > len(t):
        high = len(t)
        
        for i in range(0,high):
             if s[i] != t[i]:
                 flag += 1
                 
        count = 2
                 
    else:
        for i in range(0,len(s)):
            if s[i] != t[i]:
                flag += 1
    
        count = 3 
    
    if count == 3:
        return flag
        
    if count == 2:
        sub = 0
        if flag == 0:
            minus = len(s) - len(t)
            sub = minus
            
            return minus
        
        else:
            return flag
        
    if count == 1:
        return flag




def compare(s,t):
    flag = 0
    count = 0
    if len(s) < len(t):
         high = len(s)
        
         for i in range(0,high):
             if s[i] == t[i]:
                 flag += 1
                 
         count = 1
                 
    elif len(s) > len(t):
        high = len(t)
        
        for i in range(0,high):
             if s[i] == t[i]:
                 flag += 1
                 
        count = 2
                 
    else:
        for i in range(0,len(s)):
            if s[i] == t[i]:
                flag += 1
    
        count = 3 
    
    if count == 3:
        return format((flag/len(t) * 100),'0.2f')
        
    if count == 2:
        sub = 0
        if flag == len(t):
            minus = len(s) - len(t)
            sub = (minus / len(t)) * 100
            
        return format(((flag/len(t)) * 100 - sub),'0.2f')
        
    if count == 1:
        return format((flag/len(t) * 100),'0.2f')

def view_graph(wpm,acc):
    x_index = ['User','Average','Professional']
    y_index = [float(wpm),44.5,87.5]

    plt.bar(x_index,y_index,color = '#444444')
    plt.title("Graph of WPM")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    x_index1 = ['User','Average','Professional']
    y_index1 = [float(acc),84.5,92]

    plt.bar(x_index1,y_index1,color = '#adad3b')
    plt.title("Graph of Accuracy")
    plt.tight_layout()
    plt.grid(True)
    plt.show()



def check_results(value,word,time_1,time_2):
    result_window = Toplevel()
    result_window.title("RESULTS")
    result_window.geometry("350x90")
    result_window.iconbitmap('E:\py.ico')

    time_in_minutes = (time_2 - time_1) / 60

    errors = accuracy(list(value),list(word))

    wpm = (len(word) / 5) / time_in_minutes - (errors/time_in_minutes)
    wpm_ans = format(wpm,'0.2f')
    acc = compare(list(value),list(word))

    if value == word:
        accuracy_label = Label(result_window,text="Accuracy: 100%\t\t").grid(row=0,column=0)
        wpm_label = Label(result_window,text="Words Per Minute: " + str(wpm_ans)).grid(row = 0, column = 1)

    else:
        accuracy_ = Label(result_window,text="Accuracy: "  + str(compare(list(value),list(word))) + "\t\t").grid(row=0,column=0)
        wpm_label = Label(result_window,text="Words Per Minute: " + str(wpm_ans)).grid(row = 0, column = 1)


    btn = Button(result_window,text="CLOSE",bg="gray",borderwidth=5,command=result_window.destroy).grid(row=2,column=0)
    btn_view_graphically = Button(result_window,text="View Graphical Results",bg='gray',borderwidth=5,command=lambda:view_graph(wpm_ans,acc)).grid(row=2,column=1)


def clicked(value):
    #myLabel = Label(root,text=value).pack(anchor=E)

    response = messagebox.askyesno("User Response","Are You Ready to Take the Test?")

    if response == 1:
        if value == "Easy":
            entry = ["A good way to increase your typing speed is to type easy sentences over and over.","Be sure not to look at the keyboard when you are typing. ","The modern-day computer has become an important part of our daily life.","Pollution is the addition of unwanted substances into the environment that can damage our Earth."]
            top = Toplevel()
            top.title("Enter the Words")
            top.geometry("1500x140")
            top.iconbitmap('E:\py.ico')

            no = random.randint(0,3)
            x = entry[no]
            word_to_be_entered = Label(top,text="Enter the sentence: " + entry[no]).grid(row=0,column=0)
            
            start = time.time()

            label = Label(top,text="Enter:").grid(row = 1,column = 0)
            e = Entry(top,width=100,borderwidth=15)
            e.grid(row=1,column=1)

            newLabel = Label(top,text="               ").grid(row=2,column=0)

            btn1 = Button(top,text="Close",bg="gray",padx=5,pady=5,borderwidth=5,command=top.destroy).grid(row=3,column=0)
            btn2 = Button(top,text="Check Results",bg="gray",padx=5,pady=5,borderwidth=5,command = lambda:check_results(e.get(),x,start,time.time())).grid(row=3,column=1)

    #for medium

        elif value == "Medium":
            entry = ["Faf DuPlessis got a century in first game but not in the next.","Practice, Perseverance and hard-work are the things needed to succeed","WASP - White Anglo-Saxon Protestant.Many citizens in the Colonial Era were WASPs.","MACUSA - Magical Congress of the United States of America"]
            top = Toplevel()
            top.title("Enter the Words")
            top.geometry("1500x140")
            top.iconbitmap('E:\py.ico')

            no = random.randint(0,3)
            x = entry[no]
            word_to_be_entered = Label(top,text="Enter the sentence: " + entry[no]).grid(row=0,column=0)
            
            start = time.time()

            label = Label(top,text="Enter:").grid(row = 1,column = 0)
            e = Entry(top,width=100,borderwidth=15)
            e.grid(row=1,column=1)

            newLabel = Label(top,text="               ").grid(row=2,column=0)

            btn1 = Button(top,text="Close",bg="gray",padx=5,pady=5,borderwidth=5,command=top.destroy).grid(row=3,column=0)
            btn2 = Button(top,text="Check Results",bg="gray",padx=5,pady=5,borderwidth=5,command = lambda:check_results(e.get(),x,start,time.time())).grid(row=3,column=1)

    #for Hard

        elif value == "Hard":
            entry = ["He departed to Chennai on 17th May 2021 at 2:02pm and reached Trichy.","If we take the value of Pi as 3.14, then the area of circle with radius 1cm is 3.14cm^2.","CARE package: Cooperative for American Remittances to Europe","The speed of light is 299,792 kilometre per second!","Please email me before 15th August to my email email_123@gmail.com"]
            top = Toplevel()
            top.title("Enter the Words")
            top.geometry("1500x140")
            top.iconbitmap('E:\py.ico')

            no = random.randint(0,4)
            x = entry[no]
            word_to_be_entered = Label(top,text="Enter the sentence: " + entry[no]).grid(row=0,column=0)
            
            start = time.time()

            label = Label(top,text="Enter:").grid(row = 1,column = 0)
            e = Entry(top,width=100,borderwidth=15)
            e.grid(row=1,column=1)



            newLabel = Label(top,text="               ").grid(row=2,column=0)

            btn1 = Button(top,text="Close",bg="gray",padx=5,pady=5,borderwidth=5,command=top.destroy).grid(row=3,column=0)
            btn2 = Button(top,text="Check Results",bg="gray",padx=5,pady=5,borderwidth=5,command = lambda:check_results(e.get(),x,start,time.time())).grid(row=3,column=1) 

    #for Coding

        elif value == "Coding":
            entry = ["var replace = require('gulp-replace');","const AnalyticsSources = helpers.get_Analysis_Sources();","myObj = {'pet':'cat','age':6};","x_ = re.search('^The.*Pizza@$',txt);"]
            top = Toplevel()
            top.title("Enter the Words")
            top.geometry("1500x140")
            top.iconbitmap('E:\py.ico')

            no = random.randint(0,3)
            x = entry[no]
            word_to_be_entered = Label(top,text="Enter the sentence: " + entry[no]).grid(row=0,column=0)
            
            start = time.time()

            label = Label(top,text="Enter:").grid(row = 1,column = 0)
            e = Entry(top,width=100,borderwidth=15)
            e.grid(row=1,column=1)


            newLabel = Label(top,text="               ").grid(row=2,column=0)

            btn1 = Button(top,text="Close",bg="gray",padx=5,pady=5,borderwidth=5,command=top.destroy).grid(row=3,column=0)
            btn2 = Button(top,text="Check Results",bg="gray",padx=5,pady=5,borderwidth=5,command = lambda:check_results(e.get(),x,start,time.time())).grid(row=3,column=1) 





myButton = Button(root,text="Submit",bg="gray",padx=5,pady=5,borderwidth=5,command = lambda:clicked(initial.get())).pack()
#btn_close = Button(root,text="close",bg="gray",padx=5,pady=5,borderwidth=5,command=root.destroy).pack()



root.mainloop()