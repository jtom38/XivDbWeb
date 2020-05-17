
import flask
from flask import Flask, render_template, Blueprint, redirect, url_for, session, request
import os

from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from typing import List
from sqlalchemy.orm import sessionmaker, Session, Query

#from .admin import routes as admin_bp
#from .weapons import routes as weapon_routes

def create_app(test_config=None):
    app:Flask = Flask(__name__ 
        ,static_folder="static"
        ,template_folder="templates"
        ,instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        # load the config if it was passed in
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #d = DB(Base)
    #session: Session = d.newSession()

    @app.route('/')
    def hello():
        #return "Hello World"
        return render_template("index.html", page_name='cookie')

    return app
