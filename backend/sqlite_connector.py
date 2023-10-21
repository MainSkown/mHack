import sqlite3


class SQLiteConnector:
    def __init__(self):
        self.con = sqlite3.connect('databases/mLekarz.db')
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

