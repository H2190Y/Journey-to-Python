import pyjokes
import pyttsx3



joke = pyjokes.get_joke()
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()

# print('Printing Jokes ..... ... .. .')
# print("     ",joke)
