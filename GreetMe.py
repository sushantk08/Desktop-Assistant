from desktop_assistant import *
import datetime

def greetMe():
    hour  = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")


    