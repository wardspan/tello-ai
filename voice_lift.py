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

def circle_pan(direction="right", degrees=360, step=30, delay=1.5):
    rotations = degrees // step
    for _ in range(rotations):
        if direction == "right":
            tello.rotate_clockwise(step)
        else:
            tello.rotate_counter_clockwise(step)
        time.sleep(delay)

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
    elif "go higher" in cmd or "up" in cmd:
        speak("Going up")
        tello.move_up(50)
    elif "go lower" in cmd or "down" in cmd:
        speak("Going down")
        tello.move_down(50)
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
    elif "circle pan left" in cmd or "pan left" in cmd:
        speak("Slowly panning left")
        circle_pan(direction="left")
    elif "circle pan right" in cmd or "pan right" in cmd:
        speak("Slowly panning right")
        circle_pan(direction="right")
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