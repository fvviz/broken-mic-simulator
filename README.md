# Voice-Lag-Simulator
![img.png](img.png)

Adds stimulated lag and distortion to voice that is coming from yours mic

#Installation
First of all make sure you have a virtual mic that routes audio from one app to another installed. 

- For MacOS I'd recommend <a href="https://github.com/ExistentialAudio/BlackHole"> BlackHole </a>  

- For Windows users <a href="https://vb-audio.com/Voicemeeter/index.htm"> Voicemeeter </a> 

**Clone the Repository**
```
git clone https://github.com/fvviz/Voice-Lag-Simulator.git 
cd Voice-Lag-Simulator
```

**Install requirements**
```
pip3 install -r requirements.txt
```

**Note:** Installing pyaudio can be a little hard and can break into some errors

- Windows users may face `error: Microsoft Visual C++..`. You can refer to <a href="https://stackoverflow.com/questions/59467023/getting-error-microsoft-visual-c-14-0-is-required-when-installing-pyaudio">this</a> for a solution
- MacOS users need to first install **Portaudio** via **Homebrew** to download pyaudio. If you are on an **Apple Silicon Mac** Then you can refer to <a href="https://stackoverflow.com/questions/65709212/import-pyaudio-doesnt-work-symbol-not-found-pamaccore-setupchannelmap-on-ma"> this </a> as this was the only solution that worked for me
