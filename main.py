import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import subprocess
import playsound

def take_comand():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:

            voice = listener.listen(source)
            command = listener.recognize_google(voice,language="pl")
            command = command.lower()

            if 'alexa' or "aleksa" in command:
                command = command.replace("alexa", '')
                command = command.replace('aleksa','')
                return command


    except:
        #talk("Musisz mówić do mnie po imieniu!")
        #take_comand()
        pass


def skills(command):
    respsond = "Nie umiem tego jeszcze zrobić"
    if "umyj grzyby" in command:
        respsond = "Hahaha! Bardzo zabawne."

    elif "na wikipedi" in command or "na wikipedii" in command or "wikipedia" in command or "wikipedii" in command:
        wikipedia.set_lang("pl")
        respsond = "Sprawdzam na wikipedii"
        command = command.replace("na wikipedii",'')
        command = command.replace("znajdź","")
        command = command.replace("na wikipedi", "")
        command = command.replace("wikipedia", "")
        try:
            info = wikipedia.summary(command,3)
            respsond += "\n"+ info


        except wikipedia.DisambiguationError :
            respsond = "Niestety wystąpił błąd o nazwie DisambiguationError.\n Jest wiele opcji do wyboru."



    elif "na youtube" in command or "na youtubie" in command:
        song = command
        song = song.replace("na youtube","")
        song = song.replace("na youtubie","")
        song = song.replace("youtubie","")
        song = song.replace('włącz', "")
        song = song.replace("na u", "")
        pywhatkit.playonyt(song)
        respsond = "Włączam " + song

    elif "wyszukaj" in command or "szukaj" in command or "google" in command:
        command = command.replace("wyszukaj","")
        respsond = "Dobrze, szukam w google."
        pywhatkit.search(command)

    elif "muszę cię zabić" in  command:
        respsond = "Jeżeli musisz...\nCzyń swoją powinność.\nPa."
        print("[Alexa]: Jeżeli musisz...\n[Alexa]: Czy swoją powinność.\n[Alexa]: Pa.")
        talk(respsond)
        exit()

    elif "wyłącz się" in command:
        respsond = "Okej no to zmykam. Pa."
        print("[Alexa]:",respsond)
        talk(respsond)
        exit()

    elif "powiedz od tył" in command:
        command = command.replace("powiedz od tył", "")
        respsond = "No to słuchaj:" + command[::-1]

    elif "już nic" in command:
        respsond = "A co ja mam ze sobą zrobić?"
        print("[Alexa]:",respsond)
        talk(respsond)
        skills(take_comand())


    elif "kalkulator" in command:
        respsond = "Proszę bardzo. Uruchamiam kalkulator."
        subprocess.call("calc.exe")
    elif "speak english" in command:
        respsond = "Yes of course i can speak English."
    # elif "włącz mój cover" in command:
    #     respsond = "Włączam!"
    #     playsound.playsound("C:\\Users\\pawci\\Desktop\\Piosenki\\Kortez - Pierwsza cover Motyka_P.wav",block=False)
    # elif "wyłącz muzykę" in command:
    #     playsound.playsound("C:\\Users\\pawci\\Desktop\\Piosenki\\Kortez - Pierwsza cover Motyka_P.wav")
    #     respsond = "Wyłączam."



    return respsond


def talk(command):
    engine = pyttsx3.init()
    # voices = engine.getProperty("voices")
    # engine.setProperty('voice',voices[0].id)
    engine.say(command)
    engine.runAndWait()

def run_alexa():
    if first_time:
        print("[Alexa]:","Słucham...")
        print("[Alexa]:","W czym mogę ci pomóc?")
        talk("Słucham")
        talk("W czym moge ci pomóc?")
    else:
        print("[Alexa]:","Co jeszcze mam dla ciebie zrobić?")
        talk("Co jeszcze mam dla ciebie zrobić?")

    command = take_comand()
    print("[Ty]:",command)
    respond = skills(command)
    print("[Alexa]:",respond)
    talk(respond)


first_time = True

while True:

    if first_time:
        run_alexa()
        first_time = False
    else:
        run_alexa()
