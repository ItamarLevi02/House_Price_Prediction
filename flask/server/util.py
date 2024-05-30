import json, pickle
import numpy as np

__cities = None
__data_columns = None
__model = None

def get_estimated_price(city,bedroom,bath,acre_lot,zip_code,sqft):
    try:
        city_index = __data_columns.index(city.lower())
    except:
        city_index = -1
    
    
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
    
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __cities = __data_columns[4:]
        
    global __model
    with open('./artifacts/Bay_Area_House_Price_Prediction_Model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("loaded")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_cities_names())
    print(get_estimated_price('Alameda',2,2,.12,94501,1288.0))
