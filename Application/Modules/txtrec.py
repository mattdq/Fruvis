import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=3)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
            # said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)
    return said



