"""
FelipedelosH

get DB and generate binary files:
"""
from Database import *
import pandas as pd
from scipy import spatial
import pickle

class SerializeTree:
    def __init__(self) -> None:
        self.database = Database()

    def serialize(self):
        print("LoadKDTreeForNsCities()")
        rigaDb = self.database.getConect()
        sql = """
        select id, latitude, longitude from geo_geography where has_polygon = True and status = 0
        """
        citiesNs = pd.read_sql_query(sql, con=rigaDb)
        cities = []
        for index, row in citiesNs.iterrows():
            #print((row['latitude'], row['longitude']))
            cities.append((row['latitude'], row['longitude']))
        rigaDb.close()
        tree = spatial.cKDTree(cities)
        pickle.dump(tree, open('BIN/geography.tree', 'wb'))
        pickle.dump(citiesNs, open('BIN/geography.pandas', 'wb'))
        print("Generando archivos BIN: geography.tree + geography.pandas")
        print("LoadKDTreeForGeography()")
        nsDb = self.database.getConect()
        sql = """
        select 
        Cities.Id,
        Cities.CityCode,
        Cities.Latitude,
        Cities.Longitude,
        Cities.DescriptionES,
        C.DescriptionES
        from 
        Cities inner join Countries C on Cities.CountryId = C.Id
        where (Latitude <> 0 or Latitude is not null)
        and 
        IsSearchable = 1
        and
        Cities.CityCode not in
        ('BR_6845','B24','BR_6851','B07','BAU','RD1','BR_8385','B10','PYA','BU1','94A','A04','BR_9028','CO_0313','CO2','B17','CO_0790','B09','B08','ISR','B22','BR_8509','BR_8518','JUA','ELF','BR_10163','CO_9002','BR_112','B04','MOY','BR_5362','B14','B19','BR_7012','B01','B25','POT','PO1','AR9','M23','PUX','B13','SAD','BR_8681','BR_9625','A15','A16','A17','GPL','XH1','BR4','BR5','BR6','B02','S25','M05','M08')
        """
        citiesNs = pd.read_sql_query(sql, con=nsDb)
        cities = []
        for index, row in citiesNs.iterrows():
            cities.append((row['Latitude'], row['Longitude']))

        tree = spatial.cKDTree(cities)
        pickle.dump(tree, open('BIN/nscities.tree', 'wb'))
        pickle.dump(citiesNs, open('BIN/nscities.pandas', 'wb'))
        print("Generando archivos: nscities.tree + nscities.pandas")
