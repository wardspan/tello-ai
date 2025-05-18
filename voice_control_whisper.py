import whisper
import pyttsx3
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from djitellopy import Tello
import time

# Initialize
engine = pyttsx3.init()
model = whisper.load_model("base")
tello = Tello()
tello.connect()

def speak(text):
    print("Drone:", text)
    engine.say(text)
    engine.runAndWait()

def record_audio(duration=5, samplerate=16000, filename="command.wav"):
    speak("Listening...")
    print("Recording...")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, samplerate, audio)
    return filename

def transcribe_audio(filename):
    print("Transcribing...")
    result = model.transcribe(filename)
    print("You said:", result["text"])
    return result["text"].lower()

# Voice command loop
speak("Drone is ready for voice commands.")
while True:
    file = record_audio()
    cmd = transcribe_audio(file)

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
    elif "stop" in cmd or "exit" in cmd or "shutdown" in cmd:
        speak("Shutting down voice control.")
        break