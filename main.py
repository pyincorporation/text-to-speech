from tkinter import *
import pyttsx3

class SpeachToText():
    def __init__(self, root, engine):
        self.engine=engine
        self.root=root
        self.entry=Entry(width=50,)
        self.entry.grid(column=0, row=0, padx=30, pady=30, ipadx=30, ipady=20, columnspan=2)
        self.button_speak=Button(text='listen',bg='#313131', fg='white',width=20, command=lambda: self.speak_call())
        self.button_speak.grid(column=0, row=1, ipadx=10, ipady=15, )
        self.button_clear=Button(text='clear', bg='#e23f3f', fg='white', width=20, command=lambda: self.clear_call())
        self.button_clear.grid(column=1, row=1, ipadx=10, ipady=15, pady=20)

    def clear_call(self):
        self.entry.delete(0, END)

    def speak_call(self):
        user_text=self.entry.get()
        self.engine.say(user_text)
        self.engine.runAndWait()

if __name__ == '__main__':
    engine=pyttsx3.init()
    root=Tk()
    root.title('pyinc:Text-to-speech')
    root.resizable(width=False, height=False)
    speak=SpeachToText(root, engine)
    root.mainloop()
