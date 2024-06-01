from flask import Flask, request, jsonify
from flask_cors import CORS 
import json, pickle
import numpy as np


__cities = None
__data_columns = None
__model = None


app = Flask(__name__)
CORS(app) 


@app.route('/')
def Home():
    return "Hello"

@app.route('/get_cities')
def get_cities_names():

    response = jsonify({
        'cities': get_cities_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    city = request.form['city']
    bedroom = float(request.form['bedroom'])
    bath = float(request.form['bath'])
    acre_lot =  float(request.form['acre_lot'])
    zip_code =  float(request.form['zip_code'])
    sqft = float(request.form['sqft'])

    response = jsonify({
        'estimate_price': get_estimated_price(city,bedroom,bath,acre_lot,zip_code,sqft)
    })
    return response


def get_estimated_price(city,bedroom,bath,acre_lot,zip_code,sqft):
    try: 
        city_index = __data_columns.index(city.lower())
    except:
        city_index = -1
    
    print(type(__data_columns))
    x = np.zeros(len(__data_columns))
    
    x[0] = bedroom
    x[1] = bath
    x[2] = acre_lot 
    x[3] = zip_code
    x[4] = sqft
    
    if city_index >= 0:
        x[city_index] = 1
    return round(__model.predict([x])[0],2)

def get_cities_names():
    return __cities

def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns
    global __cities
    
    with open("./columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __cities = __data_columns[5:]
        
    global __model
    with open('./Bay_Area_House_Price_Prediction_Model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("loaded")


if __name__ == '__main__':
    print('Server Starting...')
    load_saved_artifacts()
    app.run()
    

    