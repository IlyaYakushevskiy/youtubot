
# Import the required module
import pyttsx3
 
# Create a string
string = "Lorem Ipsum is simply dummy text " \
    + "of the printing and typesetting industry."
 
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('voice', 'com.apple.voice.enhanced.en-US.Evan')
engine.setProperty('rate', 180)
#engine.say(string)

engine.save_to_file(string, "speech.wav"  )

# Wait until above command is not finished.
engine.runAndWait()