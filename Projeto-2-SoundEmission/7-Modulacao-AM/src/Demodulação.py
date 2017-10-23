#Demodulação
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math
import soundfile as sf
import keyboard
from scipy import signal as sg


f1 = 10000
f2 = 20000
fs = 44100
x = np.linspace(0, 44100,44100)
duration = 1

def main():
    audioRecive = False
    print("Codigo Startado")
    while (audioRecive == False):
        #Recebe Audio
        if keyboard.is_pressed('q'):
            audioRecive = True;
            print("Q clickado")
            audio = getAudio()
            plot(audio, "Recieved Wave")
        else:
            pass
    
    # Demodular
    print("Estou aqui")
    signal1 = createSin(x,f1)  
    signal2 = createSin(x,f2)

    m1 = demodule(audio, signal1)
    plot(m1,"M1 Wave")
    m2 = demodule(audio, signal2)
    plot(m2,"M2 Wave")


    # Filtrar
    DemodFiltrado1  = LPF(signal1, 4000, fs)
    DemodFiltrado2  = LPF(signal2, 4000, fs)

    #Fourier Sinal Filtrado
    plot(DemodFiltrado1, "Sinal Filtrado M1")
    sd.play(DemodFiltrado1, fs)
    sd.wait()

    plot(DemodFiltrado2, "Sinal Filtrado M2")
    sd.play(DemodFiltrado2, fs)
    sd.wait()
 
    #Salva os Sons
    sf.write(Path("sound1"),DemodFiltrado1 ,fs)
    sf.write(Path("sound2"),DemodFiltrado2 ,fs)

def getAudio():
    while keyboard.is_pressed('q'):
        audio = sd.rec(int(duration*fs), fs, channels=1)
        sd.wait()
    return audio[:,0]
        
def plot(s, name):
    f, axarr = plt.subplots(2, sharex=False)
    axarr[0].clear()
    axarr[1].clear()
    axarr[0].set_title(name)
    axarr[0].plot(x[43100:],s[43100:])
    axarr[1].set_title('Fourier')
    axarr[1].plot(x, np.abs(fft(s)))
    plt.show()

def createSin(f,x):
    return np.sin(2 * math.pi * x * f)

def demodule(s, signal):
    return  s * signal
    
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