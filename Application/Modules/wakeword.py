import pyaudio
import pvporcupine
import struct
from Application.Modules.tts import speak
from Application.Modules.txtrec import listen
import requests
import time

porcupine = None
pa = None
audio_stream = None

try:
    porcupine = pvporcupine.create(keywords=['alexa'])

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            requests.get("http://192.168.15.13:5000/HomeAutomation/led?pin=17&mode=HIGH")
            speak('Olá!')
            time.sleep(0.2)
            requests.get("http://192.168.15.13:5000/HomeAutomation/led?pin=17&mode=LOW")

            text = listen()
            if text.count("tchau") > 0:
                speak("adeus")
            elif text.count("xpresso") > 0:
                speak('devo fazer um expresso para você?')
                text = listen()
                if text.count("sim") > 0:
                    speak("Claro, ele ficará pronto em trinta segundos.")


finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if pa is not None:
        pa.terminate()
