from xivdb.sql import DB, Base, Weapon, Stats, Repair, Materia
from typing import List
import csv


class importCsv:
    def __init__(self):
        self.db = DB(Base)
        pass

    def intakeWeapons(self, row: int) -> Weapon:
        with open("weapons.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            lineNumber: int = 0
            for line in r:
                if lineNumber == 0:
                    lineNumber = lineNumber + 1
                    continue

                session = self.db.session()
                try:
                    name = line[3]
                    res: Weapon = session.query(Weapon).filter(
                        Weapon.name == name
                    ).one()
                    if name == res.name:
                        print(f"{name} is already present in SQL.")
                    return Weapon()
                except Exception as e:
                    print(e)
                    w = self.db.newWeapon()
                    w.url = line[1]
                    w.pictureUrl = line[2]
                    w.name = line[3]
                    w.rarity = line[4]
                    w.untradeable = self.checkBoolResult(line[5])
                    w.unique = self.checkBoolResult(line[6])
                    w.slot = str(line[7])
                    w.itemLevel = int(line[8])
                    w.jobs = line[9]
                    w.level = line[10]
                    w.compnayCrest = self.checkBoolResult(line[11])
                    w.armorie = self.checkBoolResult(line[12])
                    w.glamourChest = self.checkBoolResult(line[13])
                    w.dyeable = self.checkBoolResult(line[14])
                    w.extractable = self.checkBoolResult(line[15])
                    w.projectable = self.checkBoolResult(line[16])
                    w.desynth = str(line[17])

                    return w
        pass

    def intakeStats(self, row: int) -> Stats:
        with open("stats.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            lineNumber: int = 0
            for line in r:
                if lineNumber == 0:
                    lineNumber = lineNumber + 1
                    continue

                s = self.db.newStats()

                s.str = line[1]
                s.vit = line[2]
                s.dex = line[3]
                s.int = line[4]
                s.mnd = line[5]
                s.det = line[6]
                s.skl = line[7]
                s.spl = line[8]
                s.dhr = line[9]
                s.ten = line[10]
                s.pie = line[11]
                return s

    def intakeRepair(self, row: int) -> Repair:
        with open("repair.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            i = self.db.newRepair()
            lineNumber: int = 0
            for line in r:
                if lineNumber != row:
                    lineNumber = lineNumber + 1
                    continue

                i.job = line[1]
                i.level = line[2]
                i.material = line[3]
                return i

    def intakeMateria(self, row: int) -> Materia:
        with open("materia.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            i = self.db.newMateria()
            lineNumber: int = 0
            for line in r:
                if lineNumber != row:
                    lineNumber = lineNumber + 1
                    continue

                i.slots = line[1]
                i.melderJob = line[2]
                i.melderLevel = line[3]
                i.advancedMelding = self.checkBoolResult(line[4])
                return i

    def checkBoolResult(self, res: str) -> bool:
        if res == "True":
            return True
        else:
            return False

    def getAllWeapons(self) -> List[Weapon]:
        weapons: List[Weapon] = []
        with open("weapons.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            lineNumber: int = 0
            for line in r:
                if lineNumber == 0:
                    lineNumber = lineNumber + 1
                    continue

                w = self.db.newWeapon()
                w.url = str(line[1])
                w.pictureUrl = str(line[2])
                w.name = str(line[3])
                w.rarity = str(line[4])
                w.untradeable = self.checkBoolResult(line[5])
                w.unique = self.checkBoolResult(line[6])
                w.slot = str(line[7])
                w.itemLevel = int(line[8])
                w.jobs = str(line[9])
                w.level = int(line[10])
                w.compnayCrest = self.checkBoolResult(line[11])
                w.armorie = self.checkBoolResult(line[12])
                w.glamourChest = self.checkBoolResult(line[13])
                w.dyeable = self.checkBoolResult(line[14])
                w.extractable = self.checkBoolResult(line[15])
                w.projectable = self.checkBoolResult(line[16])
                w.desynth = float(line[17])
                weapons.append(w)
        return weapons

    def getAllStats(self) -> List[Stats]:
        stats: List[Stats] = []
        with open("stats.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            lineNumber: int = 0
            for line in r:
                if lineNumber == 0:
                    lineNumber = lineNumber + 1
                    continue

                s = self.db.newStats()
                s.str = int(line[1])
                s.vit = int(line[2])
                s.dex = int(line[3])
                s.int = int(line[4])
                s.mnd = int(line[5])
                s.det = int(line[6])
                s.skl = int(line[7])
                s.spl = int(line[8])
                s.dhr = int(line[9])
                s.ten = int(line[10])
                s.pie = int(line[11])
                stats.append(s)
        return stats

    def getAllRepairs(self) -> List[Repair]:
        repairs: List[Repair] = []
        with open("repair.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            lineNumber: int = 0
            for line in r:
                if lineNumber == 0:
                    lineNumber = lineNumber + 1
                    continue

                i = self.db.newRepair()
                i.job = str(line[1])
                i.level = int(line[2])
                i.material = str(line[3])
                repairs.append(i)

        return repairs

    def getAllMateria(self) -> List[Materia]:
        materias: List[Materia] = []
        with open("materia.csv", "r") as csvfile:
            r = csv.reader(csvfile, delimiter=",")
            lineNumber: int = 0
            for line in r:
                if lineNumber == 0:
                    lineNumber = lineNumber + 1
                    continue

                i = self.db.newMateria()
                i.slots = str(line[1])
                i.melderJob = str(line[2])
                i.melderLevel = int(line[3])
                i.advancedMelding = self.checkBoolResult(line[4])
                materias.append(i)

        return materias
