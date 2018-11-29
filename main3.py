# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:48:34 2018

@author: yosiyoshi
"""
from flask import Flask, request, render_template
import jieba

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}　\r\n Result: {}'.format(request.form['text'], "/ ".join(jieba.cut(request.form['text'], cut_all=False)))

if __name__ == '__main__':
    app.run(host='localhost',debug=True)