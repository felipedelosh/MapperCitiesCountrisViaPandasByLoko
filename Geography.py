"""
felipedelosH

Controller all relationate with:

 * Globla geography
 * Kdtree resources

"""
from Database import *

class Geografy:
    def __init__(self) -> None:
        self.data = {}
        self.database = Database()
        self.metadata = {}

    def insertInfoCities(self, txt):
        """
        Insert info: RESOURCES/Cities.csv
        """
        self.database.insertInfoCities(txt)
        self.metadata = self.database.metadata

    def insertInfoCountries(self, txt):
        """
        RESOURCES/Countries.csv
        """
        self.database.inserInfoCopuntries(txt)
        self.metadata = self.database.metadata
        