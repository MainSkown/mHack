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
        
        sql = (f'SELECT queue_id, locations.place_name, specialist, locations.city, locations.street,\
                    registration_date, visit_date, visit_name, phone\
                    FROM queues LEFT JOIN locations on locations.place_name = queues.place_name\
                    WHERE user_id="{user_id}"')
        res = self.con.execute(sql)
        
        visits = []

        for row in res:
            visits.append({
                'queue_id': row[0],
                'place_name': row[1],
                'specialist': row[2],
                'location': {
                    'city': row[3],
                    'street': row[4],
                },
                'registration_date': row[5],
                'visit_date': row[6],
                'visit_name': row[7],
                'phone': row[8]
            })

        return {'queues': visits}, 200

    def add_location(self, place_name, city, street):
        sql = f"INSERT INTO locations VALUES ('{place_name}', '{city}', '{street}')"
        self.cur.execute(sql)
        self.con.commit()
        return {'message': 'Added location successfully'}, 201

    def add_queue(self, queue_id, user_id, place_name, specialist, location,
                  registration_date, visit_date, visit_name, phone):
        sql_queue_id_check = f'SELECT * FROM queues WHERE queue_id="{queue_id}"'
        queue_id_exists = len(self.con.execute(sql_queue_id_check).fetchall())
        if queue_id_exists:
            return {'message': 'Conflict - visit with this queue_id already exists', 'test': queue_id_exists}, 409

        city = location["city"]
        street = location["street"]

        sql_location_exists = f'SELECT * FROM locations WHERE place_name = "{place_name}"'
        location_exists = len(self.cur.execute(sql_location_exists).fetchall())
        if not location_exists:
            self.add_location(place_name, city, street)

        sql_queues = f"INSERT INTO queues \
        (queue_id, user_id, place_name, specialist, registration_date, visit_date, visit_name, phone) \
        VALUES ('{queue_id}', '{user_id}', '{place_name}', '{specialist}', '{registration_date}', '{visit_date}',\
                                                                            '{visit_name}', '{phone}')"
        self.cur.execute(sql_queues)
        self.con.commit()

        return {'message': 'Registered Successfully'}, 201

    def remove_queue(self, queue_id, user_id):
        sql = f'DELETE FROM queues WHERE queue_id="{queue_id}" AND user_id="{user_id}"'
        self.cur.execute(sql)
        self.con.commit()
        return {'message': 'No content'}, 204


# tests
# ***** ***
# connector = SQLiteConnector().get_queues('696969669')
# print(connector)
#
# connector = SQLiteConnector().get_queues('nie_istnieje')
# print(connector)

# connector = SQLiteConnector().get_queues('2137')
# print(connector)

# insert_test = SQLiteConnector().add_location('test_place_2', 'Testowo', 'Działa 78')
# print(insert_test)
#
# queue_insert_test = (SQLiteConnector()
#                      .add_queue('wizyta_z_registration_date_test_2', '696969669', 'test_place_3',
#                                 {'city': 'Test', 'street': 'Malinowa 12'},
#                                 '2023-03-23', '2023-12-01', 'Porada', '696-696-696'))
# print(queue_insert_test)
