# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:16:15 2018

@author: YosiYoshi
"""
from flask import Flask, render_template, request
from ynltk import OmnibusStem
app = Flask(__name__)

@app.route('/')
def form():
   return render_template('form2.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      getkey = request.form['key']
      getvalue = request.form['value']
      s=OmnibusStem()
      input1 = getkey.replace(" ", "")
      input2 = getvalue.replace(" ", "")
      result2 = s.compStemmer(input1.lower(),input2.lower())
      return 'Result: {}'.format(result2)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
