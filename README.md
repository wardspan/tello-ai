# 🛸 Tello AI Voice-Controlled Drone Project

This project uses voice commands (via Whisper or Google Speech) to control a Ryze Tello drone using Python.

## 📦 Features

- ✅ Voice-controlled takeoff, landing, flips
- ✅ GPT-4o-powered photo description
- ✅ Whisper-based offline speech recognition
- ✅ Real-time altitude changes with voice
- ✅ Pan left/right, turn left/right, fly forward/back
- ✅ Battery status via voice
- ❌ No internet required once Whisper model is downloaded

## 🧰 Requirements

- Python 3.11+
- MacOS (tested), Linux should work similarly
- [Ryze Tello drone](https://www.ryzerobotics.com/tello)
- Internet connection for model download (first time only)

## 🔧 Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install FFmpeg for Whisper
brew install ffmpeg  # Mac
```

## 🧠 Voice Command Scripts

### `voice_control_whisper.py`
Offline voice commands using Whisper (requires Whisper model downloaded)

### `voice_lift.py`
Includes:
- takeoff/land
- go up/down
- fly forward/back
- turn left/right (30°)
- slow pan left/right (circle)

## 🗣 Example Commands

- “Take off”
- “Land”
- “Go higher”
- “Go lower”
- “Fly forward”
- “Fly backward”
- “Turn left”
- “Turn right”
- “Circle pan left”
- “Circle pan right”
- “Battery”
- “Exit”

## 📸 Vision Features

### `photo_analyzer.py`
Captures a photo from the drone and sends it to GPT-4o for visual interpretation.

## 🧪 Testing UDP

### `test_tello.py`
Connect to drone and do basic takeoff/land.

### `test_udp_send.py`
Raw socket test to verify UDP access.

---

## 🔐 Notes

- Whisper model will be downloaded to `~/.cache/whisper`
- Use a second Wi-Fi adapter to stay connected to the drone and the internet simultaneously

---

## 🙌 Contributions Welcome

Built by [Ward](https://www.linkedin.com/in/wardspan/) and friends.