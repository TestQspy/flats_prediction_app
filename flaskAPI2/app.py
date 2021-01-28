import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle


def load_models():
    file_name = "models/models_file.pickle"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data.get('model_multi_rfr_wppm')
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    request_json = request.get_json()
    x = request_json['input']
    x_in = np.array(x).reshape(1, -1)
    # print(x)
    # load model
    model = load_models()
    # print(model)
    prediction = model.predict(x_in)[0].round(decimals=2)
    print(prediction)
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)
