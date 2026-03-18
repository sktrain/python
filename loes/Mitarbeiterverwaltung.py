""" Jetzt die Mitarbeiterverwaltung inklusive der benötigten Klassen für Mitarbeiter"""

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from datetime import date, datetime
from decimal import Decimal
from re import fullmatch


class KarrerException(Exception):
    def __init__(self, message, value):
        self.__message = message
        self.__value = value

    def __str__(self):
        return f"{self.__value} verursacht: {self.__message}"


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
        self.__constraint(stdlohn)
        self.__constraint(stdzahl)
        self.__stdlohn = stdlohn
        self.__stdzahl = stdzahl

    def set_stdlohn(self, stdlohn: Decimal) -> None:
        self.__constraint(stdlohn)
        self__stdlohn = stdlohn

    def set_stdzahl(self, stdzahl: Decimal) -> None:
        self.__constraint(stdzahl)
        self.__stdzahl = stdzahl

    def get_gehalt(self) -> Decimal:
        return self.__stdzahl * self.__stdlohn

    def __str__(self):
        return f"Arbeitermodell [stdlohn={self.__stdlohn}, stdzahl={self.__stdzahl} ]"

    def __constraint(self, value: Decimal):
        if value < 0:
            raise KarrerException("Gehaltsparameter muss >= 0 sein", value)


class Fixgehaltmodell(Gehaltsmodell):
    def __init__(self, gehalt: Decimal):
        self.__constraint(gehalt)
        self.__gehalt = gehalt

    def set_gehalt(self, gehalt: Decimal) -> None:
        self.__constraint(gehalt)
        self.__gehalt = gehalt

    def get_gehalt(self) -> Decimal:
        return self.__gehalt

    def __str__(self):
        return f"Fixgehaltmodell [gehalt={self.__gehalt} ]"

    def __constraint(self, value: Decimal):
        if value < 0:
            raise KarrerException("Gehaltsparameter muss >= 0 sein", value)


@dataclass
class Mitarbeiter:
    """ Version der Mitarbeiterklasse als Dataclass"""

    __persnr: int = field(init=False)  # Not in __init__
    __vorname: str
    __nachname: str
    __gebdatum: date
    __einstdatum: date
    __gehaltmodell: Gehaltsmodell
    __geschlecht: Geschlecht = Geschlecht.D

    counter = 1

    def __post_init__(self):
        self.__namen_constraint(self.__nachname)
        self.__namen_constraint(self.__vorname)
        self.__date_constraint(self.__gebdatum)
        self.__persnr = Mitarbeiter.counter
        Mitarbeiter.counter += 1

    # Getter / Setter

    def get_persnr(self) -> int:
        return self.__persnr

    def set_persnr(self, persnr: int) -> None:
        self.__persnr = persnr

    def get_vorname(self) -> str:
        return self.__vorname

    def set_vorname(self, vorname: str) -> None:
        self.__namen_constraint(vorname)
        self.__vorname = vorname

    def get_nachname(self) -> str:
        return self.__nachname

    def set_nachname(self, nachname):
        self.__namen_constraint(nachname)
        self.__nachname = nachname

    def get_gebdatum(self) -> date:
        return self.__gebdatum

    def set_gebdatum(self, gebdatum: date) -> None:
        self.__date_constraint(gebdatum)
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
        return f"Mitarbeiter [persnr={self.__persnr}, vorname={self.__vorname}, nachname={self.__nachname}, gebdatum={self.__gebdatum}, einstdatum={self.__einstdatum}, ges={self.__geschlecht}, gehalt=" + str(
            self.get_gehalt()) + " ]"

    def __namen_constraint(self, name: str):
        if not fullmatch(r"[A-Z][a-z].*", name):
            raise KarrerException("Dieser Name ist nicht moeglich: ", name)

    def __date_constraint(self, datum: date):
        today = datetime.now()
        age = today.year - datum.year - ((today.month, today.day) < (datum.month, datum.day))
        if age < 16 or age > 79:
            raise KarrerException("Mitarbeiter hat falsches Alter: ", age)


class Mitarbeiterverwaltung:


    def __init__(self):
        # Liste mit 100 Mitarbeitern als Dummy-Objekte
        self.__mlist = []
        for i in range(100):
            if i%2 == 0:
                # Fixgehalt
                m = Mitarbeiter("Evelin", "Musterfrau" + str(i), date(2000,1, 1),
                                 date(2020, 1, 1),
                                 Fixgehaltmodell(Decimal(random.randint(100, 10000))),
                                 Geschlecht.W)
            else:
                # Arbeiter
                m = Mitarbeiter("Max", "Maulwurf" + str(i), date(2000, 1, 1),
                                 date(2020, 1, 1),
                                 Arbeitermodell(Decimal(random.randint(10, 90)), Decimal(100)),
                                 Geschlecht.M)
            self.__mlist.append(m)


    def get_mlist(self , keyextractor = None):
        if keyextractor:
            return sorted(self.__mlist, key= keyextractor)
        else:
            self.__mlist.sort(key = Mitarbeiter.get_persnr)
            return self.__mlist

    def get_mitarbeiter_by_persnr(self, persnr):
        return self.__mlist[Mitarbeiterverwaltung.counter-1]

    def insert_mitarbeiter(self, mitarbeiter):
        self.__mlist.append(mitarbeiter)

    def getgehaltsumme(self) -> Decimal:
        summe = 0
        for m in self.__mlist:
            summe += m.get_gehalt()
        return summe



if __name__ == '__main__':
    ##  Aufruf/Nutzung

    mv = Mitarbeiterverwaltung()

    mlist = mv.get_mlist(Mitarbeiter.get_gehalt)
    for m in mlist:
        print(m)
    print("*" * 50)

    print(mv.getgehaltsumme())

    m1 = Mitarbeiter( "Max", "Muster", date(2000,
                     1, 1), date(2020, 1, 1), Fixgehaltmodell(Decimal("5000")), Geschlecht.D)
    print(m1)

    mv.insert_mitarbeiter(m1)

    print(mlist[-1])