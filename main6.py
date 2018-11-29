# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:48:34 2018

@author: yosiyoshi
"""
from flask import Flask, request, render_template
import tltk.nlp as tl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}　\r\n Result: {}'.format(request.form['text'], tl.pos_tag(request.form['text'],))

if __name__ == '__main__':
    app.run(host='localhost',debug=True)