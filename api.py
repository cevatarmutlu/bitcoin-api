from flask import Flask, jsonify, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.api.query import Query

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sade123@localhost:5432/postgres'
db = SQLAlchemy(app)
query = Query(db)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/', methods=['GET'])
def root():
  return jsonify({
    '/values': '5dklik degerlerinin Json olarak sunulmasi',
    '/avg': 'ortalama degerinin sunulmasi',
    '/all': 'Bitcoin degerlerinin hepsini return eder.'
  })

@app.route('/values', methods=['GET'])
def fiveMinutes():
  symbol = request.args.get("symbol", "ETHBTC")
  time =  request.args.get("time", 15)
  return jsonify(query.coin_values(symbol=symbol, time=time))

@app.route('/avg', methods=['GET'])
def oneHour():
  symbol = request.args.get("symbol", "ETHBTC")
  time =  request.args.get("time", 1)
  return jsonify(query.coin_avg(symbol=symbol, time=time))

@app.route('/all', methods=['GET'])
def all_data():
  return jsonify(query.all_coin_values())


if __name__ == '__main__':
    app.run(debug=DEBUG)