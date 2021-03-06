import pyaudio
import wave
import numpy as np
import json
from random import randint

import soundcard as sc


json_file = open("constants.json", "r")
constants = json.load(json_file)
json_file.close()

format_ = pyaudio.paInt16
k = 1

audio = pyaudio.PyAudio()
sp = sc.get_speaker(constants["virtual_mic"])

stream = audio.open(format=format_, channels=constants["channels"],
                    rate=constants["read_rate"], input=True, frames_per_buffer=constants["chunk"])


with sp.player(samplerate=constants["write_rate"]) as v:
    while True:
        print(f">>> Transmitting distorted Audio on {sp.name} ")
        data = stream.read(constants["chunk"])
        transf_data = np.array(wave.struct.unpack("%dh" % (len(data) / 2), data)) + randint(1,5)
        if k % randint(1,15) == 0:
            for i in range(0, constants["delay_frames"]):
                pass
            pass
        else:
            v.play(transf_data)
        k += 1

