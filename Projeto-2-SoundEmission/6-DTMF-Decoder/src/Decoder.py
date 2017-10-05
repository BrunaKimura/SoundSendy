from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import read

fs = 44100
f, axarr = plt.subplots(2, sharex=False)
x = np.linspace(0, 1 , fs * 1)   
duration = 1

def main(fileReproduce):
    if (fileReproduce == "1"):
        ani = animation.FuncAnimation(f, animate, interval = 100)
    
    else:
        s, samplerate = sf.read(fileReproduce)
        sd.play(s,fs)
        sd.wait()
        plot(s)
    
    plt.show()

def animate(i):
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    s = audio[:,0]
    #sf.write(Path(),s,fs)
    plot(s)

def plot(s):
    axarr[0].clear()
    axarr[1].clear()
    axarr[0].set_title('Sond Wave')
    axarr[0].plot(x[43100:],s[43100:])
    axarr[1].set_title('Fourier')
    axarr[1].plot(x, np.abs(fft(s)))
    

def Path():
    return "./Save/tom_ask.wav"#audio + ".wav"

if __name__ == "__main__":
   main()