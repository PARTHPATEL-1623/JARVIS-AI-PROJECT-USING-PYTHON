import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyautogui
import sys
import pyjokes
import operator
from bs4 import BeautifulSoup
import requests
from pynput.keyboard import Key,Controller
import pywhatkit
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QObject, QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi
import PyPDF2





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("hello sir")
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("hello sir")
        speak("good afternoon")
    else:
        speak("hello sir")
        speak("good evening")
    speak("i am jarvis.....")
    speak("please tell me sir how can i help you")


#def pdf_reader():
   # book = open('py3.pdf','rb')
   # pdf_Reader = PyPDF2.PdffileReader(book)
   # pages = pdfReader.numPages
   # speak(f"total number of pages in this book {pages}")
   # speak("sir please enter the page number:")
   # pg = int(input("please enter the page number:"))
   # page = pdfReader.getPage(pg)
   # text = page.extractText()
   # speak(text)
    

def ads(a):
        "same as abs(a)."
        return abs(a)
def add(a,b):
        "same as a+b."
        return a+b
def and_(a,b):
        "same as a&b."
        return a&b
def floodiv(a,b):
        "same as a // b."
        return a // b
def index (a):
        "same as a,__index()"
        return a.__index()
def inv(a):
        "same as a ~a."
        return ~a 
invert = inv
def Ishift(a,b):
        "same as a << b"
        return  a << b
def mod(a,b):
     "same as a % b"
     return a % b
def mul(a,b):
     "same as a*b"
     return a*b

