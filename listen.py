import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Could not understand. Please speak clearly.")
            return None
        except Exception as e:
            print(f"Microphone error: {e}")
            return None