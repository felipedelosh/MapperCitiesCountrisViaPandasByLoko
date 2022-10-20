"""
FelipedelosH



"""
import os
from os import scandir

class Controller:
    def __init__(self) -> None:
        print("Gretting from Controller")
        pass

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