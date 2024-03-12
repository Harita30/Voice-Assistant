# Voice-Assistant

## Experience 

First and foremost, I am grateful for the opportunity to work on a project of this kind. I was absolutely excited at being able to bring together various technical concepts, some of which I have prior hands-on experience with and some I didn’t. I started out strong with research, gathering resources, and laying out an implementation plan. Along the way, I encountered quite a lot of challenges testing both my technical ability and mental determination. But I chose to keep going because the learnings were many and the will to achieve was strong.  My methods and overall choice of tools could possibly be better. I hope to further explore and develop a more optimised solution. Overall, I definitely had a fun time and am looking forward to tackling more such problems. 
 
## About

I have used Python to develop this voice assistant. Python is a language I’ve used extensively in the recent past for all of my projects. It's more user-friendly and has a wide variety of libraries that support a whole lot of use cases. 
The voice assistant displays a thought-provoking question “Will virtual care redefine current healthcare paradigms?”, to which the user might respond with a yes or a no. In case of any other response or the lack of one, the assistant prompts the user to retry. A total of 3 tries are given, after which the execution terminates. The conversation is logged to a file named output.txt, which logs all interactions one after the other if there are multiple. 
 
## Methodology and challenges

**Speech recognition**: _SpeechRecognition_ library has been used to recognize speech input from the host machine’s microphone. This library interacts with various backends and is quite easy to install and get started with.   

**Speech-to-text**: The captured audio from the speech is passed to the backend _recognize_sphinx_ module of the pocketsphinx library which returns the equivalent text. I have enabled United States, Great Britain, and Indian English accents to be recognized.   
_Pocketsphinx_ of Carnegie Mellon University is an open-source speech recognition engine. I previously attempted implementation using the google speech recognition API, but it had additional components of credentials and pricing.   

**User interface**: For the user interface, I faced quite a few challenges as I primarily work on a macOS. A quick google search will tell you _PySimpleGUI_ is the most preferred and easiest to master. _Pyqt5_ and _Tkinter_ come in next. While they provide great UI capabilities, they are a tad bit harder to master. And _Flask_ with _HTML_ was another alternative I experimented with. 

The methods I used, and the usage results are outlined in the table below. For my code, I eventually took on the challenge of learning to build with _Tkinter_ and have implemented the same. The package however has issues with its working on mac. On a Windows machine, it works as expected.
 
#### Methods / Packages I tried	How it went?

- PySimpleGUI - Installer did not execute, and Python crashed   

- Flask and HTML - Methods to accept audio input into an HTML file- webkitSpeech & getUserMedia()	webkitSpeech- this      is only supported in the Google Chrome browser getUserMedia()- only works in a secure context   

- Pyqt5 & tkinter - Both the packages were similar, but since I was building a simple GUI, I found tkinter to be           sufficient   

**File output**: The voice assistant and user interactions are logged to a file named “output.txt”. A file object is used to open the file in append mode. This enables all subsequent conversations to be logged in one place.   

**Error and exception handling**: I have accounted for errors due to API unavailability, an error in the request, and invalid instance types. As a part of the implementation, in case the user’s speech is unrecognizable or inaudible, the assistant gives them additional tries to get it right.   

**Recognizer attributes**: I have set the attribute values for background noise, speech to background noise ratio, phrase limit duration to allow enough time for a “yes or “no” answer, dynamic energy threshold to balance out according to the silence or noise levels of the room/surroundings.   

**Threads**: I used a daemon thread to execute the speech recognition modules in the background, while the Tkinter mainloop executes in foreground, to allow the changes the speech recognition modules make to be reflected on the UI.
 
## How to run?
 
**To run the code on a python IDE**-   

1. Create a new project and a virtual environment.
   
3. **Run the commands**:

    1. pip install SpeechRecognition </br>
    2. pip install pocketsphinx</br>
    3. pip install pyaudio</br>
    4. pip install tk (if not already installed)</br>
    5. pip install urllib3==1.26.6 (as urllib3 v2.0 requires OpenSSL 1.1.1+ to work and the one on my system was         compiled       with LibreSSL. An older version of urllib helped)</br>
    6. pip install setuptools (for the distutils module an error I observed on a Windows EC2     

4. **Run the code**:
    
    - On a Windows machine to observe the complete working of the voice assistant.</br>
    - On a macOS machine, the tkinter package displays an empty screen with just the button.
 
## Working

1. The question and a button to exit first displays upon start-up.</br></br>
2. A prompt to speak then appears.</br></br>
3. The audio is processed, and the assistant responds with either the answer or with invalid response and allowing the      user to retry at the next prompt.</br></br>
4. If the user exhausts all tries, the execution ends with “Invalid response. Exiting..”</br></br>
5. The user is allowed to exit otherwise with the use of the exit button.
 

