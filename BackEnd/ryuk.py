import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser as wb
import pywhatkit as kit
import smtplib
import pyjokes
import pyautogui
import requests
import time
import sys
# from sys import exit
# import exit
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ryukUI import Ui_Ryuk


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    output = "As-salamu-alaikum!"
    speak("As-salamu-alaikum!")
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        print("Good morning Boss!")
        speak("Good morning Boss!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Boss!")
    elif hour >= 18 and hour < 24:
        speak("Good evening Boss!")
    else:
        print("Good night Boss!")
        speak("Good night Boss!")
    speak("I'm REEUK. How can I help you?")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"Now time is {Time}")
    print(f"Now time is {Time}")


def date():

    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Toda's date is ")
    speak(date)
    speak(month)
    speak(year)
    print(f"Today's date is {date}/{month}/{year}")


def sent_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("omarfaruq3110@gmail.com", 'pulchritude')
    server.sendmail("omarfaruq3110@gmail.com", to, content)
    server.close()


def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=785bd91315e44d8c97855db00eb175d7'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth',
           'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: {head[i]}")
        speak(f"today's {day[i]} news is: {head[i]}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f'You said: {query}')

        except Exception as e:
            speak('Would you please repeat!')
            print('Would you please repeat!')
            return 'none'

        return query

    def TaskExecution(self):
        # if __name__ == '__main__':
        greet()
        while True:

            self.query = self.take_command().lower()

            if 'close code' in self.query:
                speak('closing code')
                os.system('taskkill /f /im Code.exe')

            elif 'thank' in self.query:
                print("You're most welcome boss!")
                speak("You're most welcome boss!")

            elif 'who is your father' or 'who is your mother' in self.query:
                print("I wasn't born rather I have been created!")
                speak("I wasn't born rather I have been created!")

            elif 'what is your name' in self.query:
                speak("My name is Reeuk!")
                print("My name is Reeuk!")

            elif 'time' in self.query:
                time()

            elif 'date' in self.query:
                date()

            elif 'code' in self.query:
                notepad_path = 'C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(notepad_path)

            elif 'command prompt' in self.query:
                os.system("start cmd")

            elif 'music' in self.query:
                songs_dir = 'F:/Music/bangla/band/Artcell/Onno samay'
                songs = os.listdir(songs_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(songs_dir, rd))
                # for song in songs:
                #     if song.endswith('.mp3'):
                #         os.startfile(os.path.join(songs_dir, song))

            elif 'ip address' in self.query:
                ip = get('http://api.ipify.org').text
                print(f"Your IP address is {ip}")
                speak(f"Your IP address is {ip}")

            elif 'wikipedia' in self.query:
                speak("Searching...")
                query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(f'{query}', sentences=2)
                print(results)
                speak('According to wikipedia ')
                speak(results)

            # elif "WhatsApp" in query:
            #     kit.sendwhatmsg('+8801671991353', 'testing', 2, 25)

            elif 'youtube' in self.query:
                print("What should I search in youtube?")
                speak("What should I search in youtube?")
                song_youtube = self.take_command().lower()
                kit.playonyt(song_youtube)

            elif 'google' in self.query:
                print("What should I search in google?")
                speak("What should I search in google?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = self.take_command().lower()
                if ' ' in search:
                    search = search.replace(' ', '')
                wb.get(chromepath).open_new_tab(search+".com")

            elif 'send email' in self.query:
                try:
                    to = input("Please input email: ")
                    print('What should your email content?')
                    speak('What should your email content?')
                    content = self.take_command()
                    if 'write' in content:
                        content = input("Please write here: ")

                    sent_email(to, content)
                    speak('Email sent')
                except Exception as e:
                    print(e)
                    speak("Couldn't send. Something went wrong")

            # elif 'set alarm' in query:

            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            # elif 'new folder' in query:
            #     # speak('What should I write')
            #     # command = take_command().lower()
            #     os.system(f'mkdir newfolder')

            elif 'window' in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(5)
                pyautogui.keyUp('alt')

            elif 'news' in self.query:
                speak('Fetching the latest news, please wait')
                news()

            elif 'location' in self.query:
                speak('Let me check sir, please wait')
                try:
                    ipAdd = requests.get('http://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    print(city+', '+country)

                    speak(
                        f"Sir I'm not sure, but I think we are in {city} city of {country}")
                except Exception as e:
                    print('Sorry sir, I am not able to find')
                    speak('Sorry sir, I am not able to find')

            elif 'get out' in self.query:
                print("Allah hafez Boss! Have a nice day.")
                speak("Allah hafez Boss! Have a nice day.")
                quit()

            else:
                speak("Sorry I don't know the answer to this one. But I'm learning.")


startExecution = MainThread()


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Ryuk()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("I:/ryuk/wave.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("I:/ryuk/initializing.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("I:/ryuk/loading.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        Current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = Current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


App = QApplication(sys.argv)
ryuk = Main()
ryuk.show()
exit(App.exec_())
