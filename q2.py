# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:07:37 2022

@author: Hafiz Admin
"""

import pandas as pd
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# read some data
df = pd.read_csv('Election-Results-2018 - Parlimen_Results_By_Candidate.csv')

@app.route('/',methods=['GET'])
def home():
    links = "<h1>Election Result</h1>"
    links += '<a href="https://hfzdnnzl.shinyapps.io/election_2018_dashboard/">Results Dashboard</a><br>'
    links += '<a href="seat">Results by Seat</a><br>'
    return links

@app.route('/seat/all', methods=['GET'])
def api_all():
    return jsonify(df.to_dict())

@app.route('/seat', methods=['GET'])
def api_each():
    if 'id' in request.args:
        id = 'P.'+request.args['id']
    else:
        links = '<h1>Election Results by Seat</h1><br>'
        links += '<a href="/..">BACK</a><br>'
        links += '<a href="seat/all">ALL</a><br><br>'
        for seat in df['Seat ID'].unique():
            link = '<a href="seat?id='+seat.replace('P.','')+'">'+seat+'</a><br>'
            links += link
        return links
    return jsonify(df[df['Seat ID']==id].to_dict())

app.run()