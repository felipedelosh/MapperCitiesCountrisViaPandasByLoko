"""
FelipedelosH

This class save and get all project info into: dbTest.db

"""
import sqlite3

class Database:
    def __init__(self) -> None:
        self.conexion = self.getConect()

    def getConect(self):
        return sqlite3.connect("DBtest.db")

    def initDatabase(self):
        pass