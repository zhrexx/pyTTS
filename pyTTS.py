import pyttsx3

class SpeechGenerator:
    def __init__(self):
        self.generation = True
        self.engine = pyttsx3.init()

    def text_to_speech(self, text):
        if self.generation:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"Error generating speech: {e}")
        else:
            print("Error 909")

inp = input("Print the Text : ")
generator = SpeechGenerator()
generator.text_to_speech(inp)

  



  
