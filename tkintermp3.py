#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as tk
import pyglet
import random
import os
import time
from threading import Thread
from tkFileDialog import askdirectory
import pygame
from mutagen.id3 import ID3
import tkMessageBox
import arrow
import calendar
import requests, bs4
import Sign_Detection_Function
from Sign_Detection_Function import Images_Capture



class Question():

    def __init__(self, main):

        self.label1 = Label(main, width=25, font=3, text="Выберите действие")
        self.Sign_Detection = Button(main, text="Режим распознавания жестов", width=30, height=15)
        self.Music_Run = Button(main, text="Режим воспроизведения музыки", width=30, height=15)
        self.Weather_Forecast = Button(main, text="Режим прогноза погоды", width=30, height=15)
        self.Calendar = Button(main, text="Календарь", width=30, height=15)

        self.label1.grid(row=0, column=1)
        self.Sign_Detection.grid(row=1, column=1)
        self.Music_Run.grid(row=1, column=2)
        self.Weather_Forecast.grid(row=2, column=1)
        self.Calendar.grid(row=2, column=2)

        self.Sign_Detection.bind("<Button-1>", self.answer_sign)
        self.Music_Run.bind("<Button-1>", self.answer_music)
        self.Weather_Forecast.bind("<Button-1>", self.answer_weather)
        self.Calendar.bind("<Button-1>", self.answer_calendar)


    def answer_sign(self, event):
        print("Sign")
        root.withdraw()
        root1.deiconify()
        Child_Sign(root1)
        Images_Capture()

    def answer_music(self, event):
        print("Music")
        root.withdraw()
        root5.deiconify()


    def answer_weather(self, event):
        print("Weather")
        root.withdraw()
        root3.deiconify()
        Child_Weather(root3)

    def answer_calendar(self, event):
        print("Calendar")
        root.withdraw()
        root4.deiconify()
        Child_Calendar(root4)


class Child_Sign():

    def __init__(self, main2):
        self.label_Sign = Label(main2, width=25, font=3, text="Режим распознавания жестов")
        self.label_Sign.grid(row=0, column=2)
        self.Btn_Sign = Button(main2, text="Назад в меню", width=45, height=15)
        self.Btn_Sign.grid(row=1, column=2)
        self.Btn_Sign.bind("<Button-1>", self.back_from_sign)

    def back_from_sign(self, event):

        Question(root)
        root1.withdraw()
        root.deiconify()

class Child_Music():

    def __init__(self, main3):
        self.label_Music = Label(main3, width=35, font=3, text="Режим воспроизведения музыки")
        self.label_Music.grid(row=0, column=2)
        self.Btn_Music = Button(main3, text="Назад в меню", width=45, height=15)
        self.Btn_Music.grid(row=1, column=2)
        self.Btn_Music.bind("<Button-1>", self.back_from_music)

    def back_from_music(self, event):

        Question(root)
        root2.withdraw()
        root.deiconify()


class Child_Weather():

    def __init__(self, main4):
        self.label_Weather = Label(main4, width=25, font=3, text="Режим прогноза погоды")
        self.label_Weather.grid(row=0, column=2)
        self.weather_text = Text(main4, height=8, width=60)
        self.weather_text.grid(row=3, column=2)
        self.weather_text.insert(END, "Morning " + pogoda1 + " " + pogoda2 + "\n")
        self.weather_text.insert(END, "Day " + pogoda3 + " " + pogoda4 + "\n")
        self.weather_text.insert(END, pogoda.strip())
        self.Btn_Weather = Button(main4, text="Назад в меню", width=25, height=1)
        self.Btn_Weather.grid(row=1, column=2)
        self.Btn_Weather.bind("<Button-1>", self.back_from_weather)

    def back_from_weather(self, event):

        Question(root)
        root3.withdraw()
        root.deiconify()

class Child_Calendar():

    def __init__(self, main5):
        self.label_Calendar = Label(main5, width=25, font=3, text="Календарь")
        self.label_Calendar.grid(row=0, column=2)
        self.date_text = Text(main5, height=8,width=21)
        self.date_text.grid(row=3, column=2)
        self.date_text.insert(END, calendar.month(year, month))
        self.Btn_Calendar = Button(main5, text="Назад в меню", width=25, height=1)
        self.Btn_Calendar.grid(row=4, column=2)
        self.Btn_Calendar.bind("<Button-1>", self.back_from_calendar)

    def back_from_calendar(self, event):

        Question(root)
        root4.withdraw()
        root.deiconify()

