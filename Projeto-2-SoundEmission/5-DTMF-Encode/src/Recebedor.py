import numpy as np
import sounddevice as sd
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import math
import drawnow
import time

class Recebedor():
    def __init__(self):
        self.duration = 2  
        self.fs = 44100

    def main(self):
        myrecording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)
        plt.ion()
        while(sd.wait()):
            self.recording_fft = fft(myrecording)
            drawnow(self.plot)
           
    def plot(self):
        plt.plot(self.recording_fft)
        plt.pause(0.02)

if __name__ == "__main__":
    Recebedor().main()          