"""
FelipedelosH

This file play with Turismoi DB info:

0 > ID_country
1 > ISO_country
2 > NAME_country
3 > NAME_PRINT_country
4 > ISO3_country
5 > CODE_country
6 > NAME_ESP_country
7 > id_city
8 > region_id
9 > name_place
10 > short_name_place
11 > slug_place
12 > group_id_place
13 > province_id_place
14 > group_slug_place
15 > latitude
16 > longitude
17 > country_host_id_place
"""
from itertools import count
from Database import *
from LatLonValidator import *
class TurismoiDATA:
    def __init__(self) -> None:
        self.data = {} # {iso_country.lower().LRstrip() + ":" + city_name.lower().LRstrip()}
        self.metadata = {}
        self.metadataReading = {}


        self.count = 0
        self.database = Database()
        self.geoLatLngValidator = GeoLatLongValidator()

    def chargeInfoInDatabase(self, txt):
        """
        Enter a info of : DATA/turismoi.csv
        And save in table turismoi
        """
        for i in txt.split("\n")[1:-1]:
            data = i.split("|")

            iso_country = str(data[1]).lower().strip()
            name_city = str(data[11])
            key = iso_country + ":" + name_city.lower().lstrip().rstrip().replace('-', ' ')
            
            # Save in memory:
            if key in self.data.keys():
                self.metadataReading["Err:Duplicate:"+str(self.count)] = " >> " + key
                self.count = self.count + 1
            else:
                self.data[key] = i




            # Info to send a database:
            id = key
            ID_country = data[0]
            ISO_country = data[1]
            NAME_country = data[2]
            NAME_PRINT_country = data[3]
            ISO3_country = data[4]
            CODE_country = data[5]
            NAME_ESP_country = data[6]
            id_city  = data[7]
            region_id = data[8]
            name_place  = data[9]
            short_name_place = data[10]
            slug_place = data[11]
            group_id_place = data[12]
            province_id_place = data[13]
            group_slug_place = data[14]
            latitude = data[15]
            try:
                latitude = float(latitude)
            except:
                latitude = None
            longitude = data[16]
            try:
                longitude = float(longitude)
            except:
                longitude = None
            country_host_id_place = data[17]

            info = (id,
            ID_country,
            ISO_country,
            NAME_country,
            NAME_PRINT_country,
            ISO3_country,
            CODE_country,
            NAME_ESP_country,
            id_city,
            region_id,
            name_place,
            short_name_place,
            slug_place,
            group_id_place,
            province_id_place,
            group_slug_place,
            latitude,
            longitude,
            country_host_id_place
            )

            self.database.insertInfoInTurismoi(info)

        self.metadata = self.database.metadata

    def resetMetadata(self):
        self.count = 0
        self.metadata = {}

    def getGeoLatLngViaKeyDic(self, key):
        info = "NULL|NULL"

        if key in self.data:
            data = self.data[key].split("|")
            latitude = data[15]
            longitude = data[16]

            if self.geoLatLngValidator.validates(latitude, longitude):
                info = latitude + "|" + longitude

        return info

    def updateGEOviaKeyDic(self, key, geo):
        if key in self.data.keys():
            # Update in RAM
            dataToEdit = self.data[key]
            dataToEdit = dataToEdit.split("|")
            new_latude = geo.split("|")[0]
            new_longitude =  geo.split("|")[1]
            dataToEdit[15] = new_latude
            dataToEdit[16] = new_longitude
            # ReStruct the data
            final_data = ""
            for i in dataToEdit:
                final_data = final_data + i + "|"

            final_data = final_data.replace('|||', '||')

            # Update in DB
            #self.database.updateGEOLatLngInTurismoi(key, new_latude, new_longitude)

            self.data[key] = final_data
            self.metadata["dbUPDATE:"+str(self.count)] = "UPDATE GEO >> " + key + " : " + geo
            self.count = self.count + 1    
        








