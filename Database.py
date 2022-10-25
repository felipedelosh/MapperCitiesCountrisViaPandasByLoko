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
        try:
            sql = """
            create table if not exists turismoi_geo_add(
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
            self.metadata[str(self.counter)] = "Create Table: turismoi_geo_add"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: turismoi_geo_add"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists netactica(
                id integer,
                country_code text,
                name_es text,
                name_full_es text,
                name_en text,
                name_full_en text,
                latitude double,
                longitude double
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: netactica"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: netactica"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists geo_ancestor(
                id integer,
                type text,
                order_t integer,
                ancestor_altern_id text,
                geo_id integer
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: geo_ancestor"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: geo_ancestor"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists geo_geography(
                id integer,
                altern_id text,
                nearest_ns_cities_id integer,
                kdtree_dist_ns_cities_id double,
                nearest_iata_code text,
                type text,
                geo_class text,
                name text,
                name_full text,
                ascii_name text,
                country_code text,
                latitude double,
                longitude double,
                time_zone text,
                iata_code text,
                icao_code text,
                has_polygon boolean,
                last_update_utc text,
                validated_by text,
                user_service text,
                status integer
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: geo_geography"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: geo_geography"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists geo_latitude_longitude(
                id integer,
                latitude double,
                longitude double
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: geo_latitude_longitude"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: geo_latitude_longitude"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists geo_polygon_shape(
                polygon_id integer,
                latlng_id integer,
                point_order integer
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: geo_polygon_shape"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: geo_polygon_shape"
        self.counter = self.counter + 1
        try:
            sql = """
            create table if not exists geo_polygon(
                id integer,
                geo_id integer,
                type text
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: geo_polygon_shape"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: geo_polygon_shape"
        self.counter = self.counter + 1
        # This is to machted result of turismoi
        try:
            sql = """
            create table if not exists turismoi_macth(
                id text primary key,
                iso_country text,
                slug_place text,
                lat double,
                lng double,
                nearest_iata_code text,
                kdtree_dist_ns_cities_id double
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: turismoi_macth"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: turismoi_macth"
        self.counter = self.counter + 1
        # This is to machted result of target
        try:
            sql = """
            create table if not exists target_macth(
                id text primary key,
                iso_country text,
                slug_place text,
                lat double,
                lng double,
                nearest_iata_code text,
                kdtree_dist_ns_cities_id double
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: target_macth"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: target_macth"
        self.counter = self.counter + 1
        try:
            # This is another project to macth
            sql = """
            create table if not exists target(
                id text primary key,
                code text,
                iso_country text,
                name_place text,
                latitude double,
                longitude double
            )
            """
            con = self.getConect()
            con.execute(sql)
            con.close()
            self.metadata[str(self.counter)] = "Create Table: target"
        except:
            self.metadata[str(self.counter)] = "Error creating Table: target"
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



    def insertInfoGeoAncestor(self, txt):
        """
        id integer,
        type text,
        order_t integer,
        ancestor_altern_id text,
        geo_id integer
        """
        count_insert_ok = 0
        count_insert_fail = 0
        self.conexion = self.getConect()
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                id = str(data[0]).replace("\"", '')
                id = int(id)
                type_t = str(data[1]).replace("\"", '')
                order_t = str(data[2]).replace("\"", '')
                order_t = int(order_t)
                ancestor_altern_id = str(data[3]).replace("\"", '')
                geo_id = str(data[4]).replace("\"", '')
                geo_id = int(geo_id)
                #print((id, type_t, order_t, ancestor_altern_id, geo_id))
                self.conexion.execute("insert into geo_ancestor (id,type,order_t,ancestor_altern_id,geo_id) values(?,?,?,?,?)", (id, type_t, order_t, ancestor_altern_id, geo_id))
                count_insert_ok = count_insert_ok + 1
            except:
                #print("Error>>",i)
                count_insert_fail = count_insert_fail + 1

        print("Total registros insertados: ", str(count_insert_ok))
        print("Total registros con errores de insersiion: ", str(count_insert_fail))
        self.conexion.commit()
        self.conexion.close()



    def insertInfoGeoGeography(self, txt):
        """
        id integer,
        altern_id text,
        nearest_ns_cities_id integer,
        kdtree_dist_ns_cities_id double,
        nearest_iata_code text,
        type text,
        geo_class text,
        name text,
        name_full text,
        ascii_name text,
        country_code text,
        latitude double,
        longitude double,
        time_zone text,
        iata_code text,
        icao_code text,
        has_polygon boolean,
        last_update_utc text,
        validated_by text,
        user_service text,
        status integer
        """
        count_insert_ok = 0
        count_insert_fail = 0
        self.conexion = self.getConect()
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                id = data[0]
                id = int(id)
                altern_id = data[1]
                nearest_ns_cities_id = data[2]
                nearest_ns_cities_id = int(nearest_ns_cities_id)
                kdtree_dist_ns_cities_id = data[3]
                kdtree_dist_ns_cities_id = float(kdtree_dist_ns_cities_id)
                nearest_iata_code = data[4]
                type_t = data[5]
                geo_class = data[6]
                name = data[7]
                name_full = data[8]
                ascii_name = data[9]
                country_code = data[10]
                latitude = data[11]
                latitude = float(latitude)
                longitude = data[12]
                longitude = float(longitude)
                time_zone = data[13]
                iata_code = data[14]
                icao_code =  data[15]
                has_polygon = data[16]
                if has_polygon == "true":
                    has_polygon = True
                else:
                    has_polygon = False
                last_update_utc = data[17]
                validated_by = data[18]
                user_service = data[19]
                status = data[20]
                status = int(status)
                self.conexion.execute("insert into geo_geography (id,altern_id,nearest_ns_cities_id,kdtree_dist_ns_cities_id,nearest_iata_code,type,geo_class,name,name_full,ascii_name,country_code,latitude,longitude,time_zone,iata_code,icao_code,has_polygon,last_update_utc,validated_by,user_service,status) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (id,altern_id,nearest_ns_cities_id,kdtree_dist_ns_cities_id,nearest_iata_code,type_t,geo_class,name,name_full,ascii_name,country_code,latitude,longitude,time_zone,iata_code,icao_code,has_polygon,last_update_utc,validated_by,user_service,status))
                count_insert_ok = count_insert_ok + 1
            except:
                count_insert_fail = count_insert_fail + 1
                #print("Error>>", i)
        print("Total registros insertados: ", str(count_insert_ok))
        print("Total registros con errores de insersiion: ", str(count_insert_fail))
        self.conexion.commit()
        self.conexion.close()


    def insertinfoGeoLatitudeLongitude(self, txt):
        """
        geo_latitude_longitude(
            id integer,
            latitude double,
            longitude double
        )
        """
        count_insert_ok = 0
        count_insert_fail = 0
        self.conexion = self.getConect()
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                id = data[0]
                id = int(id)
                latitude = data[1]
                latitude = float(latitude)
                longitude = data[2]
                longitude = float(longitude)

                self.conexion.execute("insert into geo_latitude_longitude (id,latitude,longitude) values(?,?,?)",(id,latitude,longitude))
                count_insert_ok = count_insert_ok + 1
            except:
                count_insert_fail = count_insert_fail + 1

        print("Total registros insertados: ", str(count_insert_ok))
        print("Total registros con errores de insersiion: ", str(count_insert_fail))
        self.conexion.commit()
        self.conexion.close()

    def insertinfoGeoPolygonShape(self, txt):
        """
            create table if not exists geo_polygon_shape(
                polygon_id integer,
                latlng_id integer,
                point_order integer
            )
        )
        """
        count_insert_ok = 0
        count_insert_fail = 0
        self.conexion = self.getConect()
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                polygon_id = data[0]
                polygon_id = int(polygon_id)
                latlng_id = data[1]
                latlng_id = int(latlng_id)
                point_order = data[2]
                point_order = int(point_order)
                

                self.conexion.execute("insert into geo_polygon_shape (polygon_id,latlng_id,point_order) values (?,?,?)",(polygon_id,latlng_id,point_order))
                count_insert_ok = count_insert_ok + 1
            except:
                count_insert_fail = count_insert_fail + 1

        print("Total registros insertados: ", str(count_insert_ok))
        print("Total registros con errores de insersiion: ", str(count_insert_fail))
        self.conexion.commit()
        self.conexion.close()

    def insertinfoGeoPolygon(self, txt):
        """
            create table if not exists geo_polygon(
                id integer,
                geo_id integer,
                type text
            )
        """
        count_insert_ok = 0
        count_insert_fail = 0
        self.conexion = self.getConect()
        for i in txt.split("\n")[1:-1]:
            try:
                data = i.split("|")
                id = data[0]
                id = int(id)
                geo_id = data[1]
                geo_id = int(geo_id)
                type_t = data[2] 
                

                self.conexion.execute("insert into geo_polygon (id,geo_id,type) values (?,?,?)",(id,geo_id,type_t))
                count_insert_ok = count_insert_ok + 1
            except:
                count_insert_fail = count_insert_fail + 1

        print("Total registros insertados: ", str(count_insert_ok))
        print("Total registros con errores de insersiion: ", str(count_insert_fail))
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




    def insertInfoTurismoiMacth(self, macth):
        """
        create table if not exists turismoi_macth(
            id text primary key,
            iso_country text,
            slug_place text,
            lat double,
            lng double,
            nearest_iata_code text,
            kdtree_dist_ns_cities_id double
        )
        """
        try:
            self.conexion = self.getConect()
            id = macth['id']
            iso_country = macth['iso_country']
            slug_place = macth['slug_place']
            lat = float(macth['lat'])
            lng = float(macth['lng'])
            nearest_iata_code = macth['nearest_iata_code']
            kdtree_dist_ns_cities_id = float(macth['kdtree_dist_ns_cities_id'])
            self.conexion.execute("insert into turismoi_macth (id,iso_country,slug_place,lat,lng,nearest_iata_code,kdtree_dist_ns_cities_id) values (?,?,?,?,?,?,?)", (id,iso_country,slug_place,lat,lng,nearest_iata_code,kdtree_dist_ns_cities_id))
            self.conexion.commit()
            self.conexion.close()
            #print("Metido en Database", id)
        except:
            print("Error ingresando: ")
            print(macth)





    def deleteTurismoiMacthReg(self, id):
        try:
            con = self.getConect()
            cur = con.cursor()
            sql = "DELETE FROM turismoi_macth WHERE id=?"
            cur.execute(sql, (id,))
            con.commit()
        except:
            print("Error tratando de deletear: ", str(id))



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


    def getAllMacthTurismoiInfoToCSV(self):
        """
        create table if not exists turismoi_macth(
            0 id text primary key,
            1 iso_country text,
            2 slug_place text,
            3 lat double,
            4 lng double,
            5 nearest_iata_code text,
            6 kdtree_dist_ns_cities_id double
        )
        """
        txt = ""
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from turismoi_macth")
            fila=cursor.fetchall()
            for i in fila:
                txt = txt + i[0] + "|" + i[1] + "|" + i[2] + "|" + str(i[3]) + "|" + str(i[4]) + "|" + i[5] + "|" + str(i[6]) + "|" "\n"

            cursor.close()
        except:
            pass
        return txt

    def insertInfoTarget(self, info):
        """
        create table if not exists target(
            id text primary key,
            code text,
            iso_country text,
            name_place text,
            latitude double,
            longitude double
        )
        """
        try:
            id = info[0]
            code = info[1]
            iso_country = info[2]
            name_place = info[3] 
            latitude = float(info[4])
            longitude = float(info[5])
            self.conexion = self.getConect()
            self.conexion.execute("insert into target (id,code,iso_country,name_place,latitude,longitude) values (?,?,?,?,?,?)",(id,code,iso_country,name_place,latitude,longitude))
            self.conexion.commit()
            self.conexion.close()
        except:
            print("Error Insert:")
            print(info)

    def getAllTargetInfo(self):
        """
        create table if not exists target(
            id text primary key,
            code text,
            iso_country text,
            name_place text,
            latitude double,
            longitude double
        )
        """
        total = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from target")
            fila=cursor.fetchall()
            for i in fila:
                id = i[0]
                code = i[0]
                iso_country = i[0]
                name_place = i[0]
                latitude = i[0]
                longitude = i[0]
                json = {"id":id,"code":code,"iso_country":iso_country,"name_place":name_place,"latitude":latitude,"longitude":longitude}
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










    def updateGEOLatLngInTurismoi(self, key, latitude, longitude):
        try:
            conexion = self.getConect()
            cursor = conexion.cursor()
            sql = "update turismoi_geo_add set latitude = " + str(latitude) + ", longitude = " + str(longitude) + " where id = '" + key + "'"
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            #print("Actualizada...", key)
        except:
            print("Error actualizando turismoi:", key)



    def getAllTurismoiIsoCountriesCodes(self):
        """
        return all exists iso codes in turismoi DB
        """
        iso_codes = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from turismoi")
            fila=cursor.fetchall()
            for i in fila:
                data = str(i[0]).split(":")
                iso = data[0]
                city_name = data[1]
                
                if iso not in iso_codes and city_name != "null":
                    iso_codes.append(iso)
        except:
            pass

        return iso_codes





    def getTurismoiRichInformation(self):
        """
        0 > id
        1 > ISO_country
        12 > slug_place
        16 > latitude
        17 > longitude
        """
        total = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from turismoi where latitude is not null and longitude is not null")
            fila=cursor.fetchall()
            for i in fila:
                id = i[0]
                iso_country = i[2]
                slug_place = i[12]
                lat = i[16]
                lng = i[17]
                json = {"id":id,"iso_country":iso_country,"slug_place":slug_place,"lat":lat,"lng":lng}
                total.append(json)
            cursor.close()
        except:
            print("Error")


        return total

    def getTurismoiGEOatLngViaKEyId(self, id):
        """
        16 > latitude
        17 > longitude
        """
        GEO = "NULL|NULL"
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from turismoi where id = ?", (id,))
            fila=cursor.fetchone()
            latitude = fila[16]
            longitude  = fila[17]
            if latitude == None:
                latitude = "NULL"
            if longitude == None:
                longitude = "NULL"
            GEO = str(latitude) + "|" + str(longitude)
                
            cursor.close()
        except:
            print("Error DB.Turismoi.GEO")

        return GEO

    def getRowTurismoiInfo(self, id):
        data = ""
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from turismoi where id = ?", (id,))
            fila=cursor.fetchone()
            for i in fila[1:]: # [1:] >> NO need a ID becos need exac like a .csv
                row = i
                if row == None:
                    row = "NULL"

                data = data + str(row) + "|"
        except:
            print("Error Buscado turismoi.id ", str(id))


        return data


    def getTargetRichInformation(self):
        """
        0 > id
        2 > ISO_country
        3 > slug_place
        4 > latitude
        5 > longitude
        """
        total = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from target where latitude is not null and longitude is not null")
            fila=cursor.fetchall()
            for i in fila:
                id = i[0]
                iso_country = i[2]
                slug_place = i[3]
                lat = i[4]
                lng = i[5]
                json = {"id":id,"iso_country":iso_country,"slug_place":slug_place,"lat":lat,"lng":lng}
                total.append(json)
            cursor.close()
        except:
            print("Error")
        return total


    def insertInfoTargetMacth(self, macth):
        """
        create table if not exists target_macth(
            id text primary key,
            iso_country text,
            slug_place text,
            lat double,
            lng double,
            nearest_iata_code text,
            kdtree_dist_ns_cities_id double
        )
        """
        try:
            self.conexion = self.getConect()
            id = macth['id']
            iso_country = macth['iso_country']
            slug_place = macth['slug_place']
            lat = float(macth['lat'])
            lng = float(macth['lng'])
            nearest_iata_code = macth['nearest_iata_code']
            kdtree_dist_ns_cities_id = float(macth['kdtree_dist_ns_cities_id'])
            self.conexion.execute("insert into target_macth (id,iso_country,slug_place,lat,lng,nearest_iata_code,kdtree_dist_ns_cities_id) values (?,?,?,?,?,?,?)", (id,iso_country,slug_place,lat,lng,nearest_iata_code,kdtree_dist_ns_cities_id))
            self.conexion.commit()
            self.conexion.close()
            #print("Metido en Database", id)
        except:
            print("Error ingresando: ")
            print(macth)


    def deleteTargetMacthReg(self, id):
        try:
            con = self.getConect()
            cur = con.cursor()
            sql = "DELETE FROM target_macth WHERE id=?"
            cur.execute(sql, (id,))
            con.commit()
        except:
            print("Error tratando de deletear: ", str(id))



    def getAllMacthTargetInfoToCSV(self):
        """
        create table if not exists target_macth(
            0 -> id text primary key,
            1 -> iso_country text,
            2 -> slug_place text,
            3 -> lat double,
            4 -> lng double,
            5 -> nearest_iata_code text,
            6 -> kdtree_dist_ns_cities_id double
        )
        """
        txt = ""
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from target_macth")
            fila=cursor.fetchall()
            for i in fila:
                txt = txt + i[0] + "|" + i[1] + "|" + i[2] + "|" + str(i[3]) + "|" + str(i[4]) + "|" + i[5] + "|" + str(i[6]) + "|" "\n"

            cursor.close()
        except:
            pass
        return txt


    def getAllTargetKeysMatched(self):
        """
        return all exists keys/id target macthed
        """
        keys = []
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.execute("select * from target_macth")
            fila=cursor.fetchall()
            for i in fila:
                data = str(i[0])
                keys.append(data)
                
        except:
            pass

        return keys



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


    def deleteAllFromTurismoi(self):
        try:
            self.conexion = self.getConect()
            cursor = self.conexion.cursor()
            sql = """
            delete from turismoi
            """
            cursor.execute(sql)
            self.conexion.commit()
            cursor.close()
        except:
            print("Error Borrando DB.turismoi")


    def insertInfoInTurismoiGeoADD(self, data):
        """
        create table if not exists turismoi_geo_add(
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
            self.conexion.execute("insert into turismoi_geo_add (id,ID_country,ISO_country,NAME_country,NAME_PRINT_country,ISO3_country,CODE_country,NAME_ESP_country,id_city,region_id,name_place,short_name_place,slug_place,group_id_place,province_id_place,group_slug_place,latitude,longitude,country_host_id_place) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id,ID_country,ISO_country,NAME_country,NAME_PRINT_country,ISO3_country,CODE_country,NAME_ESP_country,id_city,region_id,name_place,short_name_place,slug_place,group_id_place,province_id_place,group_slug_place,latitude,longitude,country_host_id_place))
            self.conexion.commit()
            self.conexion.close()
            self.metadata[str(self.counter)] = "Insert info in turismoi_geo_add:" + str(data[0])
        except:
            self.metadata[str(self.counter)] = "Error in info in turismoi_geo_add:" + str(data[0])
        self.counter = self.counter + 1


    def getAllTurismoiGeoADDInfo(self):
        """
        create table if not exists turismoi_geo_add(
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
            cursor = self.conexion.execute("select * from turismoi_geo_add")
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


