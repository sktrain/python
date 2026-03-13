""" Version der Mitarbeiterklasse als dataclass"""

from dataclasses import dataclass
from enum import Enum
from datetime import date
from decimal import Decimal


class Geschlecht(Enum):
    D = 1,
    W = 2,
    M = 3

@dataclass
class Mitarbeiter:
    """ Version der Mitarbeiterklasse als Dataclass"""

    __persnr: int
    __vorname: str
    __nachname: str
    __gebdatum: date
    __einstdatum: date
    __gehalt: Decimal
    __geschlecht: Geschlecht # = Geschlecht.D



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
        return self.__gehalt

    def set_gehalt(self, gehalt: Decimal) -> None:
        self.__gehalt = gehalt

    def get_geschlecht(self) -> Geschlecht:
        return self.__geschlecht

    def set_geschlecht(self, geschlecht: Geschlecht) -> None:
        self.__geschlecht = geschlecht

    def __str__(self):
        return f"Mitarbeiter [persnr={self.__persnr}, vorname={self.__vorname}, nachname={self.__nachname}, gebdatum={self.__gebdatum}, einstdatum={self.__einstdatum}, ges={self.__geschlecht}, gehalt={self.__gehalt} ]"

    


####### Nutzen ##############

# m1 = Mitarbeiter(1, "Max", "Muster", date(2000,
#                  1, 1), date(2020, 1, 1), Decimal("5000"), Geschlecht.D)
#
# print(m1.get_persnr())
# print(m1.get_vorname())
# #m1.set_nachname("Karrer")
# print(m1.get_nachname())
# print(m1)
# print(m1.__dict__)
#
# m2 = m1
# print (m1 == m2)
# print (m1 is m2)
#
# m2 = Mitarbeiter(1, "Max", "Muster", date(2000,
#                  1, 1), date(2020, 1, 1), Decimal("5000"))
#
# print (m1 == m2)
# print (m1 is m2)
# print(m1.__repr__())

@dataclass
class Arbeiter(Mitarbeiter):
    __stdlohn: Decimal
    __stdzahl: Decimal

    def set_stdlohn(self, stdlohn: Decimal) -> None:
        self__stdlohn = stdlohn

    def set_stdzahl(self, stdzahl: Decimal ) -> None:
        self.__stdzahl = stdzahl

    def get_gehalt(self) -> Decimal:
        return self.__stdzahl * self.__stdlohn


arbeiter = Arbeiter(10, "Max", "Maulwurf", date(2000,
                 1, 1), date(2020, 1, 1), Decimal(100) * Decimal(20),
                    Geschlecht.M, Decimal(20), Decimal(100))

print(arbeiter.get_gehalt())

arbeiter.set_gehalt(Decimal(50000))
print(arbeiter.get_gehalt())