year_and_month = arrow.now().format('YYYY-MM')
year = int(year_and_month[:4])
month = int(year_and_month[5:])
full_date = calendar.month(year, month)
s=requests.get('https://sinoptik.com.ru/погода-томск')
b=bs4.BeautifulSoup(s.text, "html.parser")
p3=b.select('.temperature .p3')
pogoda1=p3[0].getText()
p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()
p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()
p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()
p=b.select('.rSide .description')
pogoda=p[0].getText()




root = Tk()
root1 = tk.Toplevel()
root2 = tk.Toplevel()
root3 = tk.Toplevel()
root4 = tk.Toplevel()
root5 = tk.Toplevel()
root5.minsize(500,500)
root5.title("Music Player")
root1.withdraw()
root2.withdraw()
root3.withdraw()
root4.withdraw()
root5.withdraw()






listofsongs=[]
realnames = []

v =StringVar()
songlabel =Label(root5,textvariable=v,width=80)
index=0
count=0

global ctr
ctr=0


def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    #return songname

def pausesong(event):
    global ctr
    ctr += 1
    if (ctr%2!=0):
        pygame.mixer.music.pause()
    if(ctr%2==0):
        pygame.mixer.music.unpause()

def playsong(event):
    pygame.mixer.music.play()

def backfromplayer(event):
    Question(root)
    root5.withdraw()
    root.deiconify()
    pygame.mixer.music.pause()

def nextsong(event):
    global index
    index += 1
    if (index < count):
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    else:
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    try:
      updatelabel()
    except NameError:
        print("")

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    try:
        updatelabel()
    except NameError:
        print("")


def stopsong(event):

    pygame.mixer.music.stop()
    #v.set("")
    #return songname
def mute(event):
    vol.set(0)



label = Label(root5,text="Music Player")
label.pack

listbox=Listbox(root5,selectmode=MULTIPLE,width=100,height=20,bg="grey",fg="black")
listbox.pack


def directorychooser():
  global count
  global index
    #count=0

  directory = askdirectory()
  if(directory):
    count=0
    index=0
    #listbox.delete(0, END)
    del listofsongs[:]
    del realnames[:]

    os.chdir(directory)

    for  files in os.listdir(directory):

        try:
         if files.endswith(".mp3"):

              realdir = os.path.realpath(files)
              audio = ID3(realdir)
              realnames.append(audio['TIT2'].text[0])
              listofsongs.append(files)
        except:
            print(files+" is not a song")

    if listofsongs == [] :
       okay=tkMessageBox.askretrycancel("No songs found","no songs")
       if(okay==True):
           directorychooser()

    else:
        listbox.delete(0, END)
        realnames.reverse()
        for items in realnames:
            listbox.insert(0, items)
        for i in listofsongs:
            count = count + 1
        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[0])

        pygame.mixer.music.play()
        try:
            updatelabel()
        except NameError:
            print("")
  else:
    return 1

try:
        directorychooser()
except WindowsError:
         print("thank you")

def call(event):


 if(True):
    try:
        #pygame.mixer.music.stop()
        k=directorychooser()

    except WindowsError:
         print("thank you")

realnames.reverse()

songlabel.pack

def show_value(self):
    i = vol.get()
    pygame.mixer.music.set_volume(i)

vol = Scale(root5,from_ = 10,to = 0,orient = VERTICAL ,resolution = 10,command = show_value)
vol.place(x=85, y = 380)
vol.set(10)

framemiddle = Frame(root5,width=250,height=30)
framemiddle.pack()

framedown = Frame(root5,width=400,height=300)
framedown.pack()

openbutton = Button(framedown,text="open")
openbutton.pack(side=LEFT)

mutebutton = Button(framedown,text=u"12131")
mutebutton.pack(side=LEFT)

previousbutton = Button(framedown,text="◄◄")
previousbutton.pack(side=LEFT)

playbutton = Button(framedown,text="►")
playbutton.pack(side=LEFT)

stopbutton = Button(framedown,text="■")
stopbutton.pack(side=LEFT)

nextbutton = Button(framedown,text="►►")
nextbutton.pack(side=LEFT)

pausebutton = Button(framedown,text="►/║║")
pausebutton.pack(side=LEFT)

backtomenu_button = Button(framedown, text="Back to menu")
backtomenu_button.pack(side=LEFT)

backtomenu_button.bind("<Button-1>", backfromplayer)
mutebutton.bind("<Button-1>", mute)
openbutton.bind("<Button-1>", call)
playbutton.bind("<Button-1>", playsong)
nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", previoussong)
stopbutton.bind("<Button-1>", stopsong)
pausebutton.bind("<Button-1>", pausesong)
pygame.mixer.music.pause()
#Sign_Detection = Button(root, text="Режим распознавания жестов", width=30, height=15)
#Sign_Detection.grid(row=1, column=1)
q = Question(root)
root.title("Main menu")
root.mainloop()


