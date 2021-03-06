import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math
import soundfile as sf

def main(value1,value2):
    t = 1
    fs = 44100
    
    # cria o som
    x = np.linspace(0, 44100,44100)
    S = createSin(value1,x) + createSin(value2,x)
    sf.write(Path(),S,fs)
    
    # reproduz o som
    sd.play(S,fs)

    # aguarda fim da reprodução
    sd.wait()
    plot(x,S)

def createSin(f,x):
    return np.sin(2 * math.pi * x * f) 

def plot(x,value):
    f, axarr = plt.subplots(2, sharex=False)
    axarr[0].plot(x[43100:], value[43100:])
    axarr[0].set_title('Sond Wave')
    axarr[1].plot(x, Decibel(np.abs(fft(value))))
    axarr[1].set_title('Fourier')
    plt.savefig("./plots/graphEncoderFurier.png", dpi = 72)
    plt.show()


def Decibel(value):
    new = []
    for i in range (len(value)):
        newvalue = 10* math.log10(value[i]/20000)
        new.append(newvalue)
    return new

    
def Path():
    return "./Save/tom_Encoder.wav"#audio + ".wav"

if __name__ == "__main__":
   main()



