"""
FelipedelosH

This class save and get all project info into: dbTest.db

"""
import sqlite3

class Database:
    def __init__(self) -> None:
        self.conexion = self.getConect()
        self.metadata = {}
        self.counter = 0

    def getConect(self):
        return sqlite3.connect("DBtest.db")

    def initDatabase(self):
        try:
            sql = """
            create table if not exists Cities(
                Id integer,
                CityCode text,
                CountryId integer,
                DescriptionES text,
                DescriptionEN text,
                DescriptionPT text,
                Latitude double,
                Longitude double,
                ProvinceId text,
                IsSearchable integer,
                IsSearchableBus integer,
                TimeZone text
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: Cities"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: Cities"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists Countries(
                Id integer,
                CountryCode text,
                IsRegional intger,
                DescriptionES text,
                DescriptionEN text,
                DescriptionPT text,
                CountryCodeIso3Dig text,
                PhonePrefix text
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: Countries"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: Countries"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists turismoi(
                id text primary key,
                ID_country text,
                ISO_country text,
                NAME_country text,
                NAME_PRINT_country text,
                ISO3_country text,
                CODE_country text,
                NAME_ESP_country text,
                id_city text,
                region_id text,
                name_place text,
                short_name_place text,
                slug_place text,
                group_id_place text,
                province_id_place text,
                group_slug_place text,
                latitude double,
                longitude double,
                country_host_id_place text
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: turismoi"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: turismoi"
        self.counter = self.counter + 1


    def insertInfoCities(self, txt):
        """
        Id integer,
        CityCode text,
        CountryId integer,
        DescriptionES text,
        DescriptionEN text,
        DescriptionPT text,
        Latitude double,
        Longitude double,
        ProvinceId text,
        textIsSearchable integer,
        IsSearchableBus integer,
        TimeZone text
        """
        self.conexion = self.getConect()
        count_insert_ok = 0
        count_insert_fail = 0
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                Id = data[0]
                Id = int(Id)
                CityCode = data[1]
                CityCode = str(CityCode).replace("\"", "")
                CountryId = data[2]
                CountryId = int(CountryId)
                DescriptionES = data[3]
                DescriptionEN = data[4]
                DescriptionPT = data[5]
                Latitude = data[6]
                Latitude = float(Latitude)
                Longitude = data[7]
                Longitude = float(Longitude)
                ProvinceId = data[8]
                IsSearchable = data[9]
                IsSearchable = int(IsSearchable)
                IsSearchableBus = data[10]
                IsSearchableBus = int(IsSearchableBus)
                TimeZone = data[11]
                
                self.conexion.execute("insert into Cities (Id,CityCode,CountryId,DescriptionES,DescriptionEN,DescriptionPT,Latitude,Longitude,ProvinceId,IsSearchable,IsSearchableBus,TimeZone) values (?,?,?,?,?,?,?,?,?,?,?,?)",(Id,CityCode,CountryId,DescriptionES,DescriptionEN,DescriptionPT,Latitude,Longitude,ProvinceId,IsSearchable,IsSearchableBus,TimeZone))
                self.metadata[str(self.counter)] = "Insert info in Cities:" + str(data[0])
                count_insert_ok = count_insert_ok + 1
            except:
                self.metadata[str(self.counter)] = "Error in info in Cities:" + str(data[0])
                count_insert_fail = count_insert_fail + 1
            self.counter = self.counter + 1
        self.metadata["TOTAL_INSERTED:"] = str(count_insert_ok)
        self.metadata["TOTAL_ERR:"] = str(count_insert_fail)
        self.conexion.commit()
        self.conexion.close()


    def inserInfoCopuntries(self, txt):
        """
        Id integer,
        CountryCode text,
        IsRegional intger,
        DescriptionES text,
        DescriptionEN text,
        DescriptionPT text,
        CountryCodeIso3Dig text,
        PhonePrefix text
        """
        self.metadata = {}
        self.counter = 0
        count_insert_ok = 0
        count_insert_fail = 0
        self.conexion = self.getConect()
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                Id = data[0]
                Id = int(Id)
                CountryCode = data[1]
                IsRegional = data[2]
                try:
                    IsRegional = int(IsRegional)
                except:
                    IsRegional = 0
                DescriptionES = data[3]
                DescriptionEN = data[4]
                DescriptionPT = data[5]
                CountryCodeIso3Dig = data[6]
                PhonePrefix = data[7]
                PhonePrefix = str(PhonePrefix).replace("\"","")
                self.conexion.execute("insert into Countries (Id,CountryCode,IsRegional,DescriptionES,DescriptionEN,DescriptionPT,CountryCodeIso3Dig,PhonePrefix) values (?,?,?,?,?,?,?,?)",(Id,CountryCode,IsRegional,DescriptionES,DescriptionEN,DescriptionPT,CountryCodeIso3Dig,PhonePrefix))
                count_insert_ok = count_insert_ok + 1
                self.metadata[str(self.counter)] = "Insert info in Countries:" + str(data[0])
            except:
                count_insert_fail = count_insert_fail + 1
                self.metadata[str(self.counter)] = "Error in info in Countries:" + str(data[0])
            self.counter = self.counter + 1
        self.metadata["TOTAL_INSERTED:"] = str(count_insert_ok)
        self.metadata["TOTAL_ERR:"] = str(count_insert_fail)
        self.conexion.commit()
        self.conexion.close()

































    def insertInfoInTurismoi(self, data):
        """
        create table if not exists turismoi(
            id text primary key,
            ID_country text,
            ISO_country text,
            NAME_country text,
            NAME_PRINT_country text,
            ISO3_country text,
            CODE_country text,
            NAME_ESP_country text,
            id_city text,
            region_id text,
            name_place text,
            short_name_place text,
            slug_place text,
            group_id_place text,
            province_id_place text,
            group_slug_place text,
            latitude double,
            longitude double,
            country_host_id_place text
        )
        """
        try:
            self.conexion = self.getConect()
            id = data[0]
            ID_country = data[1]
            ISO_country = data[2]
            NAME_country = data[3]
            NAME_PRINT_country = data[4]
            ISO3_country = data[5]
            CODE_country = data[6]
            NAME_ESP_country = data[7]
            id_city = data[8]
            region_id = data[9]
            name_place = data[10]
            short_name_place = data[11]
            slug_place = data[12]
            group_id_place = data[13]
            province_id_place = data[14]
            group_slug_place = data[15]
            latitude = data[16]
            longitude = data[17]
            country_host_id_place = data[18]
            self.conexion.execute("insert into turismoi (id,ID_country,ISO_country,NAME_country,NAME_PRINT_country,ISO3_country,CODE_country,NAME_ESP_country,id_city,region_id,name_place,short_name_place,slug_place,group_id_place,province_id_place,group_slug_place,latitude,longitude,country_host_id_place) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id,ID_country,ISO_country,NAME_country,NAME_PRINT_country,ISO3_country,CODE_country,NAME_ESP_country,id_city,region_id,name_place,short_name_place,slug_place,group_id_place,province_id_place,group_slug_place,latitude,longitude,country_host_id_place))
            self.conexion.commit()
            self.conexion.close()
            self.metadata[str(self.counter)] = "Insert info in turimoui:" + str(data[0])
        except:
            self.metadata[str(self.counter)] = "Error in info in turimoui:" + str(data[0])
        self.counter = self.counter + 1









    def getAllTurismoiInfo(self):
        """
        create table if not exists turismoi(
            id text primary key,
            ID_country text,
            ISO_country text,
            NAME_country text,
            NAME_PRINT_country text,
            ISO3_country text,
            CODE_country text,
            NAME_ESP_country text,
            id_city text,
            region_id text,
            name_place text,
            short_name_place text,
            slug_place text,
            group_id_place text,
            province_id_place text,
            group_slug_place text,
            latitude double,
            longitude double,
            country_host_id_place text
        )  
        """
        total = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from turismoi")
            fila=cursor.fetchall()
            for i in fila:
                id = i[0]
                ID_country = i[1]
                ISO_country = i[2]
                NAME_country = i[3]
                NAME_PRINT_country = i[4]
                ISO3_country = i[5]
                CODE_country = i[6]
                NAME_ESP_country = i[7]
                id_city = i[8]
                region_id = i[9]
                name_place = i[10]
                short_name_place = i[11]
                slug_place = i[12]
                group_id_place = i[13]
                province_id_place = i[14]
                group_slug_place = i[15]
                latitude = i[16]
                longitude = i[17]
                country_host_id_place = i[18]
                json = {"id":id,
                "ID_country":ID_country,
                "ISO_country":ISO_country,
                "NAME_country":NAME_country,
                "NAME_PRINT_country":NAME_PRINT_country,
                "ISO3_country":ISO3_country,
                "CODE_country":CODE_country,
                "NAME_ESP_country":NAME_ESP_country,
                "id_city":id_city,
                "region_id":region_id,
                "name_place":name_place,
                "short_name_place":short_name_place,
                "slug_place":slug_place,
                "group_id_place":group_id_place,
                "province_id_place":province_id_place,
                "group_slug_place":group_slug_place,
                "latitude":latitude,
                "longitude":longitude,
                "country_host_id_place":country_host_id_place}
                total.append(json)
            cursor.close()
        except:
            pass

        return total



    def getAllCitiesInfo(self):
        """
        create table if not exists Cities(
            Id integer,
            CityCode text,
            CountryId integer,
            DescriptionES text,
            DescriptionEN text,
            DescriptionPT text,
            Latitude double,
            Longitude double,
            ProvinceId text,
            IsSearchable integer,
            IsSearchableBus integer,
            TimeZone text
        """
        total = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from Cities")
            fila=cursor.fetchall()
            for i in fila:
                Id = i[0]
                CityCode = i[1]
                CountryId = i[2]
                Latitude = i[6]
                Longitude = i[7]
                json = {"Id":Id,"CityCode":CityCode,"CountryId":CountryId,"Latitude":Latitude,"Longitude":Longitude}
                total.append(json)
            cursor.close()
        except:
            pass

        return total


    def getAllCountries(self):
        """
        create table if not exists Countries(
            Id integer,
            CountryCode text,
            IsRegional intger,
            DescriptionES text,
            DescriptionEN text,
            DescriptionPT text,
            CountryCodeIso3Dig text,
            PhonePrefix text
        )
        """
        total = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from Countries")
            fila=cursor.fetchall()
            for i in fila:
                Id = i[0]
                CountryCode = i[1]
                DescriptionES = i[3]
                json = {"Id":Id,"CountryCode":CountryCode,"DescriptionES":DescriptionES}
                total.append(json)
            cursor.close()
        except:
            pass

        return total


























    def getTotalRowsOfTableX(self, nameTable):
        total = 0

        self.conexion = self.getConect()
        sql = "select count(*) from " + nameTable
        cursor = self.conexion.execute(sql)
        fila=cursor.fetchone()
        try:
            total = str(fila).replace('(', '')
            total = total.replace(')', '')
            total = total.replace(',', '')
            total = int(total)
            self.metadata[str(self.counter)] = "Get Total of table: " + nameTable
        except:
            self.metadata[str(self.counter)] = "Error in get Total of table: " + nameTable

        self.counter = self.counter + 1
        return total
