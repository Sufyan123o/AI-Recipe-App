# txt 2 speech function !!! to be used in buttons for pages 1-4
# accessibility modification
from gtts import gTTS
import os
mytext = "I'm testing"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=True)

myobj.save("welcome.mp3")
os.system("start welcome.mp3") 
