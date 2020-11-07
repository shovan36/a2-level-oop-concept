import sounddevice as sd
import soundfile as sf
from tkinter import *
 
def voice_rec():
    fs= 48000
    duration = 5
    myrecording = sd.rec(int(duration*fs),samplerate=fs,channels=2)
    sd.wait()

    return sf.write('my_audio_file',myrecording,fs)
master = voice_rec()
label (master,text="voice recorder :"
).grid(row =0,sticky=w,rowspan=5 ) 
b= button(master,text="start",command=voice_rec)
b.grid (row = 0,column=2,columnspan=2,rowspan=2,padx=5,pady=5)
mainloop() 
