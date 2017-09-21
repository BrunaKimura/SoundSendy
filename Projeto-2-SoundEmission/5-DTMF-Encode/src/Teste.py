from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd
import numpy as np

fs = 44100
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
duration = 1

def animate(i):
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    x = np.linspace(0, 1 , fs * 1)    
    s = audio[:,0]
    ax1.clear()
    ax1.plot(s[43100:])

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
