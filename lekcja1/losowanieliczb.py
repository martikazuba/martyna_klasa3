import random
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("Wprowadz liczbe: ")
        self.entrythingy["int"] = self.contents
        self.entrythingy.bind('<Key-Return>',
                             self.takeNumber())
    def takeNumber(self):
        self.b = int(self.contents)
        return self.b

root = tk.Tk()
myapp = App(root)
myapp.mainloop()


class RandomNumber():
    a = random.randint(0, 100)
    def Guessing(self):
        self.b = -1
        while self.a!=self.b:
            self.b = myapp.takeNumber()
            if self.a<self.b:
                print("Za duza liczba")
            elif self.a>self.b:
                print("Za mala liczba")
        print("Gratulacje zgadles liczbe")
a1 = RandomNumber()
a1.Guessing()
