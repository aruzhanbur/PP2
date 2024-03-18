from tkinter import *
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title("Music Player")
root.geometry("500x330")

pygame.mixer.init()

topbar = Menu(root)
root.config(menu=topbar)

songs = []
currsong = ""
pause = False

def loadm():
    global currsong
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

    songlist.delete(0, END)
    for song in songs:
        songlist.insert(END, song)

    songlist.select_set(0)
    currsong = songs[0]

def on_song_select(event):
    global currsong
    selected_song_index = songlist.curselection()[0]
    currsong = songs[selected_song_index]
    

def playm():
    global currsong, pause
    if not pause:
        pygame.mixer.music.load(os.path.join(root.directory, currsong))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        pause = False
        
def pausem():
    global pause
    pygame.mixer.music.pause()
    pause = True

def nextm():
    global currsong, pause
    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(currsong) + 1)
        currsong = songs[songlist.curselection()[0]]
        playm()
    except:
        pass

def prev():
    global currsong, pause
    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(currsong) + 1)
        currsong = songs[songlist.curselection()[0]]
        playm
    except:
        pass

org = Menu(topbar, tearoff=False)
org.add_command(label = "Select folder", command=loadm)
topbar.add_cascade(label="Organise", menu = org)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.bind("<<ListboxSelect>>", on_song_select)
songlist.pack()

playimg = PhotoImage(file="a.png")
stopimg = PhotoImage(file="d.png")
nextimg = PhotoImage(file="c.png")
previmg = PhotoImage(file="b.png")

framecontr = Frame(root)
framecontr.pack()

playb = Button(framecontr, image=playimg, borderwidth=0, command=playm)
stopb = Button(framecontr, image=stopimg, borderwidth=0, command=pausem)
nextb = Button(framecontr, image=nextimg, borderwidth=0, command=nextm)
prevb = Button(framecontr, image=previmg, borderwidth=0, command=prev)

playb.grid(row=0,column=1, padx=7, pady = 10)
stopb.grid(row=0,column=2, padx=7, pady = 10)
nextb.grid(row=0,column=3, padx=7, pady = 10)
prevb.grid(row=0,column=0, padx=7, pady = 10)

root.mainloop()