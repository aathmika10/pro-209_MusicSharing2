import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from playsound import playsound
import pygame
from pygame import mixer

import os
import time

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None
songCounter=0


def play():
    global songSelected
    songSelected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+songSelected)
    mixer.music.play()
    if(songSelected!=""):
        infoLabel.configure(text="Now playing"+songSelected)
    else:
        infoLabel.configure(text="")

def stop():
    global songSelected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+songSelected)
    mixer.music.pause()
    infoLabel.configure(text="")


def musicWindow():

   
    print("\n\t\t\t\tMUSIC WINDOW")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    global selectlabel
    global listbox
    global textarea
    global labelchat
    global text_message
    global infoLabel

    selectlabel = Label(window, text= "Select Song",bg="LightSkyBlue", font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg="LightSkyBlue", borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=18)

    for file in os.listdir('shared_files'):
        fileName=os.fsdecode(file)
        listbox.insert(songCounter,fileName)
        songCounter=songCounter+1

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",width=10,bd=1,bg="skyBlue" ,font = ("Calibri",10),command=play)
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="Stop",width=10,bd=1,bg="skyBlue" ,font = ("Calibri",10),command=stop)
    stopButton.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=10,bd=1,bg="skyBlue", font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",width=10,bd=1,bg="skyBlue", font = ("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel=Label(window,text="",fg="blue",font=("Calibri",8))
    infoLabel.place(x=4,y=200)  
  
    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()
