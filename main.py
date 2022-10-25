"""
FelipedelosH

"""
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Program to MAPPING turismoi")
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")
        self.btnLoadFiles = Button(self.canvas, text="LOAD FILES", command=self.loadFiles)
        self.btnSaveFiles = Button(self.canvas, text="SAVE FILES", command=self.saveFiles)
        
        self.lblAddGeoToTurismoi = Label(self.canvas, text="Agregar LAT LNG a Turismoi: ")
        self.btnADDGeoLatLngViaNetactica = Button(self.canvas, text="ADD GEO to turismoi", command=self.addGeoLatLngViaNetactica)

        self.btnCreateKDTreeBinFiles = Button(self.canvas, text="INIT KDTREE", command=self.serializeTree)
        self.btnMacthTurismoiKdTree = Button(self.canvas, text="Macth Turismoi KDtree", command=self.macthTurismoiViaKdTree)
        self.btnContinueMacthTurismoiKdTree = Button(self.canvas, text="Continue Macth Tu", command=self.continueMacthTurismoiViaKdTree)
        self.btnMacthTargetKdTree = Button(self.canvas, text="Macth Target KDtree", command=self.macthTargetViaKdTree)
        self.btnContinueMacthTargetKdTree = Button(self.canvas, text="Continue Macth TC", command=self.continueMacthTargetViaKdTree)
        
        self.btnHELP = Button(self.canvas, text="?", command=self.showHelpInterface)
        
        
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

        self.btnLoadFiles.place(x=20, y=80)
        self.btnSaveFiles.place(x=20, y=120)

        self.canvas.create_line(220, 50, 220, 160)

        self.lblAddGeoToTurismoi.place(x=20, y=200)
        self.btnADDGeoLatLngViaNetactica.place(x=20, y=230)

        self.btnCreateKDTreeBinFiles.place(x=400, y=60)
        self.btnMacthTurismoiKdTree.place(x=400, y=100)
        self.btnContinueMacthTurismoiKdTree.place(x=580, y=100)
        self.btnMacthTargetKdTree.place(x=400,y=140)
        self.btnContinueMacthTargetKdTree.place(x=580, y=140)

        self.btnHELP.place(x=680, y=20)

        self.screem.mainloop()

    def loadFiles(self):
        self.controller.loadFiles()

    def saveFiles(self):
        self.controller.saveFiles()

    def addGeoLatLngViaNetactica(self):
        self.controller.addGeoLatLngViaNetactica()

    def serializeTree(self):
        self.controller.serializeTree()
    
    def macthTurismoiViaKdTree(self):
        self.controller.macthTurismoiViaKdTree()

    def continueMacthTurismoiViaKdTree(self):
        self.controller.continueMacthTurismoiViaKdTree()

    def macthTargetViaKdTree(self):
        self.controller.macthTargetViaKdTree()

    def continueMacthTargetViaKdTree(self):
        self.controller.continueMacthTargetViaKdTree()

    def showHelpInterface(self):
        t = Toplevel()
        t.title("HELP")
        t.geometry("400x300")
        canvas = Canvas(t, width=400, height=300)
        canvas.place(x=0, y=0)
        btnDeleteTurismoi = Button(canvas, text="Delete * from turismoi", command=self.deleteAllFrontTurismoi)
        btnDeleteTurismoi.place(x=20, y=260)


    def deleteAllFrontTurismoi(self):
        self.controller.deleteAllFromTurismoi()



s = Software()
