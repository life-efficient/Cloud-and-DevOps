from flask import Flask, request
import json
# from MLModel import Model

# model = Model()

app = Flask(__name__)


@app.route('/home')
def home():
    return '<html><h1>yo</h1><p>hi</p></html>'


@app.route('/')
def root():
    return json.dumps({
        'statusCode': 200,
        'body': 'yo'
    })

@app.route('/predict', methods=['POST'])
def predict():
    x = request.get_json()['input']

    return json.dumps({
        'statusCode': 200,
        'body': model.predict(x)
    })
    # try:
    # except:
    #     return json.dumps({
    #         'statusCode': 500,
    #         'message': 'Internal server error'
    #     })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)