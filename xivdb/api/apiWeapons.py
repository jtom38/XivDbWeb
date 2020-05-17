from flask import render_template, Blueprint
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from typing import List
from sqlalchemy.orm import sessionmaker, Session, Query
import json

apiWeapons_bp = Blueprint('apiWeapons', __name__)

d = DB(Base)

@apiWeapons_bp.route('/list')
def weaponList() -> List[Weapon]:
    items: List[Weapon] = []
    session = d.newSession()
    try:
        for names in session.query(Weapon.name, Weapon.level, 
            Weapon.itemLevel, Weapon.id):
            items.append({
                'name': names[0],
                'level': names[1],
                'itemLevel': names[2],
                'id': names[3]
            })
        session.close()
    except Exception as e:
        print(e)
    return json.dumps(items)

@apiWeapons_bp.route('/<string:name>/latest')
def weaponByName(name: str) -> Weapon:
    items: List[Weapon] = []
    session = d.newSession()
    try:
        for names in session.query(Weapon.name, Weapon.level, 
            Weapon.itemLevel, Weapon.id):
            items.append({
                'name': names[0],
                'level': names[1],
                'itemLevel': names[2],
                'id': names[3]
            })
        session.close()
    except Exception as e:
        print(e)
    return json.dumps(items)
