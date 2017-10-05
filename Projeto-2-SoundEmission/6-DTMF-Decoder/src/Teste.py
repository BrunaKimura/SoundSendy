from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd
import numpy as np

fs = 44100
f, axarr = plt.subplots(2, sharex=False)
x = np.linspace(0, 1 , fs * 1)    
duration = 1

def animate(i):
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    s = audio[:,0]
    axarr[0].clear()
    axarr[1].clear()
    axarr[0].plot(x[43100:],s[43100:])
    axarr[1].plot(x,np.abs(fft(s)))

ani = animation.FuncAnimation(f, animate, interval = 100)
plt.show()
