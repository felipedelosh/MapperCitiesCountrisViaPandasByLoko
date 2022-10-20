"""
FelipedelosH



"""
import os
from os import scandir
from Database import *
from Turismoi import *

class Controller:
    def __init__(self) -> None:
        self.database = Database()
        self.database.initDatabase()
        self.saveMetadata("DATABASE/dbCreate.txt", self.database.metadata)
        self.dataTurimoi = TurismoiDATA()
        self.consoleTXT = ""

    def loadFiles(self):
        total_data_turismoi = self.database.getTotalRowsOfTableX("turismoi")
        data_turismoi = self.rtnArcheveInfo("DATA/turismoi.csv")
        self.dataTurimoi.chargeInfoInDatabase(data_turismoi)
        self.saveMetadata("DATABASE/dbInsertTurismoi.txt", self.dataTurimoi.metadata)
        self.saveMetadata("READ/turismoi.txt", self.dataTurimoi.metadataReading)

    def saveFiles(self):
        # Save a turismoi database info:
        data = self.database.getAllTurismoiInfo()
        self.saveArrayJson("OUTPUT/DATABASE/turismoi.txt", data)
        

    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


    def rtnArchieveFilesNames(self):
        """
        Return all files names of data folder
        """
        try:
            path = os.getcwd() + "/data"

            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if ".txt" in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return None


    def saveMetadata(self, filename, information):
        try:
            data = ""
            for i in information:
                data = data + str(i) + " >> " +  information[i] + "\n"

            f = open("METADATA/"+filename, "w", encoding="UTF-8")
            f.write(data)
            f.close()
        except:
            self.appendTextInConsoleText("Error write metadata >> " + filename)


    def saveArrayJson(self, title, data):
        """
        title = filename.txt
        data = [{},{},{}]
        """
        try:
            txt = ""
            for i in data:
                txt = txt + str(i) + "\n"
            
            f = open(title, 'w', encoding="UTF-8")
            f.write(txt)
            f.close()
            print("Archivo creado: ", title)
        except:
            print("Error creando el json")

