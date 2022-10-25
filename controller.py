"""
FelipedelosH



"""
import os
from os import scandir
from Database import *
from Macher import Macther
from Turismoi import *
from Geography import *
from serializeTree import SerializeTree
from Macher import *
from Target import *

class Controller:
    def __init__(self) -> None:
        self.database = Database()
        self.database.initDatabase()
        self.saveMetadata("DATABASE/dbCreate.txt", self.database.metadata)
        self.dataTurimoi = TurismoiDATA()
        self.target = Target_to_macth() # With Turismoi
        self.geography = Geografy()
        self.serializerTreeFromDB = SerializeTree()
        self.macther = Macther()
        self.consoleTXT = ""

    def loadFiles(self):
        total_cities = self.database.getTotalRowsOfTableX("Cities")
        print("Total de ciudades en DB: ", str(total_cities))
        if total_cities == 0:
            data_cities  = self.rtnArcheveInfo("RESOURCES/Cities.csv")
            print("Se ingresaran un total de Cities: ", str(len(str(data_cities).split("\n"))))
            self.geography.insertInfoCities(data_cities)
            self.saveMetadata("DATABASE/dbInsertCities.txt", self.geography.metadata)

        total_countries = self.database.getTotalRowsOfTableX("Countries")
        print("Total de Countries en DB: ", str(total_countries))
        if total_countries == 0:
            data_countries = self.rtnArcheveInfo("RESOURCES/Countries.csv")
            print("Se ingresarán a la base de datos: ", str(len(str(data_countries).split("\n"))))
            self.geography.insertInfoCountries(data_countries)
            self.saveMetadata("DATABASE/dbInsertCountries.txt", self.geography.metadata)

        total_turismoi = self.database.getTotalRowsOfTableX("turismoi")
        print("Total datos de turismoi: ", str(total_turismoi))
        if total_turismoi == 0:
            data_turismoi = self.rtnArcheveInfo("DATA/turismoi.csv")
            print("Se ingresará la Db turismoi: ", str(len(str(data_turismoi).split("\n"))))
            self.dataTurimoi.chargeInfoInDatabase(data_turismoi)
            self.saveMetadata("DATABASE/dbInsertTurismoi.txt", self.dataTurimoi.metadata)
            self.saveMetadata("READ/turismoi.txt", self.dataTurimoi.metadataReading)

        total_netactica_db = self.database.getTotalRowsOfTableX("netactica")
        print("Total datos Netactica DB: ", str(total_netactica_db))
        total_netactica_ram = len(self.geography.data)
        print("Total datos Netactica RAM: ", str(total_netactica_ram))

        if total_netactica_db == 0:
            data_netactica = self.rtnArcheveInfo("RESOURCES/netactica.csv")
            print("Se ingresarán un total de datos de Netactica: ", str(len(str(data_netactica).split("\n"))))
            self.geography.chargeNetacticaData(data_netactica)
            self.saveMetadata("READ/netactica.txt", self.geography.metadata)


        # To kDtree tables
        total_geo_ancestor = self.database.getTotalRowsOfTableX("geo_ancestor")
        print("Total de datos geo_ancestor: ", str(total_geo_ancestor))
        if total_geo_ancestor == 0:
            data_geo_ancestor = self.rtnArcheveInfo("RESOURCES/geo_ancestor.csv")
            print("Se ingresarán a la base de datos Geo ancestor: ", str(len(str(data_geo_ancestor).split("\n"))))
            self.database.insertInfoGeoAncestor(data_geo_ancestor)

        total_geo_geography = self.database.getTotalRowsOfTableX("geo_geography")
        print("Total datos en geo_geography: ", str(total_geo_geography))
        if total_geo_geography == 0:
            data_geo_geography = self.rtnArcheveInfo("RESOURCES/geo_geography.csv")
            print("Se ingresarán a la base de datos geo_geography:", str(len(str(data_geo_geography).split("\n"))))
            self.database.insertInfoGeoGeography(data_geo_geography)
        
        total_geo_lat_lng = self.database.getTotalRowsOfTableX("geo_latitude_longitude")
        print("Total datos en geo_latitude_longitude: ", str(total_geo_lat_lng))
        if total_geo_lat_lng == 0:
            data_geo_lat_lng = self.rtnArcheveInfo("RESOURCES/geo_latitude_longitude.csv")
            print("Se ingresarán a DB geo_latitude_longitude: ", str(len(str(data_geo_lat_lng).split("\n"))))
            self.database.insertinfoGeoLatitudeLongitude(data_geo_lat_lng)

        total_geo_polygon_shape = self.database.getTotalRowsOfTableX("geo_polygon_shape")
        if total_geo_polygon_shape == 0:
            data_geo_polygon_shape = self.rtnArcheveInfo("RESOURCES/geo_polygon_shape.csv")
            print("Se ingresarán a Db geo_polygon_shape: ", str(len(str(data_geo_polygon_shape).split("\n"))))
            self.database.insertinfoGeoPolygonShape(data_geo_polygon_shape)

        total_geo_polygon = self.database.getTotalRowsOfTableX("geo_polygon")
        print("Total datos en geo_polygon: ", str(total_geo_polygon))
        if total_geo_polygon == 0:
            data_geo_polygon = self.rtnArcheveInfo("RESOURCES/geo_polygon.csv")
            print("Se ingresarán a la base de datos: ", str(len(str(data_geo_polygon).split("\n"))))
            self.database.insertinfoGeoPolygon(data_geo_polygon)

        total_target = self.database.getTotalRowsOfTableX("target")
        print("Total Datos en target: ", str(total_target))
        if total_target == 0:
            data = self.rtnArcheveInfo("DATA/target.csv")
            print("Se ingresaran A DB en target: ", str(len(str(data).split("\n"))))
            # 0 Code;1 Name;2 Creation date;Latitude;Longitude;Zoom;Airport IATA;Country
            self.target.delimiter = ";"
            self.target.id_position = -1
            self.target.code_position = 0
            self.target.name_place_position = 1
            self.target.latitude_position = 3
            self.target.longitude_position = 4
            self.target.loadData(data)
            self.saveMetadata("READ/target.txt", self.target.metadata)



        print("....Database ENDE....")
        

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

        # Save target Info
        data = self.database.getAllTargetInfo()
        self.saveArrayJson("OUTPUT/DATABASE/target.txt",data)


        # Save MACTH turismoi via KDtree
        data = self.database.getAllMacthTurismoiInfoToCSV()
        headers = "id|iso_country|slug_place|latitude|longitude|nearest_iata_code|kdtree_dist_ns_cities_id"
        self.saveCSV("OUTPUT/turismoiMACTH.csv", data, headers)

        # Sace MACTH target via KDtree
        data = self.database.getAllMacthTargetInfoToCSV()
        self.saveCSV("OUTPUT/targetMACTH.csv", data, headers)

        



    def _saveRAMfiles(self):
        self.saveRAMData("OUTPUT/RAM/turismoi.txt", self.dataTurimoi.data)

    def addGeoLatLngViaNetactica(self):
        self.geography.resetMetadata()
        self.dataTurimoi.resetMetadata()
        # If find in RAM:
        total_data = len(self.dataTurimoi.data)
        if total_data > 0:
            print("Cargando datos Netactica.Turismoi desde RAM....")
            # Only Update
            count = 0
            count_percent = 0
            current_percent = 0
            top_percent = 0
            for i in self.dataTurimoi.data:
                GEO = self.dataTurimoi.getGeoLatLngViaKeyDic(i)
                

                if GEO == "NULL|NULL":
                    newGEO = self._addGeoLatLngViaNetactica(i)
                    if newGEO != "NULL|NULL":
                        self.updateGEOLatLngInTurismoi(i, newGEO)
                        count = count + 1

                current_percent = (count_percent / total_data) * 100
                if current_percent >= top_percent:
                    print(current_percent, " % ")
                    top_percent = top_percent + 10
                count_percent = count_percent + 1
            


        total_reg_turismoi = self.database.getTotalRowsOfTableX("turismoi")

        self.saveMetadata("MACTH/turismoi.join.netactica.txt", self.geography.metadata)
        self.saveMetadata("DATABASE/dbUpdateTurismoi.txt", self.dataTurimoi.metadata)

    def _addGeoLatLngViaNetactica(self, keyTurismoi):
        iso_code = keyTurismoi.split(":")[0]
        city_name = keyTurismoi.split(":")[1]
        allRegInfo = self.dataTurimoi.data[keyTurismoi]
        delimiter = "|"
        vecPosToSearch = [9,10,11]
        return self.geography.getGeoLatLongViaName(iso_code,city_name,allRegInfo,delimiter,vecPosToSearch)
        
    def serializeTree(self):
        self.serializerTreeFromDB.serialize()


    def updateGEOLatLngInTurismoi(self, key, geo):
        self.dataTurimoi.updateGEOviaKeyDic(key, geo)

    def macthTurismoiViaKdTree(self):
        self.macther.tryToMacthTurismoi()

    def macthTargetViaKdTree(self):
        self.macther.tryToMacthTarget()

    def continueMacthTargetViaKdTree(self):
        self.macther.continueTryToMacthTarget()

    def deleteAllFromTurismoi(self):
        self.database.deleteAllFromTurismoi()


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

    def saveCSV(self, path, info, headers):
        """
        path: path/filename.csv
        info: all data
        headers = h1|h2|h3|
        """
        try:
            f = open(path, 'w', encoding="UTF-8")
            f.write(headers+"\n"+info)
            f.close()
            print("Creado el archivo: ", path)
        except:
            print("Error creando CSV")

