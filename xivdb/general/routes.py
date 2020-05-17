from flask import render_template, Blueprint
#from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from typing import List
from sqlalchemy.orm import sessionmaker, Session, Query

general_bp = Blueprint('general', __name__
    ,template_folder='templates')

@general_bp.route('/')
def index():
    return render_template('general/index.html')

@general_bp.route('/about')
def about():
    return render_template('general/about.html')