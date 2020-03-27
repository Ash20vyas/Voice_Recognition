import SpeechRecognition as sr
r=sr.Recognizer()
with sr.Microphone() as src:
    print("Speak Now")
    audio = r.listen(src)
    print(r.recognize_google(audio))