import os
import gtts
from playsound import playsound


f1 = open("C:\\Users\\nikhi\\OneDrive\\Desktop\\file.txt")
text = f1.read()

t1= gtts.gTTS(text="Hey Nikhil Good Morning", lang='en', slow=False)
#os.remove("welcome1.mp3")

t1.save("welcome1.mp3")

