import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("i am jarvis sir. please tell me how may i help you.")            
def takecommand():


    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("Can you repeat it once again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('foreverything042@gmail.com','india4all')
    server.sendmail('foreverything042@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    WishMe()
    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("according to wikipedia")
          #print(results)
          speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open over' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\harry potter series'
            film = os.listdir(music_dir)
            print(film)
            os.startfile(os.path.join(music_dir,film[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime} ")

        elif 'open code' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to ujjwal' in query:
            try:
                speak("what should i say ?")
                content = takecommand()
                to = "foreverything042@gmail.com"
                sendEmail(to,content)
                speak("email has been sent ")
            except Exception as e:
                print(e)
                speak("sorry i am not able to sent")   
                            

        

