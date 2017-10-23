#Demodulação
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math
import soundfile as sf
import keyboard
from scipy import signal as sg

f1 = 5000
f2 = 14000
fs = 44100
duration = 2

def main():
    audioReceive = False
    print("Codigo Startado")
    audio = getAudio()
    plot(audio, "Recieved Wave")
    
    # Demodular
    signal1 = genetate_portadora(f1,len(audio)) 
    signal2 = genetate_portadora(f2,len(audio))

    m1 = demodule(5000,audio)
    plot(m1,"M1 Wave")
    m2 = demodule(14000,audio)
    plot(m2,"M2 Wave")

    # Filtrar
    DemodFiltrado1  = LPF(m1, 3000, fs)
    DemodFiltrado2  = LPF(m2, 3000, fs)

    #Fourier Sinal Filtrado
    plot(DemodFiltrado1, "Sinal Filtrado M1")
    print('Demo 1')
    sd.play(DemodFiltrado1, fs)
    sd.wait()

    print('Demo 2')
    plot(DemodFiltrado2, "Sinal Filtrado M2")
    sd.play(DemodFiltrado2, fs)
    sd.wait()
 
    #Salva os Sons
    sf.write(Path("sound1"),DemodFiltrado1 ,fs)
    sf.write(Path("sound2"),DemodFiltrado2 ,fs)

def getAudio():
    #while keyboard.is_pressed('q'):
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    print('Acabou a gravação')
    return audio[:,0]

def genetate_portadora(frequency,tamanho):
    portadora= []
    times = np.linspace(0, 44100,tamanho)
    for i in   times:
        portadora.append(math.cos(frequency*2*math.pi*i))
    return portadora

def returnXdata(sound):
    return np.linspace(0,len(sound)/44100,len(sound))
        
def plot(s, name):
    f, axarr = plt.subplots(2, sharex=False)
    axarr[0].clear()
    axarr[1].clear()
    axarr[0].set_title(name)
    axarr[0].plot(returnXdata(s[43100:]),s[43100:])
    axarr[1].set_title('Fourier')
    axarr[1].plot(returnXdata(np.abs(fft(s))), np.abs(fft(s)))
    plt.savefig("./plotsDem/{0}.png".format(name), dpi = 72)
    plt.show()

def createSin(f,x):
    return np.sin(2 * math.pi * x * f)

def demodule(freq,signal):
    audio =signal
    print(audio[0])
    
    ts = np.linspace(0,len(audio) / 44100,len(audio))
    audio = audio*np.sin(2*math.pi*freq*ts)
    return audio
    
def LPF(signal, cutoff_hz, fs):
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))

def Path(name):
    return "./Save/{0}.wav".format(name)#audio + ".wav"

if __name__ == "__main__":
       main()