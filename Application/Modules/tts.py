import requests
from simpleaudio import WaveObject
import boto3
import json

def speak(text):
    with open('/home/matt/PycharmProjects/Fruvis/credentials.json') as json_file:
        cred = json.load(json_file)
        access_key_id = cred['AWSAccessKey']
        secret_access_key = cred['AWSSecretKey']

    polly_client = boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name='us-west-2').client('polly')

    response = polly_client.synthesize_speech(VoiceId='Camila',
                                          OutputFormat='mp3',
                                          Text=text)


    audio_stream = response['AudioStream'].read()
    response['AudioStream'].close()

    f = open(f'/home/matt/PycharmProjects/Fruvis/Sounds/{text}.mp3', 'wb')
    f.write(audio_stream)
    f.close()
    import os
    os.system('mpg321 /home/matt/PycharmProjects/Fruvis/Sounds/' + str(text).replace(" ", "\\ ") + '.mp3 -q')


def GLaDOSCall(text):
    try:
        WaveObject.from_wave_file('/home/matt/PycharmProjects/Fruvis/Sounds/' + str(text) + '.wav').play().wait_done()
        print(text)
    except FileNotFoundError:
        url = "https://glados.c-net.org/generate?text=" + text

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            with open('/home/matt/PycharmProjects/Fruvis/Sounds/' + str(text) + '.wav') as f:
                f.write(response.content)
            WaveObject.from_wave_file(response.content)
            print(text)
        elif response.status_code == 503:
            WaveObject.from_wave_file(
                "/home/matt/PycharmProjects/Fruvis/Sounds/i'll take a while to answer that.wav").play().wait_done()
            print(text)
            speak("I'll answer for you!")
            speak(text)