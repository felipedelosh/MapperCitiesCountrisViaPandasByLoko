"""
FelipedelosH

Thsi file is based in KdTree
Need this files:
BIN/geography.pandas
BIN/geography.tree
BIN/nscities.pandas
BIN/nscities.tree
"""
from Database import *
import pickle
import pandas as pd
from shapely.geometry import Point, Polygon
from decimal import Decimal
class Macther:
    def __init__(self) -> None:
        self.database = Database()
        self.geographyTree = None
        self.geographyDataFrame = None
        self.nsCitiesTree = None
        self.nsCitiesDataFrame = None

    def chargeBinFiles(self):
        # Open the pandas files.
        with open("BIN/geography.tree", "rb") as file:
            self.geographyTree = pickle.load(file)

        with open("BIN/geography.pandas", "rb") as file:
            self.geographyDataFrame = pickle.load(file)

        with open("BIN/nscities.tree", "rb") as file:
            self.nsCitiesTree = pickle.load(file)

        with open("BIN/nscities.pandas", "rb") as file:
            self.nsCitiesDataFrame = pickle.load(file)

    def tryToMacthTurismoi(self):
        self.chargeBinFiles()
        data = self.database.getTurismoiRichInformation()[0:100]
        total_data = len(data)
        print("Total files turismoi para Machear: ", str(total_data))
        
        count_percent = 0
        current_percent = 0
        top_percent = 0
        
        for i in data:
            #print("Buscando... >> ", str(i['id']))
            polygons = self.GetNearPolygons(i, polygonsCount=40) # Get ALL GEO
            polygons = self.ChooseContainerPolygons(i, polygons) #  if GEO eqls?
            geoIdList = None
            if polygons is not None:
                geoIdList = self.GetRelatedGeoIdsFromPolygon(polygons) # No idea ?
            self.GetNearCityFromNs(i)
            #print(str(i['id']), "macheado con >> ", str(i['nearest_iata_code']), " Dist: ", str(i['kdtree_dist_ns_cities_id']))
            self.saveMacthInDatabaseTurismoi(i) # Save a Macth In database

            current_percent = (count_percent/total_data)*100
            if current_percent >= top_percent:
                print(current_percent, " % ")
                top_percent = top_percent + 5
            count_percent = count_percent + 1


        


    def GetNearPolygons(self, target_place, polygonsCount=40):
        if len(self.geographyDataFrame) < polygonsCount:
            polygonsCount = len(self.geographyDataFrame)
        
        treeResult = self.geographyTree.query([target_place['lat'], target_place['lng']], k=polygonsCount)
        if treeResult is None:
            return None
        if len(treeResult[0]) == 0:
            return None

        nearestGeoPointsDf = self.geographyDataFrame.iloc[treeResult[1].tolist()]
        if len(nearestGeoPointsDf) == 0:
            return None
        
        nearestGeoPointsIdList = nearestGeoPointsDf['id'].tolist()
        nearestGeoPointsIdListQueryString = ','.join([str(elem) for elem in nearestGeoPointsIdList])

        queryPolygons = f"""
        select geo_id, ''||geo_id||'|'||gp.id as polygon_id, latitude, longitude, gps.point_order from geo_latitude_longitude
        inner join geo_polygon_shape gps on geo_latitude_longitude.id = gps.latlng_id
        inner join geo_polygon gp on gps.polygon_id = gp.id
        where gp.geo_id in ({nearestGeoPointsIdListQueryString})
        order by geo_id, gp.id, gps.point_order
        """
        rigaDb = self.database.getConect()
        filterts = str(nearestGeoPointsIdListQueryString)
        sql = "select geo_id, ''||geo_id||'|'||gp.id as polygon_id, latitude, longitude, gps.point_order from geo_latitude_longitude "
        sql = sql + "inner join geo_polygon_shape gps on geo_latitude_longitude.id = gps.latlng_id "
        sql = sql + "inner join geo_polygon gp on gps.polygon_id = gp.id "
        sql = sql + "where gp.geo_id in (" + filterts + ") "
        sql = sql + "order by geo_id, gp.id, gps.point_order"
        geoPolygonsDataFrame = pd.read_sql_query(sql, con=rigaDb)
        UniqueGeoPolygon = geoPolygonsDataFrame['polygon_id'].unique()
        DataFrameDict = {elem: pd.DataFrame for elem in UniqueGeoPolygon}
        for key in DataFrameDict.keys():
            DataFrameDict[key] = geoPolygonsDataFrame[:][geoPolygonsDataFrame['polygon_id'] == key]
        allPolygons = []
        for key in DataFrameDict.keys():
            polygonPointsDf = DataFrameDict[key]
            polygonData = []
            for index, row in polygonPointsDf.iterrows():
                polygonData.append((row['latitude'], row['longitude']))
            allPolygons.append({
                'key': key,
                'polygon': polygonData
            })
        return allPolygons 

    def ChooseContainerPolygons(self, target_place, polygons):
        choosedPolygons = []
        for polygonData in polygons:
            polygon = Polygon(polygonData['polygon'])
            if polygon.contains(Point(Decimal(target_place['lat']), Decimal(target_place['lng']))):
                choosedPolygons.append(polygonData)
        return None if len(choosedPolygons) == 0 else choosedPolygons


    def GetRelatedGeoIdsFromPolygon(self, polygons):
        if polygons is None:
            return None
        geoIdList = None
        for polygon in polygons:
            key = polygon['key']
            geo_id = key.split('|')[0]
            query = f'''
            select gg.id as geo_id from geo_ancestor inner join geo_geography gg 
            on geo_ancestor.ancestor_altern_id = gg.altern_id where geo_ancestor.geo_id={geo_id}
            '''
            rigaDb = self.database.getConect()
            geoIdDf = pd.read_sql_query(query, con=rigaDb)
            if geoIdList is None:
                geoIdList = geoIdDf['geo_id'].tolist()
            else:
                geoIdList.extend(geoIdDf['geo_id'].tolist())
            geoIdList.append(int(geo_id))
        uniqueIds = set(geoIdList)
        return list(uniqueIds)



    def GetNearCityFromNs(self, target_place):
        nsCitiesTree = self.nsCitiesTree
        nsCitiesDataFrame = self.nsCitiesDataFrame
        cityMapped = nsCitiesTree.query([target_place['lat'], target_place['lng']])
        if cityMapped is None:
            return None
        target_place['nearest_iata_code'] = nsCitiesDataFrame.iloc[cityMapped[1]]['CityCode'] # Here you macth RESOURCES/Cities.csv[CityCode]
        target_place['kdtree_dist_ns_cities_id'] = cityMapped[0] # Here you calculate a distance


    def saveMacthInDatabaseTurismoi(self, target_place):
        """
        Only update a record
        """
        # Delete a before Macth
        self.database.deleteTurismoiMacthReg(target_place['id'])

        # Save a new Macth
        self.database.insertInfoTurismoiMacth(target_place)
