import os
os.system ('cls')
import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia # pip install wikipedia
import smtplib # internal lib for sending email
import webbrowser as wb # for chrome search

bottle = pyttsx3.init()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) #gmail port 587
    server.ehlo() # checking the coneection of smtp gmail
    server.starttls() # print function of the email
    server.login('ajaiir@gmail.com','password')# need to add less secure app on gmail to enable the feature
    server.sendmail('ajaiir@gamil.com',to,content)
    server.close()



def speak (passed_text):
    bottle.say(passed_text)
    bottle.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("the time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year) # type casting to int
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak ("The date is ")
    speak (day)
    speak (month)
    speak (year)

def greet():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning AJ")
    elif hour >=12 and hour<18:
        speak("Good afternoon AJ")
    elif hour >=18 and hour <20:
         speak("Good evening AJ") 
    else:
        speak ("Good Night AJ")
    speak ("I am online. How can I help you")

def listen():
    r =sr.Recognizer() # intializing recognizer in r variable
    with sr.Microphone() as source: #get input through microphone save in source variable
       # print("Listening") 
        r.pause_threshold = 1 # wait for 1 sec and listen the audio
        audio =r.listen(source) # listening to the microphone
    try:
       # print("recognising") # using google to recognise
        query = r.recognize_google(audio,language= 'en-in')
        print(query)
    except Exception as e: # if unable to recognize
        print(e)
        return "None"
        #
        # speak("say that again please..")
    return query
# listen()
if __name__ == "__main__":
    greet()
    speak("hey Matt how you doing")
    while True:
        packet = listen().lower()
        if 'time' in packet:
            time()
        elif 'date' in packet:
            date()
        elif 'wikipedia' in packet:
            speak("searching")
            packet =packet.replace("wikipedia","")
            result =wikipedia.summary(packet, sentences=2)
            speak(result)

        elif "can you hear me" in packet:
            speak("I am listening AJ")

        elif 'email' in packet:
            try:
                speak("What should I write AJ")
                content = listen()
                to = 'ajai.raj@fairfaxmedia.co.nz'
                sendEmail(to,content)
                speak('Email send AJ')
            except Exception as e:
                print(e)
                speak("unable to send AJ")

        elif 'search in chrome' in packet:
            speak ("what should i search") 
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' 
            search = listen().lower
            wb.get('chrome').open_new_tab(search+'.com')
            
        elif 'offline' in packet:
            speak("going offline AJ, See you soon")
            quit()



 


# greet()


