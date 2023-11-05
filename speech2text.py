# speech 2 text alg.. to be integrated on page 3 to confirm recipe selection
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech


def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for user to speak


while (1):

    # Exception handling to handle exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            # audio2 = r.listen(source2)
            audio2 = r.listen(source2, 4, 7)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ", MyText, "?")
            MyQuestion = "Did you say " + MyText + "?"
            SpeakText(MyQuestion)
            audio3 = r.listen(source2)
            Response = r.recognize_google(audio3)
            Response = Response.lower()
            if ("yes" in Response):
                myresponse = "Ingredient Confirmed"
                print(myresponse)
                SpeakText(myresponse)
                

            else:
                myresponse = "Confirmation not recieved"
                print(myresponse)
                SpeakText(myresponse)
                

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
