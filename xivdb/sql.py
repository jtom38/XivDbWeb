from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Boolean,
    ForeignKey,
    create_engine,
    Binary
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
import sqlalchemy
import psycopg2
import uuid
from dotenv import load_dotenv
from pathlib import Path
import os
import XivDbReader.collections

Base = declarative_base()

class Env:
    def __init__(self):
        envPath: str = Path(".env")
        load_dotenv(envPath)

        self.pgUser = os.getenv("pgUser")
        self.pgPass = os.getenv("pgPass")
        self.pgHost = os.getenv("pgHost")
        self.pgPort = os.getenv("pgPort")
        self.pgDb = os.getenv("pgDb")
        pass

class Stats(Base):
    __tablename__ = "stats"
    id = Column(String, primary_key=True)
    str = Column(Integer)
    vit = Column(Integer)
    dex = Column(Integer)
    int = Column(Integer)
    mnd = Column(Integer)
    pie = Column(Integer)
    det = Column(Integer)
    spl = Column(Integer)
    skl = Column(Integer)
    dhr = Column(Integer)
    ten = Column(Integer)

    def __init__(self) -> None:
        self.id = uuid.uuid4()

    def convertToSqlObject(self, parseData:XivDbReader.collections.Stats) -> None:
        t = str(type(parseData))
        if 'stats' in t.lower():
            self.str = parseData.strength
            self.vit = parseData.vitality
            self.dex = parseData.dexterity
            self.int = parseData.intelligence
            self.mnd = parseData.mind
            self.pie = parseData.piety
            self.det = parseData.determination
            self.spl = parseData.spellSpeed
            self.skl = parseData.skillSpeed
            self.dhr = parseData.directHitRate
            self.ten = parseData.tenacity


class Repair(Base):
    __tablename__ = "repair"
    id = Column(String, primary_key=True)
    job = Column(String)
    level = Column(Integer)
    material = Column(String)

    def __init__(self) -> None:
        self.id = uuid.uuid4()

    def convertToSqlObject(self, parseData: XivDbReader.collections.RepairInfo) -> None:
        t = str(type(parseData))
        if 'repair' in t.lower():
            self.job = parseData.job
            self.level = parseData.level
            self.material = parseData.material


class Materia(Base):
    __tablename__ = "materia"
    id = Column(String, primary_key=True)
    slots = Column(Integer)
    melderJob = Column(String)
    melderLevel = Column(Integer)
    advancedMelding = Column(Boolean)

    def __init__(self) -> None:
        self.id = uuid.uuid4()
    
    def convertToSqlObject(self, parseData: XivDbReader.collections.Materia) -> None:
        t = str(type(parseData))
        if 'materia' in t.lower():
            self.slots = parseData.slots
            self.melderJob = parseData.melderJob
            self.melderLevel = parseData.melderLevel
            self.advancedMelding = parseData.advancedMelding

class PictureIcon(Base):
    __tablename__ = 'pictureicon'
    id = Column(String, primary_key=True)
    url = Column(String)
    pictureBinary = Column(Binary)

    def __init__(self) -> None:
        self.id = uuid.uuid4()

class Weapon(Base):
    __tablename__ = "weapon"
    id = Column(String, primary_key=True)
    url = Column(String)
    pictureUrl = Column(String)
    name = Column(String)
    rarity = Column(String)
    untradeable = Column(Boolean)
    unique = Column(Boolean)
    slot = Column(String)
    itemLevel = Column(Integer)
    jobs = Column(String)
    level = Column(Integer)
    companyCrest = Column(Boolean)
    armorie = Column(Boolean)
    glamourChest = Column(Boolean)
    dyeable = Column(Boolean)
    extractable = Column(Boolean)
    projectable = Column(Boolean)
    desynth = Column(Float)
    patch = Column(String)

    stats_id = Column(String, ForeignKey("stats.id"))
    stats = relationship(Stats, backref=backref("weapon", uselist=True))

    repair_id = Column(String, ForeignKey("repair.id"))
    repair = relationship(Repair, backref=backref("weapon", uselist=True))

    materia_id = Column(String, ForeignKey("materia.id"))
    materia = relationship(Materia, backref=backref("weapon", uselist=True))

    #pictureIcon_id = Column(String, ForeignKey("pictureicon.id"))
    #pictureIcon = relationship(PictureIcon, backref=backref('weapon', uselist=True))

    def __init__(self):
        self.id = uuid.uuid4()

    def convertToSqlObject(self, parseData:XivDbReader.collections.Weapon) -> None:
        t = str(type(parseData))
        if 'weapon' in t.lower():
            self.url = parseData.url
            self.pictureUrl = parseData.pictureUrl
            self.name = parseData.name
            self.rarity = parseData.rarity
            self.untradeable = parseData.untradable
            self.unique = parseData.unique
            self.slot = parseData.slot
            self.itemLevel = parseData.itemLevel
            self.jobs = parseData.jobs
            self.level = parseData.level
            self.companyCrest = parseData.companyCrest
            self.armorie = parseData.armorie
            self.glamourChest = parseData.glamourChest
            self.dyeable = parseData.dyeable
            self.extractable = parseData.extractable
            self.projectable = parseData.projectable
            self.desynth = parseData.desynth
            self.patch = parseData.patch

class DB:
    def __init__(self, Base):
        env: Env = Env()
        url: str = f"postgresql://{env.pgUser}:{env.pgPass}@{env.pgHost}:{env.pgPort}/{env.pgDb}"
        self.engine = create_engine(url, client_encoding="utf8")
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        self.Base = Base
        self.Base.metadata.create_all(self.engine)

    def newWeapon(self) -> Weapon:
        w = Weapon()
        w.id = uuid.uuid4().__str__()
        w.stats = self.newStats()
        w.materia = self.newMateria()
        w.repair = self.newRepair()
        return w

    def newStats(self) -> Stats:
        s = Stats()
        s.id = uuid.uuid4().__str__()
        return s

    def newSession(self) -> Session:
        s: Session = self.session()
        return s

    def newMateria(self) -> Materia:
        m = Materia()
        m.id = uuid.uuid4().__str__()
        return m

    def newRepair(self) -> Repair:
        r = Repair()
        r.id = uuid.uuid4().__str__()
        return r
