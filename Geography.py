"""
felipedelosH

Controller all relationate with:

 * Globla geography
 * Kdtree resources

"""
from Database import *

class Geografy:
    def __init__(self) -> None:
        self.database = Database()
        self.metadata = {}

    def insertInfoCities(self, txt):
        """
        Insert info: RESOURCES/Cities.csv
        """
        self.database.insertInfoCities(txt)
        self.metadata = self.database.metadata
        