import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math

def main(value1,value2):
    t = 1
    fs = 44100
    # cria o som
    x = np.linspace(0, t, fs * t)
    S = createSin(value1,x) + createSin(value2,x)
    
    # reproduz o som
    sd.play(S,fs)

    # aguarda fim da reprodução
    sd.wait()
    plot(x,S)
    plotF(x,np.abs(fft(S)))

def createSin(f,x):
    return np.sin(2 * math.pi * x * f) 

def plot(x,value):
    plt.title('Sond Wave')
    plt.ylabel('Values')
    plt.plot(x[43100:], value[43100:], label='values')
    plt.legend(loc='upper right')
    plt.show()

def plotF(x,value):
    plt.title('Fourier')
    plt.ylabel('Values')
    plt.plot(x[:], value[:], label='values')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    main()