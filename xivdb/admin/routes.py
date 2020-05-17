from flask import Flask, render_template, Blueprint
from typing import List, Dict
from sqlalchemy.orm import sessionmaker, Session, Query
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
#from xivdb.src.admin import AdminTasks
from XivDbReader import Reader
from json import dumps

d = DB(Base)
session: Session = d.newSession()
admin_bp = Blueprint('admin', __name__ 
    ,template_folder="templates")

@admin_bp.route('/')
def index() -> None:
    return render_template('admin/adminIndex.html')

