from Application.Modules.gladosvoice import FruvisCall
from Application.Modules.gladosears import listen
import requests


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
        FruvisCall(fala)


Activation = False
runtime = 0
while True:

    if runtime == 0:
        print("Activated")
        runtime = 1

    text = listen()

    if text.count("GLaDOS") > 0:
        FruvisCall('hi matt')
        Activation = True

    while Activation:
        text = listen()
        if text.count("turn yourself off") > 0:
            FruvisCall("goodbye")
            Activation = False

        elif text.count("turn lights on") > 0:
            FruvisCall("turning lights on")
            requests.get("http://192.168.15.13:5000/HomeAutomation/light?mode=HIGH")
        elif text.count("turn lights off") > 0:
            FruvisCall("turning lights off")
            requests.get("http://192.168.15.13:5000/HomeAutomation/light?mode=LOW")
        elif text.count("wake up") > 0:
            FruvisCall("hi")
            Activation = True
