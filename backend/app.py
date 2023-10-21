from flask import Flask, request, jsonify
from api_translation import ApiTranslation

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/search', methods=['GET'])

def search():

    search = ApiTranslation()
    request_data = request.get_json()
    search.get_request(request_data)
    search.constructing_filters()
    search.generating_api_command()

    return search.getting_json()

if __name__ == '__main__':  
    app.run()
