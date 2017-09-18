import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import math

class Emissor(object):
    def __init__(self):
        self.t = 1
        self.fs = 44100
        self.duratiom = 53  

    def main(self,sound):
       
        S1 = self.createsin(675) + self.createsin(1209) 
        S2 = self.createsin(675) + self.createsin(1336) 
        S3 = self.createsin(675) + self.createsin(1477) 
        
        S4 = self.createsin(770) + self.createsin(1209) 
        S5 = self.createsin(770) + self.createsin(1336) 
        S6 = self.createsin(770) + self.createsin(1477) 

        S7 = self.createsin(852) + self.createsin(1209) 
        S8 = self.createsin(852) + self.createsin(1336) 
        S9 = self.createsin(852) + self.createsin(1477) 

        S0 = self.createsin(941) + self.createsin(1336)

        # reproduz o som
        sd.play(sound, self.fs)

        # aguarda fim da reprodução
        sd.wait()
        self.plot(S8)

    def createsin(self,f):
        x = np.linspace(0, self.t, self.fs * self.t)
        return np.sin(2 * math.pi * x * f) 

    def plot(self,value):
        plt.title('Sond Wave')
        plt.ylabel('Values')
        plt.plot(value, label='values')
        plt.legend(loc='upper right')
        plt.show()
