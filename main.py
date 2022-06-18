from ctypes import sizeof
# from moviepy.editor import mp
from tkinter import *
from tkinter import ttk
from tkvideo import tkvideo
import pydub
from pydub import AudioSegment
from scipy.io.wavfile import write
import glob
import sounddevice
import soundfile
import os
#import vlc
import pygame
import playsound
import subprocess, sys
from bvPlayer import bvPlayer

#AudioSegment.converter = '/usr/local/Cellar/ffmpeg/5.0.1_2/bin/ffmpeg'

def recordVoice():
    fs = 44100
    duration = 5
    recording = sounddevice.rec(int(duration * fs), samplerate = fs, channels=1)
    sounddevice.wait() 
    write('user_output.wav', fs, recording)
    ## if windows IGNORE
    # os.startfile("user_output.wav") IGNORE
    ## Uncomment below if you want recorded file to play IGNORE
    # opener = "open" if sys.platform == "darwin" else "xdg-open" IGNORE
    # subprocess.call([opener, 'user_output.wav']) IGNORE
    sound = AudioSegment.from_wav('user_output.wav')
    return sound.export('user_output.wav', format='wav')

def parseText():
    parsedText = textBox.get('1.0','end')
    ##print(parsedText)
    ## Text is here, send this to the program
    ## or make it a file and then send, however matts program works

def displayResponse():
    ## Grab mp4 from videos file
    ## NOTE - reroute voca to drop the mp4 into the videos file in this project
    # pygame.init()
    # pygame.display.set_caption('Show Video on screen')
    # video = mp.VideoFileClip('*.mp4')
    # video.preview()
    # pygame.quit()
    vids = glob.glob("*.mp4")
    bvPlayer(vids[0], videoOptions=True, dim=(512,512), pos = (200,200), draggable=True, videoOption=True)
    
    # vidToDisplay = ""
    # vids = glob.glob("*.mp4")
    #dst = "converted.wav"
    # creating vlc media player object
    #media = vlc.MediaPlayer("1.mp4")
    
    # convert mp3 to wav
    # sound = AudioSegment.from_mp3(vids[0])
    # sound.export(dst, format="wav")
    
    # label = Label(root)
    # label.grid(column=3,row=0)
    # playVid = tkvideo.tkvideo(, label, loop=1, size=(512,512))
    # song = AudioSegment.from_wav("*.mp4")
    # print('playing sound using  pydub')
    # play(song)
    # playsound('*.mp4')
    # print('playing sound using  playsound')
    # start playing video
    #media.play()
    # for vid in vids:
    #     vidToDisplay = vid
    # print(vidToDisplay)
    # label = Label(root)
    # label.grid(column=3,row=0)
    # playVid = tkvideo.tkvideo(bvPlayer(vids[0], dim=(350,350)), label, loop=1, size=(300,300))
    # playVid.play()

root = Tk()
root.title("Voca Talks!")
root.geometry("900x700")
print(root)

frm = ttk.Frame(root, padding=10)
frm.grid()

textBox = Text(frm, height=20, width=50)
textBox.grid(column=0, row=1)

ttk.Button(frm, text="Parse Text", command=parseText).grid(column=0, row=2)
ttk.Button(frm, text="Record Voice", command=recordVoice).grid(column=0, row=3)
ttk.Button(frm, text="Listen to response", command=displayResponse).grid(column=0,row=4)

# my_label = Label(root)
# my_label.pack()
# player = tkvideo.tkvideo("video.mp4", my_label, loop = 1, size = (1280,720))
# player.play()
 

##ttk.Label(frm, text="Hello World!").grid(column=0, row=0) IGNORE
##ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1) IGNORE

root.mainloop()

