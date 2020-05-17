
from xivdb.sql import DB, Base, Weapon, Repair, Materia, Stats
from xivdb.importCsv import importCsv
from typing import List
from sqlalchemy.orm import sessionmaker
from XivDbReader import Reader
import sqlalchemy.orm

d = DB(Base)
session: sessionmaker = d.newSession()
w = d.newWeapon()

read: Reader = Reader(job='whm')
whm = read.getArms(recordLimit=1)

for i in whm:
    try:
        res: Weapon = session.query(Weapon).filter(Weapon.name == i.name).one()
    except Exception as e:
        #print(f"{i.name} was not found in the DB.")
        

ic = importCsv()
counter: int = 1

weapons: List[Weapon] = ic.getAllWeapons() 
stats: List[Stats] = ic.getAllStats()
repairs: List[Repair] = ic.getAllRepairs()
materias: List[Materia] = ic.getAllMateria()
counter: int = 0
for i in weapons:
    try:
        res: Weapon = session.query(Weapon).filter(Weapon.name == i.name).one()
        counter = counter + 1
        if res.name != None:
            print(f"Skiped - {i.name}")
            continue

    except:
        w: Weapon = i
        s: Stats = stats[counter]
        r: Repair = repairs[counter]
        m: Materia = materias[counter]
        w.stats = s
        w.repair = r
        w.materia = m
        session.add(w)
        counter = counter + 1

        try:
            session.commit()
            print(f"Added - {w.name}")
        except Exception as e:
            print(e)
            

session.close()

