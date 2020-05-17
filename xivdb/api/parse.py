from flask import render_template, Blueprint
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from typing import List, Dict
from sqlalchemy.orm import Session, Query
from json import dumps

from XivDbReader import Reader

d = DB(Base)

parse_bp = Blueprint('parse', __name__)

@parse_bp.route('/weapons/<string:job>/<int:amount>', methods=['POST'])
def importWeaponsByJob(job: str, amount: int):
    r = Reader(job)
    results = r.getArms(amount)

    msg: List[Dict] = []
    if len(results) >= 1:
        db = DB(Base)
        session = db.newSession()
        for i in results:
            try:
                sqlRes = session.query(Weapon).filter(Weapon.name == i.name).one()
                msg.append({
                    "msg": f"Item was already present.",
                    "item": i.name
                })
            except Exception as e:
                w = Weapon()
                w.convertToSqlObject(i)
                w.stats = Stats()
                w.stats.convertToSqlObject(i.stats)
                w.repair = Repair()
                w.repair.convertToSqlObject(i.repair)
                w.materia = Materia()
                w.materia.convertToSqlObject(i.materia)
                session.add(w)
                session.commit()
                msg.append({
                    "msg": "Item was added to the database",
                    "item": i.name
                })
        session.close()
    return dumps(msg)
