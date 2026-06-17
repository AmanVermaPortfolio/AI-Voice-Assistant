import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    female_voice = None
    for v in voices:
        if 'female' in v.name.lower() or 'zira' in v.name.lower() or 'hazel' in v.name.lower():
            female_voice = v.id
            break
    if female_voice:
        engine.setProperty('voice', female_voice)
    elif len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()