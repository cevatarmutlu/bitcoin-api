from flask import Flask, jsonify, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.server.query import Query
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
    '/avg': 'ortalama degerinin sunulmasi'
  })

@app.route('/values', methods=['GET'])
def fiveMinutes():
  return jsonify(query.coin_values())

@app.route('/avg', methods=['GET'])
def oneHour():
  return jsonify(query.coin_avg())


if __name__ == '__main__':
    app.run(debug=DEBUG)