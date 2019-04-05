import pyttsx3
engine=pyttsx3.init()
x=int(input("enter 0 for male voice or 1 for female voice:"))
y=str(input("enter the text which you need to convert into text:"))
voices=engine.getProperty('voices')
if x==0:
    engine.setProperty('voice',voices[x].id)
    engine.say(y)
elif x==1:
    engine.setProperty('voice',voices[x].id)
    engine.say(y)
else:
    print("plzz choose the correct voice either 1 or 0")
engine.runAndWait()
