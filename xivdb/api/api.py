from flask import Flask, render_template, Blueprint
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from typing import List
from sqlalchemy.orm import sessionmaker, Session, Query
import json

d = DB(Base)
#session: Session = d.newSession()
api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def apiHello():
    res = {"msg": "Hello World"}
    return json.dumps(res)

