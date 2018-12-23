# e.g.: curl -i -H "Content-Type: application/json" -d "{\"amount\":5000.0,\"description\":\"salary\"}" http://localhost:5000/data
from flask import Flask, jsonify, request
from ynltk import Langvowel

app = Flask(__name__)
l = Langvowel()

data = []

@app.route('/data')
def get_data():
  return jsonify(data)

@app.route('/lang')
def detec_lang():
  return l.langvowel(str(data))

@app.route('/data', methods=['POST'])
def add_data():
  data.append(request.get_json())
  return '', 204

if __name__ == '__main__':
    app.run(host='localhost',debug=True)