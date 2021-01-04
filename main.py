import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

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
        talk("Musisz mówić do mnie po imieniu!")


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

    elif "wyszukaj" in command or "szukaj" in command:
        command = command.replace("wyszukaj","")
        respsond = "Dobrze, szukam w google."
        pywhatkit.search(command)

    return respsond


def talk(command):
    engine = pyttsx3.init()
    # voices = engine.getProperty("voices")
    # engine.setProperty('voice',voices[0].id)
    engine.say(command)
    engine.runAndWait()

def run_alexa():
    print("Słucham...")
    print("W czym mogę ci pomóc?")
    talk("Słucham")
    talk("W czym moge ci pomóc?")

    command = take_comand()
    print(command)
    respond = skills(command)
    print(respond)
    talk(respond)


run_alexa()
