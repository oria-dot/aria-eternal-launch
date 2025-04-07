# voice_command_ai.py – Speech Recognition for ARIA Command Execution

try:
        import speech_recognition
except ImportError:
    speech_recognition = None as sr

class VoiceCommandAI:
    def __init__(self, context, dispatcher):
        self.context = context
        self.dispatcher = dispatcher

    def listen_and_execute(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            print("[Voice AI] Listening for command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).strip().lower()
            print(f"[Voice AI] You said: {command}")
            from aria_core.commands.command_router     import CommandRouter
            router = CommandRouter(self.context, self.dispatcher)
            result = router.execute(command)
            print("[Voice AI] Command executed. Result:", result)
            return result
        except sr.UnknownValueError:
            print("[Voice AI] Could not understand audio.")
        except sr.RequestError as e:
            print(f"[Voice AI] Recognition error: {e}")
