import mysql.connector as ms

class DBconnect:
    def __init__(self):
        self.con=ms.connect(host="localhost", user="root", password="SOFTwarica1@", database="pani")
        self.cur=self.con.cursor()

    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()
