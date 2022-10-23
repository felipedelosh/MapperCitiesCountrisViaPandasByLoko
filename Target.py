"""
FelipedelosH

This is another project/class/DB to MACTH with turismoi


create table if not exists target(
    id text primary key,
    code text,
    iso_country text,
    name_place text,
    latitude double,
    longitude double
)

"""
class Target_to_macth():
    def __init__(self) -> None:
        self.data = {} # iso_code+:+city_name = all info
        self.metadata = {}
        self.count = 0
        self.duplicated_control = 0
        self.delimiter = ""
        self.id_position = 0
        self.code_position = 0
        self.name_place_position = 0
        self.latitude_position = 0
        self.longitude_position = 0
        

    def loadData(self, txt):
        for i in txt.split("\n")[1:-1]:
            data = i.split(self.delimiter)
            if str(data[1]).lower().__contains__('no usar'):
                self.metadata["Test_register:"+str(self.count)] = str(data)
                self.count = self.count + 1
            else:
                id_country = data[self.id_position]
                NAME_country = str(id_country).split("(")[0]
                NAME_country = NAME_country.lstrip().rstrip()
                iso_country = str(id_country).split("(")[-1]
                iso_country = iso_country.replace(')', '')
                iso_country = iso_country.strip().lower()

                name_city = str(data[1]).lstrip().rstrip().lower()
                name_city = name_city.replace('-', ' ')
                name_city = name_city.replace(',', '')
                name_city = name_city.replace('\'', '')
                name_city = name_city.replace("(state)", '')

                key = iso_country + ":" + name_city

                if key in self.data.keys():
                    key = key + "-" + str(self.duplicated_control)
                    self.duplicated_control = self.duplicated_control + 1

                # Save a Data in RAM
                self.data[key] = i

        self.metadata["Total_Reg_Inserted"] = str(len(self.data))
        self.metadata["Counter_not_used"] = str(self.count)
        self.metadata["Counter_duplicated_fix"] = str(self.duplicated_control)

                
