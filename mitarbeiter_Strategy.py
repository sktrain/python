""" Version der Mitarbeiterklasse mit Gehaltsmodell als abstrakte Vorgabe"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from datetime import date
from decimal import Decimal


class Geschlecht(Enum):
    D = 1,
    W = 2,
    M = 3

class Gehaltsmodell(ABC):
    @abstractmethod
    def get_gehalt(self):
        pass

    def __str__(self):
        pass

class Arbeitermodell(Gehaltsmodell):
    def __init__(self, stdlohn: Decimal, stdzahl: Decimal):
        self.__stdlohn = stdlohn
        self.__stdzahl = stdzahl

    def set_stdlohn(self, stdlohn: Decimal) -> None:
        self__stdlohn = stdlohn

    def set_stdzahl(self, stdzahl: Decimal) -> None:
        self.__stdzahl = stdzahl

    def get_gehalt(self) -> Decimal:
        return self.__stdzahl * self.__stdlohn

    def __str__(self):
        return f"Arbeitermodell [stdlohn={self.__stdlohn}, stdzahl={self.__stdzahl} ]"

class Fixgehaltmodell(Gehaltsmodell):
    def __init__(self, gehalt: Decimal):
        self.__gehalt = gehalt

    def set_gehalt(self, gehalt: Decimal) -> None:
        self.__gehalt = gehalt

    def get_gehalt(self) -> Decimal:
        return self.__gehalt

    def __str__(self):
        return f"Fixgehaltmodell [gehalt={self.__gehalt} ]"


@dataclass
class Mitarbeiter:
    """ Version der Mitarbeiterklasse als Dataclass"""

    __persnr: int
    __vorname: str
    __nachname: str
    __gebdatum: date
    __einstdatum: date
    __gehaltmodell: Gehaltsmodell
    __geschlecht: Geschlecht = Geschlecht.D

    # Getter / Setter

    def get_persnr(self) -> int:
       return self.__persnr

    def set_persnr(self, persnr: int) -> None:
        self.__persnr = persnr

    def get_vorname(self) -> str:
        return self.__vorname

    def set_vorname(self, vorname: object) -> None:
        self.__vorname = vorname

    def get_nachname(self) -> str:
        return self.__nachname

    def set_nachname(self, nachname: str) -> None:
        self.__nachname = nachname

    def get_gebdatum(self) -> date:
        return self.__gebdatum

    def set_gebdatum(self, gebdatum: date) -> None:
        self.__gebdatum = gebdatum

    def get_einstdatum(self) -> date:
        return self.__einstdatum

    def set_einstdatum(self, einstdatum: date) -> None:
        self.__einstdatum = einstdatum

    def get_gehalt(self) -> Decimal:
        return self.__gehaltmodell.get_gehalt()

    def get_gehaltsmodell(self) -> Gehaltsmodell:
        return self.__gehaltmodell

    def set_gehaltmodell(self, gehaltmodell: Gehaltsmodell) -> None:
        self.__gehaltmodell = gehaltmodell

    def get_geschlecht(self) -> Geschlecht:
        return self.__geschlecht

    def set_geschlecht(self, geschlecht: Geschlecht) -> None:
        self.__geschlecht = geschlecht

    def __str__(self):
        return f"Mitarbeiter [persnr={self.__persnr}, vorname={self.__vorname}, nachname={self.__nachname}, gebdatum={self.__gebdatum}, einstdatum={self.__einstdatum}, ges={self.__geschlecht}, gehalt=" + str(self.get_gehalt()) + " ]"

    


####### Nutzen ##############

m1 = Mitarbeiter(1, "Max", "Muster", date(2000,
                 1, 1), date(2020, 1, 1), Fixgehaltmodell(Decimal("5000")), Geschlecht.D)

print(m1.get_persnr())
print(m1.get_vorname())
print(m1.get_nachname())
print(m1)
#print(m1.__dict__)

arbeitermodell = Arbeitermodell(Decimal(20), Decimal(100))
arbeiter = Mitarbeiter(10, "Max", "Maulwurf", date(2000,
                 1, 1), date(2020, 1, 1), arbeitermodell,
                       Geschlecht.M)
print(arbeiter)
print(arbeiter.get_gehaltsmodell().get_gehalt())

# setze beim Arbeiter neue Parameter
# print("setze beim Arbeiter neue Parameter")
# print(type(arbeiter.get_gehaltsmodell()))
# arbeitermodel = arbeiter.get_gehaltsmodell()
# arbeitermodel.set_stdlohn(Decimal(50))
# print(arbeitermodel)
# print(arbeiter.get_gehalt())

print("setze neues Arbeitermodell")
neues_arbeitermodel = Arbeitermodell(50, 100)
arbeiter.set_gehaltmodell(neues_arbeitermodel)
print(arbeiter.get_gehalt())

# mache Arbeiter zu Fixgehaltmitarbeiter:
arbeiter.set_gehaltmodell(Fixgehaltmodell(10000))
print(arbeiter.get_gehalt())
