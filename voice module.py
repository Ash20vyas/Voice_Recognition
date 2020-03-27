import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as src:
    print("Speak")
    audio = r.listen(src)
    print("thanks")

try:
    print(r.recognize_google(audio));
except:
    pass;