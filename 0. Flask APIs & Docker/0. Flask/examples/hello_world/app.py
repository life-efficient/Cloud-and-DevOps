from flask import Flask
import json

APP_NAME = 'my_api'
APP_HOST = '0.0.0.0'
APP_PORT = 5000

app = Flask(APP_NAME)

@app.route('/') # defines the function which is the response is returned from at / route 
def home():
    return 'hello world'

@app.route('/home') # defines the function which is the response is returned from at /home route 
def home():
    return '<html><h1>yo</h1><p>hi</p></html>'

@app.route('/with_status_code') # requests to localhost:5000/with_status_code call this function
def root():
    return json.dumps({
        'statusCode': 200,
        'body': 'yo'
    })

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)