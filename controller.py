"""
FelipedelosH



"""
import os
from os import scandir
from Database import *

class Controller:
    def __init__(self) -> None:
        self.database = Database()
        self.database.initDatabase()
        self.saveMetadata("DATABASE/db.txt", self.database.metadata)

    def loadFiles(self):
        pass

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

