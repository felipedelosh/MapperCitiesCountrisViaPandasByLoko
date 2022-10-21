"""
felipedelosH

Controller all relationate with:

 * Globla geography
 * Kdtree resources


Netactica Headers
id
country_code
name_es
name_full_es
name_en
name_full_en
latitude
longitude
"""
from Database import *

class Geografy:
    def __init__(self) -> None:
        self.data = {} # To SAVE RESOURCES/netactica.csv
        self.database = Database()
        self.metadata = {}
        self.count = 0

    def insertInfoCities(self, txt):
        """
        Insert info: RESOURCES/Cities.csv
        """
        self.database.insertInfoCities(txt)
        self.metadata = self.database.metadata

    def insertInfoCountries(self, txt):
        """
        RESOURCES/Countries.csv
        """
        self.database.inserInfoCopuntries(txt)
        self.metadata = self.database.metadata

    def chargeNetacticaData(self, txt):
        count = 0
        duplicated_control = 0
        for i in txt.split("\n")[1:-1]:
            data = i.split("|")
            iso_code = data[1].strip().lower()
            city_name = data[2].lower().lstrip().rstrip()
            city_name = city_name.replace('-', ' ')
            city_name = city_name.replace('\'', '')

            key = iso_code + ":" + city_name


            if key in self.data.keys():
                key = key + "-" + str(duplicated_control)
                duplicated_control = duplicated_control + 1
                self.metadata["Duplicated:"+str(self.count)] = key
                self.count = self.count + 1
            
            self.data[key] = i

        self.isTheDataLoad = True 
        self.metadata["Total_Reg_Inserted"] = str(len(self.data))
        self.metadata["Counter_err"] = str(count) 
        