import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() # Variable or user who can recognize voice
engine = pyttsx3.init()
voices = engine.getProperty('voices') # Getting all the voices from the pythonttx3 library
engine.setProperty('voice', voices[1].id)

# Talking with Alexa
def talk(text):
    engine.say(text)
    engine.runAndWait()

 # To interact with Alexa
def take_command():
    try:
        with sr.Microphone() as source: # Detecting the voice from our microphone
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice) #Speech_recognition
            command = command.lower()   # converting in lowercase
            if 'alexa' in command: #If and only if Alexa mentioned in the speech
                command = command.replace('alexa', '')
                print(command)
    except:   # Don't do anything
        pass
    return command


def run_alexa():
    command = take_command() # taking command or input from the user
    print(command) 
    if 'play' in command:
         # To remove the 'play' from the  command
        # replace the play with the empty string
        song = command.replace('play', '') #replacing the particular word from the string by '' so it will not be repeat again
        talk('playing ' + song)
        pywhatkit.playonyt(song)  # play on you tube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') # in 24hrs format ('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'day' in command:
        day = datetime.datetime.now().strftime('%A')
        print(day)
        talk("Today is " + day)
    elif 'year' in command:
        year = datetime.datetime.now().strftime('%Y')
        print(year)
        talk("Current ongoing year is " + year)
    elif 'month' in command:
        month = datetime.datetime.now().strftime('%B')
        print(month)
        talk("Current ongoing month is " + month)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 4)  # Searching on the wikipedia 
        print(info)
        talk(info)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person,4)
        print(info)
        talk(info)
    elif 'find' in command:
        person = command.replace("find" , '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'how are you' in command:
        talk('I have a headache')
    elif 'where are you from' in command:
        talk('I am from technology world')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()