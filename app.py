import numpy as np
import os
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify, render_template, request, redirect
# import get_data

import psycopg2

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app._static_folder = 'static/'

##################################

# # Connects to the database using the app config
db = SQLAlchemy(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():

    # return render_template("index.html")
    return "sadgfd"

@app.route("/about.html")
def team():

    return render_template("docs/index.html")

    
if __name__ == '__main__':
    app.run(debug=True)
