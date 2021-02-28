from Application.Modules.tts import speak
from Application.Modules.txtrec import listen
import requests
from Application.Modules.spytify import Spot

def fruvisfalas():
    falas = ['hi',
             'hi matt',
             'hi gabi',
             "i'll take a while to answer that",
             'yes',
             'no',
             'turning lights on',
             'turning lights off']
    for fala in falas:
        speak(fala)


Activation = False
runtime = 0
while True:

    if runtime == 0:
        print("Activated")
        runtime = 1

    text = listen()

    if text.count("John") > 0:
        speak('hi matt')
        Activation = True

    while Activation:
        text = listen()
        if text.count("turn yourself off") > 0:
            speak("goodbye")
            Activation = False

        elif text.count("turn lights on") > 0:
            speak("turning lights on")
            requests.get("http://192.168.15.13:5000/HomeAutomation/light?mode=HIGH")
        elif text.count("turn lights off") > 0:
            speak("turning lights off")
            requests.get("http://192.168.15.13:5000/HomeAutomation/light?mode=LOW")
        elif text.count("wake up") > 0:
            speak("hi")
            Activation = True

        elif text.count("music") > 0:

            if text.count("living room") > 0:
                Sala = True
            else:
                Sala = False

            speak("Which one?")
            text = listen()
            if not Sala:
                Player = Spot(local='Pc', vol=80)
            else:
                Player = Spot(local='sala', vol=20)

            Music = Player.searchtrack(searchStr=text)
            speak(f"do you want me to play {Music['name']} from {Music['artist']}?")
            text = listen()
            if text.count('yes'):
                Player.playtrack(uri=Music['tracks']['items'][0]['uri'])