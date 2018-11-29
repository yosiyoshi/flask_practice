# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:16:15 2018

@author: YosiYoshi
"""
import re
from flask import Flask, render_template, request
from ynltk import OmnibusStem
app = Flask(__name__)

@app.route('/')
def form():
   return render_template('form2.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      for key, value in result.items():
          txt1 = re.sub(' ', '', key)
          txt2 = re.sub(' ', '', value)
      s=OmnibusStem()
      result2 = s.compStemmer(txt1.lower(),txt2.lower())
      return 'Result: {}'.format(result2)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
