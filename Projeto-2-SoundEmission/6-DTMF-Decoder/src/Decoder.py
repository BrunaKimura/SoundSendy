from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import read

fs = 44100
f, axarr = plt.subplots(2, sharex=False)
x = np.linspace(0, 44100,44100)   
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
    printTom(s)

def printTom(s):
    allpoints = np.abs(fft(s))
    peaks_indexes = peakutils.indexes(allpoints[:(len(allpoints)//2)], min_dist=50)
    peaks = []
    for i in peaks_indexes:
        peaks.append(x[i])
    peaks.sort()
    if(len(peaks) >= 2):
        first_hz = peaks[-1]
        second_hz = peaks[-2]
        matrix = [
            [1336,941],[1209,697], [1336,697],
            [1477,697], [1209,770], [1336,770],
            [1477,770], [1209,852], [1336,852],
            [1477,852]
        ]
        counter = 0
        for i in matrix:
            if np.abs(first_hz-i[0]) < 3 and np.abs(second_hz-i[1]) < 3:
                print(counter)
            counter += 1

def Path():
    return "./Save/tom_ask.wav"#audio + ".wav"

if __name__ == "__main__":
   main()