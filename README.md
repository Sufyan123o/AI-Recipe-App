<p align="center">
  <a href="https://discord.gg/b6zyJyCQUu">
    <img src="https://cdn.discordapp.com/attachments/597104422123995136/1172330024406355989/medium.png?ex=655fec6a&is=654d776a&hm=d961a6c6ca29e1ade50b713e3f295bb351c139183e043b04a98709bbd04ba09b&" alt="Logo" width="auto" height="180">
  </a>
  
# Cook-Aid


Welcome to "Cook-Aid"
This is our Durhack 2023 submission, an aid application for visually-impared users (VIUs) to ease their cooking process. Our application scans in the ingredients you have at your disposal, optimized to the use of a phone camera and/or the ADLINK Neon-202B-JT2-X (sensor dimensions: 1600 1200) industrial machine vision and AI smart camera, and then generates 3 recipes that you can make with what's available to you.

In the interest of extended accessibility, our application is to have embedded text-to-speech functionality to allow VIUs to smoothly navigate the program. As an extenstion, the application would also allow for speech-to-text communication with the program to process ingredients, confirm their identifications and select the final recipe choice.

--------
The backend functionalities depend on the following technologies:
- Open Computer Vision (CV2) (to recognize items in the snapshots/images)
- Google Translate's GTTS (to read out the text)
- Google Vision (to identify the ingredients scanned in)
- Recipe API (access: https://api-ninjas.com/api/recipe)
- TaiPy 
- Object Detection API (access: https://api-ninjas.com/api/objectdetection)
- Pyttsx3 Speech --> Text Library (+ Pyaudio) for the accesibiility functionality that allows users to interact with the application with only their voice
- Open API (to match the identified ingredients to recipes in available API)

The main issues encountered with the project is the barrier of open-access knowledge around the smart camera, the ADLINK Neon-202B-JT2-X. Being such an expensive technology, there is limited open-access documentation as to the integration of such technology with a more user-based web-app.

Alltogether, we've learned more within this venture in the last 24 hours about API integration, frontend development using python, Open CV and Neon ADLINK technology than we were ever likely to in our academic careers as first-years.

We do plan to work on this further to string together the pieces, and expand the functionality to the following:
- Integrate an AI Voice assistant rather than the speech confirmation algorithm currently used to enable more interactive interaction with the webapp
- Add an ordering feature for "favorited" ingredients which would then be ordered immediately if they are identified as not available during a scan
- Adding the funcitonality to favorite/save recipes for easier access
