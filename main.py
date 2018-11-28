# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:05:30 2018

@author: user
"""
from flask import Flask, request, render_template
from ynltk import Langvowel

app = Flask(__name__)
l = Langvowel()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}　\r\n Recognized language: {}'.format(request.form['text'], l.langvowel(request.form['text']))

if __name__ == '__main__':
    app.run(host='localhost',debug=True)