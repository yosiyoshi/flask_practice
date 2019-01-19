# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 08:37:47 2019

@author: Yosiyoshi
"""
import sqlite3
from flask import Flask, jsonify, request
from ynltk import Langvowel
import datetime
import json

dbpath='sample_db.sqlite'
connection=sqlite3.connect(dbpath)
cursor=connection.cursor()

#try:
cursor.execute("DROP TABLE IF EXISTS sample")
cursor.execute("CREATE TABLE IF NOT EXISTS sample (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO sample VALUES (1,'Alpha')")
cursor.execute("INSERT INTO sample VALUES (2,'Bravo')")
cursor.execute("INSERT INTO sample VALUES (3,'Charlie')")
cursor.execute("INSERT INTO sample VALUES (4,'Alpha \n Bravo \n Charlie')")
connection.commit()

cursor.execute('SELECT * FROM sample ORDER BY id')
res = cursor.fetchall()
print(res)
connection.close()

app = Flask(__name__)
restr= '\n'.join(map(str, res))

@app.route('/')
def index():
    l=Langvowel()
    return 'Date: {} \n JSON: {}　\n Length: {} \n Character: {} \n Language: {}'.format(
            datetime.datetime.now(), restr, str(len(res)), str(len(str(jsonify(res)))), 
            l.langvowel(str(res)))

@app.route('/date')
def date():
    return str(datetime.datetime.now())

@app.route('/json')
def json():
    return restr

@app.route('/len')
def length():
    return str(len(res))

@app.route('/character')
def chara():
    jsonres=str(jsonify(res))
    return str(len(jsonres))

@app.route('/lang')
def detec_lang():
    l=Langvowel()
    return l.langvowel(str(res))

if __name__ == '__main__':
    app.run(host='localhost',debug=True)