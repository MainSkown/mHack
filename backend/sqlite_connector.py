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

    def add_location(self, place_name, city, street):
        sql = f"INSERT INTO locations VALUES ('{place_name}', '{city}', '{street}')"
        self.cur.execute(sql)
        self.con.commit()
        return {'status': 201, 'message': 'Added location successfully'}

    def add_queue(self, queue_id, user_id, location, visit_date, visit_name, phone):
        place_name = location["place_name"]
        city = location["city"]
        street = location["street"]

        sql_location_exists = f'SELECT * FROM locations WHERE place_name = "{place_name}"'
        location_exists = len(self.cur.execute(sql_location_exists).fetchall())
        if not location_exists:
            self.add_location(place_name, city, street)

        sql_queues = f"INSERT INTO queues VALUES ('{user_id}', '{queue_id}', '{place_name}', '{visit_date}',\
                                                                                    '{visit_name}', '{phone}')"
        self.cur.execute(sql_queues)
        self.con.commit()

        return {'status': 201, 'message': 'Registered Successfully'}