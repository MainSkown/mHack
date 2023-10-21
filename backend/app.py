from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/test', methods=['POST'])

def test():
    request_data = request.get_json()
    print(request_data)
    return "test"

if __name__ == '__main__':
    app.run()
