# Cook-Aid

Welcome to "Cook-Aid"
This is our Durhack 2023 submission, an aid application for visually-impared users (VIUs) to ease their cooking process. Our application scans in the ingredients you have at your disposal, optimized to the use of a phone camera and/or the ADLINK Neon-202B-JT2-X (1600 1200) industrial machine vision and AI smart camera, and then generates 3 recipes that you can make with what's available to you.

In the interest of extended accessibility, our application is to have embedded text-to-speech functionality to allow VIUs to smoothly navigate the program. As an extenstion, the application would also allow for speech-to-text communication with the program to process ingredients, confirm their identifications and select the final recipe choice.

--------
The backend functionalities depend on the following technologies:
- Open Computer Vision (CV2) (to recognize items in the snapshots/images)
- Google Translate's GTTS (to read out the text)
- Google Vision (to identify the ingredients scanned in)
- Recipe API (access: https://api-ninjas.com/api/recipe)
- Object Detection API (access: https://api-ninjas.com/api/objectdetection)
- Pyttsx3 Speech --> Text Library (+ Pyaudio)
- Open API (to match the identified ingredients to recipes in available API)
