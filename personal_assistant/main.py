import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import webbrowser
import time
import subprocess
from GoogleNews import GoogleNews


r = sr.Recognizer()
engine = pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', file_name])
    talk("I have made a note of that!")


def get_audio():
    talk('Start to speak now...')
    with sr.Microphone() as s:
        audio = r.listen(s)
        talk('Finish speak')
        speak = ''
        try:
            speak = r.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Sorry, my speech service is down')

        return speak


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:

            voice_data = r.recognize_google(audio)

            voice_data = voice_data.lower()


        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Sorry, my speech service is down')

        return voice_data


def respond(voice_data):

    if 'wiki' in voice_data:
        search = voice_data.replace('wiki', '')
        print(search)
        info = wikipedia.summary(str(search), 1)
        print(info)
        talk(info)

    elif 'news' in voice_data:
        googlenews = GoogleNews()
        googlenews = GoogleNews('en', 'd', encode='utf-8')
        talk('Select country')
        country = str(input('Select country: '))

        googlenews.search(country)
        googlenews.get_page(1)
        news = googlenews.result()
        for n in news:
            print()
            print(n['title'])
            talk(n['title'])
            print(n['desc'])
            talk(n['desc'])
            print(n['link'])
            print(n['date'])
            print()

    elif 'open' in voice_data:
        if 'notepad' in voice_data:
            print('Open notepad')
            talk('Open notepad')
            talk('What would you like me to write?')
            note_text = get_audio()
            note(note_text)

        elif 'calculator' in voice_data:
            print('Open calculator')
            talk('Open calculator')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'control' in voice_data:
            print('Open control panel')
            talk('Open control panel')
            subprocess.Popen('C:\\Windows\\System32\\control.exe')

    elif 'play' in voice_data:
        song = voice_data.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'google' in voice_data:
        search = voice_data.replace('google', '')
        url = f'https://google.com/search?q={search}'
        print(f'Here is what i found for {search}')
        talk(f'Here is what i found for {search}')
        webbrowser.get().open(url)

    elif 'location' in voice_data:
        location = voice_data.replace('location', '')
        url = f'https://google.nl/maps/place/{location}/&amp;'
        print(f'Here is the location of {location}')
        talk(f'Here is the location of {location}')
        webbrowser.get().open(url)

    elif 'time' in voice_data:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'joke' in voice_data:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'weather' in voice_data:
        talk('Select the city.')
        city = str(input('Give city: '))
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=7933ecbc4c180e23d0e129deca5d56d2&units=metric'
        json_data = requests.get(url).json()
        weather_now = f"The weather in {json_data['name']} now is {json_data['weather'][0]['description']}. The temperature is {json_data['main']['temp']} degrees Celcius. The humidity is {json_data['main']['humidity']} percent. "
        print(weather_now)
        talk(weather_now)



    elif 'exit' in voice_data:
        talk('Bye bye')
        exit()


time.sleep(1)
print('I am listening you...')
talk('How can I help you? I am listening you...')

print("say 'wiki' + word for wikipedia search")
talk("say 'wiki' + word for wikipedia search")

print("say 'google' + word for google search")
talk("say 'google' + word for google search")

print("say 'time' ")
talk("say 'time' ")

print("say 'joke' ")
talk("say 'joke' ")

print("say 'weather' for weather prediction")
talk("say 'weather' for weather prediction")

print("say 'exit' for exit")
talk("say 'exit' for exit")
while 1:
    voice_data = record_audio()
    respond(voice_data)
