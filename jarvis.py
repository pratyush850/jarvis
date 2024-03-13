import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import os
import webbrowser


listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        return ""
    
def greeting():
    current_time = datetime.datetime.now()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk('Good Morning Pratyush')
    elif 12 <= hour < 18:
        talk('Good Afternoon Pratyush')
    elif 18 <= hour < 0:
        talk('Good Evening Pratyush')
    
def run_jarvis():
    command = take_command()
    if 'hello' in command or 'hi' in command:
        talk('hi Pratyush how are you')
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif 'play' in command:
        song = command.replace('play', "")
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Cuurent time is" + time)
        
    elif 'how am i looking today' in command:
        talk("Hi Esika you are looking so beautiful as always and your heart and soul both are even more beautiful")
        
    elif 'open' in command:
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk('opening' + command)
        
    elif 'close' in command:
        talk('I am closing the tab')
        pyautogui.hotkey('alt','f4')
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'remember that' in command:
        rememberMessage = command.replace('remember that', '')
        talk('you told me to remember that' + rememberMessage)
        remember = open('remember.txt', "a")
        remember.write(rememberMessage)
        remember.close()
        
    elif 'What do you remember' in command:
        remember = open('remember.txt', "r")
        talk('you told me to remember that' + remember.read())
        
    elif 'shutdown' in command or 'shut down' in command:
        talk('closing the pc')
        os.system("shutdown /s /t 1")
        
    elif 'restart' in command:
        talk('restarting the pc')
        os.system("shutdown /r /t 1")
        
    elif 'search' in command:
        usercm = command.replace('search', "")
        usercm = usercm.lower()
        webbrowser.open(f"{usercm}")
        talk("this is what i found on internet")
        
    elif 'exit' in command:
        talk('Okay bye Pratyush')
        exit()
        
    else:
        talk('I do not understand')
        
talk('Hey I am Jarvis')

greeting()

while True:
    run_jarvis()