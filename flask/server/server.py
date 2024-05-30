from flask import Flask, request, jsonify
import util


app = Flask(__name__)

@app.route('/get_cities_names')
def get_cities_names():

    response = jsonify({
        'citiess': util.get_cities_names()
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
        'estimate_price': util.get_estimated_price(city,bedroom,bath,acre_lot,zip_code,sqft)
    })
    return response

if __name__ == '__main__':
    print('Server Starting...')
    app.run()