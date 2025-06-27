import pyjokes
import pyttsx3

joke = pyjokes.get_pipxjoke()
print("Printing Jokes ...")

engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()
