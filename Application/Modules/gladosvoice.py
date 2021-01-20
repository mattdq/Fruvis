import requests
from simpleaudio import WaveObject


def FruvisCall(text):
    try:
        WaveObject.from_wave_file('/home/matt/PycharmProjects/Fruvis/Sounds/' + str(text) + '.wav').play().wait_done()
    except FileNotFoundError:
        url = "https://glados.c-net.org/generate?text=" + text

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            with open('/home/matt/PycharmProjects/Fruvis/Sounds/' + str(text) + '.wav') as f:
                f.write(response.content)
            WaveObject.from_wave_file(response.content)
        elif response.status_code == 503:
            WaveObject.from_wave_file("/home/matt/PycharmProjects/Fruvis/Sounds/i'll take a while to answer that.wav").play().wait_done()