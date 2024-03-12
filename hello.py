import tkinter
import speech_recognition as sr
import time
from threading import Thread
class GUI:
    #UI using tkinter module
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.main_window.geometry('600x400')

        self.top = tkinter.Frame(self.main_window)
        self.mid = tkinter.Frame(self.main_window)
        self.bot = tkinter.Frame(self.main_window)

        self.question = tkinter.Label(self.top, fg="black", font="Heather 12 bold", text='Will virtual care redefine current healthcare paradigms?')

        self.question.pack(side='left')

        self.statement2=tkinter.StringVar()

        self.sorry = tkinter.Label(self.mid, fg='black', font='Heather 15 bold', textvariable=self.statement2)

        self.sorry.pack(side='left', padx='50', pady='50')

        #Exit button
        self.exit = tkinter.Button(self.bot, text='EXIT', background='Black', font='Heather 14 bold', fg='White', command=self.main_window.destroy)

        self.exit.pack(side='left', padx='50', pady='20')

        self.top.pack()
        self.mid.pack()
        self.bot.pack()
        self.start_thread()
        tkinter.mainloop()
    #To allow a child process to execute the speech recognition definitions
    def start_thread(self):
        t= Thread(target=self.mic_input, daemon=True)
        t.start()
    def user_input(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        if not isinstance(r, sr.Recognizer):
            raise TypeError("'recognizer' must be 'Recognizer' instance")
        if not isinstance(m, sr.Microphone):
            raise TypeError("'microphone' must be 'Microphone' instance")
        response = None

        with m as source:
            self.fileob = open('output.txt', 'a')
            self.fileob.write('Will virtual care redefine current healthcare paradigms?\n')
            self.fileob.write('Speak now!\n')
            time.sleep(5)
            self.statement2.set('Speak now!')
            r.pause_threshold = 1
            #adjusting to ambient noise
            r.adjust_for_ambient_noise(source, duration=1)
            #Energy below 10 is considered silence
            r.energy_threshold = 10
            r.dynamic_energy_threshold = True
            #Speech is recognised as 1.5 higher than background noise
            r.dynamic_energy_adjustment_ratio = 1.5
            r.dynamic_energy_adjustment_damping = 0.15
            # setting a time limit so that it doesn't wait indefinitely or for too long
            audio = r.listen(source, phrase_time_limit=1)

        # I'm using Sphinx to implement speech to text conversion
        try:
            response = r.recognize_sphinx(audio, language="en-US" or "en-GB" or "en-IN")
        # if the API is unavailabe
        except sr.UnknownValueError:
            response = "unavailable"
        # if an error is encountered
        except sr.RequestError as e:
            response = "error"
        response = response.lower()
        return response

    def mic_input(self):
        tries = 1
        while tries < 4:
            answer = self.user_input()
            if answer == "yes" or answer == "no":
                self.fileob.write(f'you said {answer}\n')
                self.statement2.set(f'You said {answer}')
                break
            if answer == "unavailable" or answer == "error":
                self.fileob.write('Error. Exiting\n')
                self.statement2.set('Error. Exiting..')
                time.sleep(1)
                self.main_window.destroy()
                break
            if tries < 3:
                self.fileob.write('Invalid response. Repeat at the prompt!\n')
                self.statement2.set('Invalid response. Repeat at the prompt.')
                time.sleep(1)
            else:
                self.fileob.write('Invalid response. Exiting\n')
                self.statement2.set('Invalid response. Exiting..')
                time.sleep(3)
                self.main_window.destroy()
            tries += 1
        self.fileob.close()

if __name__ == '__main__':
    g=GUI()
