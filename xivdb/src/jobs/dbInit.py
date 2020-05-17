
import os
import requests
import shutil
from typing import List
from xivdb.sql import Weapon, Stats, Materia, Repair, PictureIcon, DB, Base
#from xivdb.src.jobs import Job
from XivDbReader import Reader


class DbInit():
    def __init__(self) -> None:
        self.db = DB(Base)
        self.cd = os.getcwd()
        self.cd = f"{self.cd}/xivdb/static/images/itemIcons/"
        pass

    def runJob(self) -> None:
        self.downloadExternalData()
        pass

    def downloadExternalData(self) -> None:
        r = Reader(job='gnb')
        gnbList: List[Weapon] = r.getArms(recordLimit=10)
        for i in gnbList:
            self.checkSql(i)

    def checkSql(self, item: Weapon) -> None:
        session = self.db.newSession()
        try:
            returnedItem: Weapon = session.query(Weapon).filter(Weapon.name == item.name).one()
            session.close()
        except Exception as e:
            w: Weapon = Weapon()
            w.convertToSqlObject(item)
            s: Stats = Stats()
            s.convertToSqlObject(item.stats)
            r: Repair = Repair()
            r.convertToSqlObject(item.repair)
            m: Materia = Materia()
            m.convertToSqlObject(item.materia)

            w.stats = s
            w.repair = r
            w.materia = m
            
            self.downloadPicturesToStatic(w.pictureUrl, w.name)
            session.add(w)
            session.commit()
            session.close()

    def downloadPicturesToStatic(self, pictureUrl: str, itemName: str) -> None:
        png = f"{self.cd}{itemName}.png"
        if os.path.exists(png) == False:
            self.downloadPicture(png, pictureUrl)

            if os.path.exists(png) == False:
                print(f"failed to download icon for {itemName}")


    def downloadPicture(self, pngPath: str, pictureUrl: str) -> None:
        try:
            requestRes = requests.get(pictureUrl, stream=True)
            requestRes.raw.decode_content = True
            with open(pngPath, 'wb') as imgFile:
                shutil.copyfileobj(requestRes.raw, imgFile)
        except Exception as e:
            print(e)