import speech_recognition as sr
import pyttsx3
from djitellopy import Tello
import time

# Initialize recognizer and TTS
r = sr.Recognizer()
engine = pyttsx3.init()

# Initialize Tello
tello = Tello()
tello.connect()

def speak(text):
    print("Drone:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
    return ""

# Voice command loop
speak("Drone is ready for voice commands.")
while True:
    cmd = listen()

    if not cmd:
        continue
    elif "take off" in cmd:
        speak("Taking off")
        tello.takeoff()
    elif "land" in cmd:
        speak("Landing")
        tello.land()
    elif "battery" in cmd:
        battery = tello.get_battery()
        speak(f"Battery level is {battery} percent.")
    elif "flip" in cmd:
        if "left" in cmd:
            speak("Flipping left")
            tello.flip('l')
        elif "right" in cmd:
            speak("Flipping right")
            tello.flip('r')
        elif "forward" in cmd:
            speak("Flipping forward")
            tello.flip('f')
        elif "back" in cmd:
            speak("Flipping back")
            tello.flip('b')
    elif "go forward" in cmd or "fly forward" in cmd:
        speak("Flying forward")
        tello.move_forward(50)
    elif "go back" in cmd or "fly back" in cmd or "go backwards" in cmd:
        speak("Flying backward")
        tello.move_back(50)
    elif "turn right" in cmd or "rotate right" in cmd:
        speak("Turning right 30 degrees")
        tello.rotate_clockwise(30)
    elif "turn left" in cmd or "rotate left" in cmd:
        speak("Turning left 30 degrees")
        tello.rotate_counter_clockwise(30)
    elif "stop" in cmd or "exit" in cmd or "shutdown" in cmd:
        speak("Shutting down voice control.")
        break