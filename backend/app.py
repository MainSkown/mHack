from flask import Flask, request
from api_translation import ApiTranslation
from sqlite_connector import SQLiteConnector
from flask_cors import CORS
from geo_location import GeoLocation

app = Flask(__name__)

cors = CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!', 200


@app.route('/search', methods=['GET', 'POST'])
def search():

    radius_search = GeoLocation()
    cities = radius_search.collect_data(radius_search.db_file_path)


    
    request_data = request.get_json()
    nearby_cities = radius_search.find_nearby_cities(request_data['locality'].lower(), 30, cities)

    search = ApiTranslation()
    search.get_request(request_data)

    search.constructing_filters()
    search.generating_api_command()
    full_dataset = search.getting_json()

    if nearby_cities:

        for city in nearby_cities:

            request_data['locality'] = city
            search.get_request(request_data)
            search.constructing_filters()
            search.generating_api_command()
            full_dataset += search.getting_json()
    

    return full_dataset


@app.route('/user/registered', methods=['POST'])
def users_registrations():
    request_data = request.get_json()
    user_database_conn = SQLiteConnector()

    try:
        res = user_database_conn.get_queues(request_data['user_id'])
        return res
    except:
        return {'message': 'Conflict'}, 409


@app.route('/user/register', methods=['POST'])
def user_register():
    save_request_data = request.get_json()
    user_database_conn = SQLiteConnector()
    try:

        status = user_database_conn.add_queue(save_request_data['queue_id'], save_request_data['user_id'],
                                              save_request_data['place_name'], save_request_data['specialist'],
                                              save_request_data['location'],
                                              save_request_data['registration_date'], save_request_data['visit_date'],
                                              save_request_data['visit_name'], save_request_data['phone'])
    except:
        return {'message': 'Conflict - visit with this queue_id already exists'}, 409

    return status


@app.route('/user/delete', methods=['PUT'])
def delete_visit():
    save_request_data = request.get_json()
    user_database_conn = SQLiteConnector()
    try:
        queue_id = save_request_data['queue_id']
        user_id = save_request_data['user_id']

        status = user_database_conn.remove_queue(queue_id, user_id)
        return status
    except:
        return {'message': 'Conflict'}, 409


if __name__ == '__main__':
    app.run()
