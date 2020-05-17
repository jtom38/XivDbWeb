from flask import Flask, render_template, Blueprint
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from typing import List
from sqlalchemy.orm import sessionmaker, Session, Query
import json

from xivdb.src.jobs.dbInit import DbInit

apiJobs_bp = Blueprint('apiJobs', __name__)

d = DB(Base)

@apiJobs_bp.route('/dbinit',methods=['POST'])
def initDb():
    db = DbInit()
    db.runJob()
