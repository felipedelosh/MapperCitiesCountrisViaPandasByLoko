"""
felipedelosH

Controller all relationate with:

 * Globla geography
 * Kdtree resources


Netactica Headers
0 -> id
1 -> country_code
2 -> name_es
3 -> name_full_es
4 -> name_en
5 -> name_full_en
6 -> latitude
7 -> longitude
"""
from Database import *
from LatLonValidator import *
from WordsCompare import *
class Geografy:
    def __init__(self) -> None:
        self.data = {} # To SAVE RESOURCES/netactica.csv
        self.database = Database()
        self.geoLatLngValidator = GeoLatLongValidator()
        self.wordsComparer = WordsComparator()
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
        self.data = {}
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

    def getGeoLatLongViaName(self, iso_code, city_name, allRegInfo, delimiter, vecPosToSearch=[]):
        data = "NULL|NULL"
        found = False
        # Frist Search via key
        key = iso_code + ":" + city_name
        if key in self.data:
            found = True
            # To Macth table
            dataTurismoi = allRegInfo.split(delimiter)
            # 1 > ISO_country 7 > id_city 11 > slug_place
            dataTurismoi = dataTurismoi[1] + "|" + dataTurismoi[7] + "|" + dataTurismoi[11]
            # 1 -> country_code  0 -> id  2 -> name_es 
            dataNetactica = self.data[key].split("|")
            dataNetactica = dataNetactica[1] + "|" + dataNetactica[0] + "|" + dataNetactica[2]
            self.metadata["MACTID:"+str(self.count)] = dataTurismoi + "|" + dataNetactica
            self.count = self.count + 1
            GEO = self._getGeoLatLngViaKeyDic(key)
            if GEO != "NULL|NULL":
                data = GEO

        if not found:
            seraching = allRegInfo.split(delimiter)
            for i in self.data:
                # Only serach in country
                name_es = self.data[i].split("|")[2]
                name_en = self.data[i].split("|")[4]
                if iso_code+":" in i and city_name != "null":
                    for j in vecPosToSearch:
                        txtA = seraching[j]
                        # Search 2 -> name_es
                        if self.wordsComparer.compare(txtA, name_es):
                            # To Macth table
                            dataTurismoi = allRegInfo.split(delimiter)
                            # 1 > ISO_country 7 > id_city 11 > slug_place
                            dataTurismoi = dataTurismoi[1] + "|" + dataTurismoi[7] + "|" + dataTurismoi[11]
                            # 1 -> country_code  0 -> id  2 -> name_es 
                            dataNetactica = self.data[i].split("|")
                            dataNetactica = name_es
                            self.metadata["MACTNAMEES:"+str(self.count)] = dataTurismoi + "|" + dataNetactica
                            data = self._getGeoLatLngViaKeyDic(i)
                            self.count = self.count + 1
                            found = True
                            break

                        # Search 4 -> name_en 
                        if self.wordsComparer.compare(txtA, name_en):
                            # To Macth table
                            dataTurismoi = allRegInfo.split(delimiter)
                            # 1 > ISO_country 7 > id_city 11 > slug_place
                            dataTurismoi = dataTurismoi[1] + "|" + dataTurismoi[7] + "|" + dataTurismoi[11]
                            # 1 -> country_code  0 -> id  2 -> name_es 
                            dataNetactica = self.data[i].split("|")
                            dataNetactica = name_en
                            self.metadata["MACTNAMEEN:"+str(self.count)] = dataTurismoi + "|" + dataNetactica
                            data = self._getGeoLatLngViaKeyDic(i)
                            self.count = self.count + 1
                            found = True
                            break

                    if found:
                        break

                # Break for anothers contries
                if found: 
                    break


        return data
        
        
    def _getGeoLatLngViaKeyDic(self, key):
        info = "NULL|NULL"

        if key in self.data:
            data = self.data[key].split("|")
            latitude = data[6]
            longitude = data[7]

            if self.geoLatLngValidator.validates(latitude, longitude):
                info = latitude + "|" + longitude


        return info


    def resetMetadata(self):
        self.count = 0
        self.metadata = {}




        