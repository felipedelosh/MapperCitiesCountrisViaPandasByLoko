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
