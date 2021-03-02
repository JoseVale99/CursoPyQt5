import  sqlite3

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("Model/db.db")
        self.cursor = self.connection.cursor()
    
    def getData(self):
        self.cursor.execute("SELECT *FROM personas")
        data = self.cursor.fetchall()
        return data