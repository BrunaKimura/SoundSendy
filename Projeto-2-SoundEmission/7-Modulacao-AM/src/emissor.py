import soundfile as sf
import sounddevice as sd
import math
from scipy.fftpack import fft, ifft
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg

def LPF(signal, cutoff_hz, fs):
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))

def read_audio(location):
    return sf.read(location)

def genetate_portadora(frequency):
    portadora= []
    times = np.linspace(0, 44100,5000)
    for i in   times:
        portadora.append(math.cos(frequency*2*math.pi*i))
    return portadora

def modulate(freq,signal):
    audio =signal
    if(not isinstance(signal[0], float)):
         audio = signal[:,0]
    ts = np.linspace(0,len(audio) / 44100,len(audio))
    audio = audio*np.sin(2*math.pi*freq*ts)
    return audio

def returnXdata(sound):
    return np.linspace(0,len(sound)/44100,len(sound))

def Path(name):
    return "./Save/{0}.wav".format(name)#audio + ".wav"

first_audio, fs = sf.read(Path("soundm1"))
print(first_audio)
#first_audio = first_audio[0,:]

second_audio, fs = sf.read(Path("soundm2"))
print(second_audio)
#second_audio = second_audio[0,:]

print('Aguarde as analises')

first = LPF(first_audio,3000,44100)
second = LPF(second_audio,3000,44100)


print('Audio 1')
sd.play(first)
sd.wait()

print('Audio 2')
sd.play(second)
sd.wait()

print('Modulando...')
modulated_audio_one = modulate(5000,first)
modulated_audio_two = modulate(14000,second)

print('Somando audio final....')
resultant_audio  = []
for i in range(0,len(modulated_audio_one)):
    resultant_audio.append(modulated_audio_one[i] + modulated_audio_two[i])
# print(resultant_audio)
print('Reproduzindo audio final....')
sd.play(resultant_audio,44100)
sd.wait()

# plots
plt.title('Aúdio 1 filtro passa baixa aplicado')
plt.plot(returnXdata(first),first)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg1"), dpi = 72)
plt.show()
#--------------------------
plt.title('Aúdio 2 filtro passa baixa aplicado')
plt.plot(returnXdata(second),second)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg2"), dpi = 72)
plt.show()
#----------------------------
plt.title('Aúdio 1 filtro passa baixa aplicado (Fourrier')
first_audio = np.abs(fft(first))
first_audio = np.concatenate([first_audio[len(first_audio) // 2:len(first_audio)] ,first_audio[0:len(first_audio) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(first_audio)),first_audio)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg3"), dpi = 72)
plt.show()
#----------------------------
plt.title('Aúdio 2 filtro passa baixa aplicado (Fourrier')
second_audio = np.abs(fft(second))
second_audio = np.concatenate([second_audio[len(second_audio) // 2:len(second_audio)] ,second_audio[0:len(second_audio) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(second_audio)),second_audio)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg4"), dpi = 72)
plt.show()
#----------------------------
plt.title('Portadora 1 (5000)')
plt.plot(genetate_portadora(5000))
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg5"), dpi = 72)
plt.show()
#-----------------------------
plt.title('Portadora 2 (1000)')
plt.plot(genetate_portadora(10000))
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg6"), dpi = 72)
plt.show()
#-----------------------------
plt.title('audio 1 modulado no tempo')
plt.plot(returnXdata(modulated_audio_one),modulated_audio_one)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg7"), dpi = 72)
plt.show()
#-------------------------------
plt.title('audio 2 modulado no tempo')
plt.plot(returnXdata(modulated_audio_two),modulated_audio_two)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg8"), dpi = 72)
plt.show()
#---------------------------------
plt.title('Aúdio 1 modulado (Fourrier')
modulated_audio_one = np.abs(fft(modulated_audio_one))
modulated_audio_one = np.concatenate([modulated_audio_one[len(modulated_audio_one) // 2:len(modulated_audio_one)] ,modulated_audio_one[0:len(modulated_audio_one) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(modulated_audio_one)),modulated_audio_one)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg9"), dpi = 72)
plt.show()
#-----------------------------------
plt.title('Aúdio 2 modulado (Fourrier')
modulated_audio_two = np.abs(fft(modulated_audio_two))
modulated_audio_two = np.concatenate([modulated_audio_two[len(modulated_audio_two) // 2:len(modulated_audio_two)] ,modulated_audio_two[0:len(modulated_audio_two) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(modulated_audio_two)),modulated_audio_two)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg10"), dpi = 72)
plt.show()
#------------------------------------
plt.title("Fourier dos sinais modulados somados")
resultant_audio = np.abs(fft(resultant_audio))
resultant_audio = np.concatenate([resultant_audio[len(resultant_audio) // 2:len(resultant_audio)] ,resultant_audio[0:len(resultant_audio) // 2] ])
plt.plot(np.linspace(-44100/2,44100/2, len(resultant_audio)),resultant_audio)
plt.savefig("./plotsMod/{0}.png".format("trasmissorImg11"), dpi = 72)
plt.show()


