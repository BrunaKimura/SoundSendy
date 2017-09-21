import numpy as np
import sounddevice as sd
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import math
from drawnow import *
import time
import pickle

class Decoder():
    def __init__(self):
        self.duration = 1
        self.fs = 44100

        
    def main(self):
        self.x = np.linspace(0, 1, self.fs * 1)        
        plt.ion()
        while(True):
            self.audio = sd.rec(int(self.duration * self.fs), self.fs, channels=1)
            sd.wait()
            self.audio = self.audio[:,0]
            save = pickle.dump(self.audio,open("Save.p","wb"))
            drawnow(self.plot)
            drawnow(self.plotF)
            plt.pause(0.0001)
    
    def openF(self):
        openFile = pickle.load(open("Save.p","rb"))
        sd.play(openFile,self.fs)
        time.sleep(0.2)

    def plot(self):
        plt.title('Sond Wave')
        plt.grid(True)
        plt.ylabel("values")
        #plt.savefig("./plots/graphDecoder.png", dpi = 72)
        plt.plot(self.audio[43100:])
        plt.legend(loc='upper right')
        
    def plotF(self):
        plt.title('Fourier')
        plt.grid(True)
        plt.ylabel("values")
        #plt.savefig("./plots/graphDecoder.png", dpi = 72)
        plt.plot((np.abs(fft(self.audio))))
        plt.legend(loc='upper right')
        
if __name__ == "__main__":
    Decoder().main()         