class MainThread(QThread):
    def  __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("listnenning.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

     try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

     except Exception as e:
        #speak("say that again please....")
        return "none"
     query=query.lower()
     return query




    def TaskExecution(self) :
        wish()
        while True:
         import pyautogui

       
         self.query = self.takecommand()

         if "open notepad" in self.query:
            npath =r"C:\Windows\notepad.exe"
            os.startfile(npath)
            speak("okay sir...opening notepad")

         if "notepad khol" in self.query:
            npath =r"C:\Windows\notepad.exe"
            os.startfile(npath)
            speak("okay sir...openning notepad")

         elif "how are you" in self.query:
             speak("i am fine sir,thanks for asking me")

         elif "how r u" in self.query:
             speak("i am fine sir,thanks for asking me")

         elif "how r you" in self.query:
             speak("i am fine sir,thanks for asking me")

         elif "how are u" in self.query:
             speak("i am fine sir,thanks for asking me")

         elif "close whatsapp" in self.query:
             speak("okay sir,closing whatsapp")
             pyautogui.press("alt","f4")


         elif "close notepad" in self.query:
             speak("okay sir,closing notepad")
             os.system("taskkill /f /im notepad.exe")

         elif "whatsapp" in self.query:
             from Whatsapp import sendMessage
             sendMessage()

         elif "ip address" in self.query:
             ip = get('https://api.ipify.org').text
             speak(f"your ip address is {ip}") 

         elif "wikipedia" in self.query:
             speak("searching wikipedia.....")
             self.query = self.query.replace("wikipedia","")
             results = wikipedia.summary(self.query,sentences=2)
             speak("according to wikipedia")
             speak(results)
             print(results)
         

         elif "open youtube" in self.query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

         elif "youtube open" in self.query:
            speak("opening youtube")
            webbrowser.open("youtube.com")


         elif "deactivate" in self.query:
          pyautogui.press("f")
          speak("deactivate full screen")
          
         elif "skip" in self.query:
          pyautogui.press("l")
          speak("video skip")
          

         elif "stop video" in self.query:
          pyautogui.press("k")
          speak("video stoped")

         elif "play video" in self.query:
          pyautogui.press("k")
          speak("video played")

         elif "ok jarvis" in self.query:
             speak("okay sir...")
             speak("sir,do you have any other work")

         elif "type" in self.query:
             self.query=self.query.replace("type","")
             pyautogui.typewrite(f"{self.query}",0.1)

         elif "activate search" in self.query:
                    from pywikihow import search_wikihow
                    speak("search mode activate,please tell me what you want to search")
                    how = self.takecommand()
                    max_results = 1
                    how_to = search_wikihow(how,max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)

         elif "where i am" in self.query:
             speak("wait sir...... i check")
             speak("sir.....")
             speak("i am not sure but now you are in the bhavnagar")
    
         elif "hu kya chu" in self.query:
             speak("wait sir...... i check")
             speak("sir.....")
             speak("i am not sure but now you are in the bhavnagar")


         elif "wait" in self.query:
             speak("okay sir i am waitinge")

         
         elif "mute" in self.query:
             pyautogui.press("m")
             speak("video muted")

         elif "unmute" in self.query:
             pyautogui.press("m")
             speak("video unmuted")

         elif "back video" in self.query:
            pyautogui.press("j")
            speak("video 10 second back")

         elif "forward video" in self.query:
            pyautogui.press("l")
            speak("video 10 second forward")

         elif "full screen" in self.query:
           pyautogui.press("f")
           speak("activate full scre")
          
         elif "music" in self.query:
             speak("tell me the name of song")
             musicname=self.takecommand()
             pywhatkit.playonyt(musicname)
             speak("your song has been started")
             speak("enjoy sir")

         elif "youtube" in self.query:
             speak("closing youtube")
             pyautogui.hotkey("alt","f4")

          
         elif "open google" in self.query:
             speak("opening google")
             speak("sir,what should i search on google")
             cm = self.takecommand()
             webbrowser.open(f"{cm}")

         elif "google" in self.query:
             speak("closing google.")
             pyautogui.hotkey("alt","f4")

         elif "open instagram" in self.query:
             speak("opening instagram")
             webbrowser.open("instagram.com")


         elif "instagram" in self.query:
             speak("closing instagram")
             pyautogui.hotkey("alt","f4")


         elif "shut down the system" in self.query:
             os.system("shutdown /s /t 5")
        
         elif "restart the system" in self.query:
             os.system("shutdown /r /t 5")


         elif "open flipkart" in self.query:
             webbrowser.open("www.flipkart.com")
             speak("opening flipkart")

         elif "flipkart" in self.query:
             speak("closing flipkart")
             pyautogui.hotkey("alt","f4")

         elif "open amazon" in self.query:
             webbrowser.open("www.amazon.com")
             speak("opening amazon")

         elif "amazon" in self.query:
             speak("closing amazon")
             pyautogui.hotkey("alt","f4")

         elif "do some calculation" in self.query:
             r=sr.Recognizer()
             with sr.Microphone() as source:
                 speak("say what you want to calculate, example: 3 plus 3")
                 print("listening.......")
                 r.adjust_for_ambient_noise(source)
                 audio=r.listen(source)
             my_string=r.recognize_google(audio)
             print(my_string)
             def get_operator_fn(op):
                 return {
                     '+' : operator.add,
                     '-' : operator.sub, 
                     '*' : operator.mul,
                     'divided' : operator.__truediv__,
                 }[op]
             def eval_binary_expr(op1,oper,op2):
                 op1,op2= int(op1), int(op2)
                 return get_operator_fn(oper)(op1,op2)
             speak("you result is")
             speak(eval_binary_expr(*(my_string.split())))
                    
         elif "calculation" in self.query:
             r=sr.Recognizer()
             with sr.Microphone() as source:
                 speak("say what you want to calculate, example: 3 plus 3")
                 print("listening.......")
                 r.adjust_for_ambient_noise(source)
                 audio=r.listen(source)
             my_string=r.recognize_google(audio)
             print(my_string)
             def get_operator_fn(op):
                 return {
                     '+' : operator.add,
                     '-' : operator.sub, 
                     '*' : operator.mul,
                     'divided' : operator.__truediv__,
                 }[op]
             def eval_binary_expr(op1,oper,op2):
                 op1,op2= int(op1), int(op2)
                 return get_operator_fn(oper)(op1,op2)
             speak("you result is")
             speak(eval_binary_expr(*(my_string.split())))
        
         elif "whatsapp" in self.query:
            from Whatsapp import sendMessage
            sendMessage()

        
         elif "mobile camera" in self.query:
              import urllib.request
              import cv2 
              import numpy as np
              import time
              URL="http://192.168.31.196:8080/shot.jpg"
              while True:
                   img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                   img=cv2.imdecode(img_arr,-1)
                   cv2.imshow('IPWebcam',img)
                   q=cv2.waitKey(1)
                   if q==ord("q"):
                        break;
        
        
              cv2.destroyAllWindows()             
                 
                
         
         elif "open mobile camera" in self.query:
              import urllib.request
              import cv2 
              import numpy as np
              import time
              URL="http://192.168.73.88:8080/shot.jpg"
              while True:
                   img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                   img=cv2.imdecode(img_arr,-1)
                   cv2.imshow('IPWebcam',img)
                   q=cv2.waitKey(1)
                   if q==ord("q"):
                        break;
        
        
              cv2.destroyAllWindows()
          
         elif "tell me a joke" in self.query:
             joke = pyjokes.get_joke()
             speak("joke")

         elif "temperature" in self.query:
             
             search="temperature in bhavnagar"
             url=f"https://www.google.com/search?q={search}"
             r =requests.get(url)
             data= BeautifulSoup(r.text,"html.parser")
             temp=data.find("div",class_="BNeawe").text
             speak(f"current{search} is {temp} ")

         elif "game" in self.query:
                
                    from game import game_play
                    game_play()

         elif "screenshot" in self.query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     speak("sir,screenshot take succesfully")


         elif "photo" in self.query:
                    pyautogui.hotkey("super")
                    pyautogui.typewrite("camera")
                    pyautogui.hotkey("enter")
                    pyautogui.sleep(2)
                    speak("SMILE  please....")
                    pyautogui.hotkey("enter")


         elif "camera" in self.query:
             pyautogui.hotkey("alt","f4")

         elif "volume up" in self.query:
             pyautogui.press("volumeup")
             speak("okay sir,volume up....")

         elif "volume down" in self.query:
             pyautogui.press("volumedown")
             speak("okay sir,volume down....")

         

         elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:

            import psutil
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"sir our system have {percentage} percent battery")

            if percentage>=75:
                 speak("sir......,we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                 speak("sir......,we should connect our system to charing point to charge our battery")

    


         elif "internet speed" in self.query:
                    import speedtest
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

         elif "no thanks" in self.query:
             speak("okay sir,thanks for using me,have a good day")
             break

        
            
                
startExecution = MainThread()
         
         
class Main(QMainWindow):
   def __init__(self):
      super().__init__()
      self.ui = Ui_jarvisUi()
      self.ui.setupUi(self)
      self.ui.pushButton.clicked.connect(self.startTask)
      self.ui.pushButton_2.clicked.connect(self.close)

   def startTask(self):
      self.ui.movie = QtGui.QMovie("D:/JARVIS AI PROJECT/7LP8.gif")
      self.ui.label.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie = QtGui.QMovie("D:/JARVIS AI PROJECT/Jarvis_Loading_Screen.gif")
      self.ui.label_2.setMovie(self.ui.movie)
      self.ui.movie.start()
      timer = QTimer(self)
      timer.timeout.connect(self.showTime)
      timer.start(1000)
      startExecution.start()

   def showTime(self):
      current_time = QTime.currentTime()
      current_date = QDate.currentDate()
      label_time = current_time.toString('hh:mm:ss')
      label_date = current_date.toString(Qt.ISODate)
      self.ui.textBrowser.setText(label_date)
      self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())            

