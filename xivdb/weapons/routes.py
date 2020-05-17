from flask import render_template, Blueprint, send_file
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats, PictureIcon
from typing import List
from sqlalchemy.orm import sessionmaker, Session, Query
import os
import io

d = DB(Base)
session: Session = d.newSession()
weapon_bp = Blueprint('weapons', __name__, template_folder="templates")

@weapon_bp.route('/')
def index():
    return render_template('weapons/index.html')

@weapon_bp.route('/list')
def weaponsList():
    items: List[dict] = []
    session = d.newSession()
    try:
        for names in session.query(Weapon.name,Weapon.level ,Weapon.itemLevel ,Weapon.id ):
            items.append({
                'name': names[0]
                ,'level': names[1]
                ,'itemLevel': names[2]
                ,'id': names[3]
            })
          
    except Exception as e:
        print(e)
        
    session.close()

    return render_template('weapons/list.html', items=items)


@weapon_bp.route('/details/<string:index>')
def details(index: str):
    item = Weapon()
    session = d.newSession()
    try:
        for items in session.query(Weapon).filter(Weapon.id == index):
            item = items

        for m in session.query(Materia).filter(Materia.id == item.materia_id):
            item.materia = m

        for r in session.query(Repair).filter(Repair.id == item.repair_id):
            item.repair = r
        
        for s in session.query(Stats).filter(Stats.id == item.stats_id):
            item.stats = s

    except Exception as e:
        print(e)
    session.close()
    return render_template('weapons/details.html', item=item)