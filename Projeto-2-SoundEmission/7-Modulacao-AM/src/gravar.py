import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math
import soundfile as sf
import keyboard
from scipy import signal as sg


def Path(name):
    return "./Save/{0}.wav".format(name)#audio + ".wav"

fs = 44100
duration = 2

print("gravando")
audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()
sf.write(Path("soundGrav"),audio ,fs)
