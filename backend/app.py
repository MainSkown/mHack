from flask import Flask, request, jsonify
from api_translation import ApiTranslation
from sqlite_connector import SQLiteConnector
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/search', methods=['GET', 'POST'])

def search():

    search = ApiTranslation()
    request_data = request.get_json()
    search.get_request(request_data)
    search.constructing_filters()
    search.generating_api_command()

    return search.getting_json()

@app.route('/user/registered', methods=['POST'])

def users_registrations():

    request_data = request.get_json()
    print(request_data)
    user_database_conn = SQLiteConnector()
    
    return user_database_conn.get_queues(request_data['user_id'])

if __name__ == '__main__':  
    app.run()
