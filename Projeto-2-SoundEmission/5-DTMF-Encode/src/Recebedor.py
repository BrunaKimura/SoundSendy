import numpy as np
import sounddevice as sd
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from drawnow import *
import time
import sounddevice as sd

fs = 44100
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
duration = 1

x = np.linspace(0, 1 , fs*1)
def animate(i):
    print('dsad')
    audio = sd.rec(int(duration*fs), fs, channels=1)
    ax1.clear()
    ax1.plot(x[0:1000],audio[0:1000])

ani = animation.FuncAnimation(fig, animate, interval = 1000)
print('vai carai')