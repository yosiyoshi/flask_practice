# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:16:15 2018

@author: YosiYoshi
"""
#curl -i -H "Content-Type: application/json" -d "{\"id\":\"a\",\"password\": \"a\"}" http://localhost:5000/data

from flask import Flask, render_template, jsonify, request
import json
import re
import subprocess
import webbrowser

app = Flask(__name__)

data = []

@app.route('/')
def form():
   return render_template('login.html')

@app.route('/data', methods=['POST'])
def add_data():
  data.append(request.get_json())
  return '', 204

@app.route('/auth', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      getkey = request.form['key']
      getvalue = request.form['value']
      authkey = "id:"+getkey+",password:"+getvalue
      jsdump = json.dumps(data)
      key = re.sub(r'["{[/ \]}"]', "", jsdump)
      if key == authkey:
         auth_res = "Login successful"
         subprocess.call(['python', 'lang_json.py'])
         url = "http://localhost:5000/"
         webbrowser.open(url)
      else:
         auth_res = "Login failed"
      return "Result: {}".format(auth_res)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
