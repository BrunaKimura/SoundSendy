import soundfile as sf
import sounddevice as sd
import math
from scipy.fftpack import fft, ifft
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg

def LPF(signal, cutoff_hz, fs):
        #####################
        # Filtro
        #####################
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))
#comecei 

def read_audio(location):
    return sf.read(location)

def genetate_portadora(frequency):
    portadora= []
    times = np.linspace(0, 44100,5000)
    for i in   times:
        portadora.append(math.cos(frequency*2*math.pi*i))
    return portadora

def modulate(frequency,data):
    times = np.linspace(0,len(data)/frequency,len(data))
    mc = np.sin(2*np.pi*frequency*times)
    return mc*data

def returnXdata(sound):
    return np.linspace(0,len(sound)/44100,len(sound))


print('grave o primeiro aúdio(3 segundos')
audio1 = sd.rec(int(3*44100), 44100, channels=1)
sd.wait()
first_audio = audio1[:,0]

print('grave o segundo audio (3 segundos)')
audio = sd.rec(int(3*44100), 44100, channels=1)
sd.wait()
second_audio = audio[:,0]

print('aguarde as analises')

first = LPF(first_audio,4000,44100)
second = LPF(second_audio,4000,44100)
print('modulando...')
modulated_audio_one = modulate(7000,first)
modulated_audio_two = modulate(13000,second)

print('somando audio final....')
resultant_audio  = []
for i in range(0,len(modulated_audio_one)):
    resultant_audio.append(modulated_audio_one[i] + modulated_audio_two[i])
# print(resultant_audio)
print('reproduzindo audio final....')
sd.play(resultant_audio,44100)
sd.wait()

# plots
plt.title('Aúdio 1 filtro passa baixa aplicado')
plt.plot(returnXdata(first),first)
plt.show()
#--------------------------
plt.title('Aúdio 2 filtro passa baixa aplicado')
plt.plot(returnXdata(second),second)
plt.show()
#----------------------------
plt.title('Aúdio 1 filtro passa baixa aplicado (Fourrier')
first_audio = fft(first)
first_audio = np.concatenate([first_audio[len(first_audio) // 2:len(first_audio)] ,first_audio[0:len(first_audio) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(first_audio)),first_audio)
plt.show()
#----------------------------
plt.title('Aúdio 2 filtro passa baixa aplicado (Fourrier')
second_audio = fft(second)
second_audio = np.concatenate([second_audio[len(second_audio) // 2:len(second_audio)] ,second_audio[0:len(second_audio) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(second_audio)),second_audio)
plt.show()
#----------------------------
plt.title('Portadora 1 (7000)')
plt.plot(genetate_portadora(7000))
plt.show()
#-----------------------------
plt.title('Portadora 2 (13000)')
plt.plot(genetate_portadora(13000))
plt.show()
#-----------------------------
plt.title('audio 1 modulado no tempo')
plt.plot(returnXdata(modulated_audio_one),modulated_audio_one)
plt.show()
#-------------------------------
plt.title('audio 2 modulado no tempo')
plt.plot(returnXdata(modulated_audio_two),modulated_audio_two)
plt.show()
#---------------------------------
plt.title('Aúdio 1 modulado (Fourrier')
modulated_audio_one = fft(modulated_audio_one)
modulated_audio_one = np.concatenate([modulated_audio_one[len(modulated_audio_one) // 2:len(modulated_audio_one)] ,modulated_audio_one[0:len(modulated_audio_one) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(modulated_audio_one)),modulated_audio_one)
plt.show()
#-----------------------------------
plt.title('Aúdio 2 modulado (Fourrier')
modulated_audio_two = fft(modulated_audio_two)
modulated_audio_two = np.concatenate([modulated_audio_two[len(modulated_audio_two) // 2:len(modulated_audio_two)] ,modulated_audio_two[0:len(modulated_audio_two) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(modulated_audio_two)),modulated_audio_two)
plt.show()
#------------------------------------
plt.title("Fourier dos sinais modulados somados")
resultant_audio = fft(resultant_audio)
resultant_audio = np.concatenate([resultant_audio[len(resultant_audio) // 2:len(resultant_audio)] ,resultant_audio[0:len(resultant_audio) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(resultant_audio)),resultant_audio)
plt.show()