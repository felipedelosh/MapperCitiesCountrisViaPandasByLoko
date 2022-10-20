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
