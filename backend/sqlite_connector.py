import sqlite3


class SQLiteConnector:
    def __init__(self):
        self.con = sqlite3.connect('databases/mLekarz.db')
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def get_queues(self, user_id):
        sql = (f'SELECT queue_id, locations.place_name, locations.city, locations.street, visit_date, visit_name, phone\
                    FROM queues LEFT JOIN locations on locations.place_name = queues.place_name\
                    WHERE user_id = "{user_id}"')

        res = self.con.execute(sql)
        visits = []

        for row in res:
            visits.append({
                'queue_id': row[0],
                'place_name': row[1],
                'city': row[2],
                'street': row[3],
                'visit_date': row[4],
                'visit_name': row[5],
                'phone': row[6]
            })

        return {'status': 200, 'queues': visits}
