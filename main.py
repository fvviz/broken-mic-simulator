import pyaudio
import wave
import numpy as np

import soundcard as sc


virtual_mic = "BlackHole"
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 41000
k = 1

audio = pyaudio.PyAudio()
sp = sc.get_speaker("BlackHole")

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, frames_per_buffer=chunk)


with sp.player(samplerate=44800) as v:
    while True:
        print("Transmitting distorted Audio on")
        data = stream.read(1024)
        data = np.array(wave.struct.unpack("%dh" % (len(data) / 2), data))
        if k%15 == 0:
            pass
        else:
            v.play(data)
        k += 1