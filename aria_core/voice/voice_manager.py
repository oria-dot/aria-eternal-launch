# voice_manager.py – Voice Alert System

try:
        import pyttsx3
except ImportError:
    pyttsx3 = None

class VoiceManager:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()
