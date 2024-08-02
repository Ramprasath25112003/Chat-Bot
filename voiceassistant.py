import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your alexa chatbot')
engine.say('what can i do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    print('if you want to search anything in the wikipedia use a word (wikipedia)')
    print('if you want to search anything in google use the word(google)')
    print('if you want to search anything in youtube use the word (youtube)')
    print('if you want to use whatsapp use the word (whatsapp)')
    command = input("listening....\n")
    command = command.lower()
    if 'alexa' in command:
        command= command.replace('alexa','')
        #print(command)
    return command

def run_alexa():
    command= take_command()
    if 'you tube' in command:
        song = input("what do you want to search\n")
        talk('playing ' + song)
        print('playing'+song)
        pywhatkit.playonyt(song)
        pass
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is '+time)
        print(time)
    elif 'i love you' in command:
        print('sorry, I am already committed with wifi')
        talk('sorry, I am already committed with wifi')
    elif 'joke' in command:
        jokes= pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    elif 'wikipedia' in command:
        w=input("enter what to you want to search\n")
        info = wikipedia.summary(w,2)
        print(info)
        talk(info)
    elif 'whatsapp' in command:
        number=input("enter the phone number whom you want to send msg\n")
        msg= input("what do you want to send\n")
        hour= int(input("enter the hour\n"))
        minute=int(input("enter the minute\n"))
        pywhatkit.sendwhatmsg(number,msg,hour,minute)
    elif 'google' in command:
        search=input("enter what do you want to search in google\n")
        talk('searching '+search)
        pywhatkit.search(search)

    elif 'calendar' in command:
        yy = int(input("enter the year you want to see\n"))
        mm = int(input("enter the month you want to see\n"))
        print(calendar.month(yy, mm))
    else:
        print('please type what you want clearly')




while True:
    run_alexa()