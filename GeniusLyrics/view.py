import tkinter
from tkinter import ttk
import pygame
import GeniusLyrics.Genius as Genius
import threading as thread

## Pygame Start ##
pygame.mixer.init(48000, -16, 1, 1024)

class Pause(object):

    def __init__(self):
        self.paused = pygame.mixer.music.get_busy()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused

PAUSE = Pause()

def plussecs(*args):
    pygame.mixer.music.set_pos(pygame.mixer.music.get_pos()+5)

def minussecs(*args):
    pygame.mixer.music.set_pos(pygame.mixer.music.get_pos()-5)

def getsongs(*args):
    song = entrvar.get()
    entrvar_temp.set(entrvar.get())
    songlist = Genius.listMusic(song)
    musiclist.set(songlist)

def downloadSong(*args):
    pos = int(mus_listbox.curselection()[0])
    songlink = Genius.getMusic(entrvar_temp.get(), pos+1)
    title = Genius.downloadMusic(songlink)
    pygame.mixer.music.load(title)
    pygame.mixer.music.play()




root =  tkinter.Tk()





musiclist = tkinter.StringVar()
entrvar = tkinter.StringVar()
entrvar_temp = tkinter.StringVar()
mainframe = ttk.Frame(root)

titlbl = ttk.Label(mainframe, text="Seja bem vindo, digite o nome da música que desejas!")
mus_entr = ttk.Entry(mainframe, textvariable = entrvar,width=60)
mus_entr.bind("<Return>",lambda *args : thread.Thread(target=lambda : getsongs()).start())
mus_listbox = tkinter.Listbox(mainframe, background="purple", foreground="white", listvariable = musiclist, height=5,width=60)
mus_listbox.bind('<<ListboxSelect>>',lambda *args : thread.Thread(target=lambda : downloadSong()).start())
playPause_button = ttk.Button(mainframe,text="Play/Pause",command=PAUSE.toggle())
back_button = ttk.Button(mainframe,text="-5",command=lambda *args:thread.Thread(target=lambda :minussecs()).start())
forward_button = ttk.Button(mainframe,text="+5",command=lambda *args:thread.Thread(target=lambda :plussecs()).start())

mainframe.pack()
mus_entr.pack()
mus_listbox.pack()
back_button.pack(side="left")
playPause_button.pack(side="left",padx=70)
forward_button.pack(side="right")

root.mainloop()