from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd
import soundfile as sf
import numpy as np

fs = 44100
f, axarr = plt.subplots(2, sharex=False)
x = np.linspace(0, 1 , fs * 1)    
duration = 1

def main(fileReproduce):
    print(fileReproduce)
    ani = animation.FuncAnimation(f, animate, interval = 100, fargs = fileReproduce)
    plt.show()

def animate(i,fileReproduce):
    if (fileReproduce == "1"):
        audio = sd.rec(int(duration*fs), fs, channels=1)
        sd.wait()
        s = audio[:,0]
        sf.write(Path(),s,fs)
    
    else:
        s = fileReproduce
        s.play(s,fs)
        sd.wait()
        
    axarr[0].clear()
    axarr[1].clear()
    axarr[0].set_title('Sond Wave')
    axarr[0].plot(x[43100:],s[43100:])
    axarr[1].set_title('Fourier')
    axarr[1].plot(x,np.abs(fft(s)))

def Path():
    return "./Save/tom_ask.wav"#audio + ".wav"

if __name__ == "__main__":
   main()