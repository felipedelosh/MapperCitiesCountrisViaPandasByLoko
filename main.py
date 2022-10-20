"""
FelipedelosH

"""
import re
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="This is a main banner")
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")
        self.btnLoadFiles = Button(self.canvas, text="LOAD FILES")


        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Turismoi MAPPER by loko v2.0")
        self.screem.geometry("720x480")
        self.canvas['width'] = 720
        self.canvas['height'] = 480
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=20, y=20)
        self.lblFooterProgram.place(x=300, y=450)



        self.screem.mainloop()




s = Software()