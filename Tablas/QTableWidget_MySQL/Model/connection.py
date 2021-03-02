import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234567890",
        database = "Personas"
        )
        self.cursor = self.connection.cursor()
    
    def getData(self):
        self.cursor.execute("SELECT *FROM Persona")
        data = self.cursor.fetchall()
        return data