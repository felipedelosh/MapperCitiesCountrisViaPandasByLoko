"""
FelipedelosH



"""
import os
from os import scandir
from Database import *
from Turismoi import *
from Geography import *

class Controller:
    def __init__(self) -> None:
        self.database = Database()
        self.database.initDatabase()
        self.saveMetadata("DATABASE/dbCreate.txt", self.database.metadata)
        self.dataTurimoi = TurismoiDATA()
        self.geography = Geografy()
        self.consoleTXT = ""

    def loadFiles(self):
        data_cities  = self.rtnArcheveInfo("RESOURCES/Cities.csv")
        self.geography.insertInfoCities(data_cities)
        self.saveMetadata("DATABASE/dbInsertCities.txt", self.geography.metadata)

        data_countries = self.rtnArcheveInfo("RESOURCES/Countries.csv")
        self.geography.insertInfoCountries(data_countries)
        self.saveMetadata("DATABASE/dbInsertCountries.txt", self.geography.metadata)

        data_turismoi = self.rtnArcheveInfo("DATA/turismoi.csv")
        self.dataTurimoi.chargeInfoInDatabase(data_turismoi)
        self.saveMetadata("DATABASE/dbInsertTurismoi.txt", self.dataTurimoi.metadata)
        self.saveMetadata("READ/turismoi.txt", self.dataTurimoi.metadataReading)

    def saveFiles(self):
        self._saveDatabase()
        self._saveRAMfiles()


    def _saveDatabase(self):
        # Save a countries info:
        data = self.database.getAllCitiesInfo()
        self.saveArrayJson("OUTPUT/DATABASE/cities.txt", data)

        # Save a countries
        data = self.database.getAllCountries()
        self.saveArrayJson("OUTPUT/DATABASE/countries.txt", data)

        # Save a turismoi database info:
        data = self.database.getAllTurismoiInfo()
        self.saveArrayJson("OUTPUT/DATABASE/turismoi.txt", data)



    def _saveRAMfiles(self):
        self.saveRAMData("OUTPUT/RAM/turismoi.txt", self.dataTurimoi.data)


        

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
            pass

    def saveRAMData(self, filename, information):
        try:
            data = ""
            for i in information:
                data = data + str(i) + " >> " +  information[i] + "\n"

            f = open(filename, "w", encoding="UTF-8")
            f.write(data)
            f.close()
            print("Archivo creado: ", filename)
        except:
            print("Error creando:", filename)


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

