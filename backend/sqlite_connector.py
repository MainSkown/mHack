import sqlite3
import os
db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'databases', 'mLekarz.db'))


class SQLiteConnector:

    def __init__(self):

        self.con = sqlite3.connect(db_file_path)
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
                'location': {
                    'city': row[2],
                    'street': row[3],
                },
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

    def add_queue(self, queue_id, user_id, place_name, location, visit_date, visit_name, phone):
        city = location["city"]
        street = location["street"]

        sql_location_exists = f'SELECT * FROM locations WHERE place_name = "{place_name}"'
        location_exists = len(self.cur.execute(sql_location_exists).fetchall())
        if not location_exists:
            self.add_location(place_name, city, street)

        sql_queues = f"INSERT INTO queues VALUES ('{queue_id}', '{user_id}', '{place_name}', '{visit_date}',\
                                                                                    '{visit_name}', '{phone}')"
        self.cur.execute(sql_queues)
        self.con.commit()

        return {'status': 201, 'message': 'Registered Successfully'}


# tests
# connector = SQLiteConnector().get_queues('696969669')
# print(connector['queues'])
#
# connector = SQLiteConnector().get_queues('nie_istnieje')
# print(connector)

# connector = SQLiteConnector().get_queues('2137')
# print(connector)

# insert_test = SQLiteConnector().add_location('test_place_2', 'Testowo', 'Działa 78')
# print(insert_test)

# queue_insert_test = (SQLiteConnector()
#                      .add_queue('test_wizyta', '696969669',
#                                 {'place_name': 'test_place_3', 'city': 'Test', 'street': 'Malinowa 12'},
#                                 '2023-03-23', 'Porada', '696-696-696'))
# print(queue_insert_test)
