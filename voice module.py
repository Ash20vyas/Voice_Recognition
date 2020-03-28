import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say the code");
    audio = r.listen(source)
    print("Thank You")
c="NoInput"
try:
    c=r.recognize_google(audio);
except:
    pass
if c=="Bravo":
    print(c+" was accepted")
elif c=="":
    print("No input")
else:
    print(c+" was denied")