from enum import Enum
from datetime import date
from decimal import Decimal


class Geschlecht(Enum):
    D = 1,
    W = 2,
    M = 3


class Mitarbeiter:
    """ Zweite Version der Mitarbeiterklasse mit wert-mäßiger Gleichheit"""

    def __init__(self, persnr: int, vorname: str, nachname: str, gebdatum: date,
                 einstdatum: date, gehalt: Decimal, geschlecht: Geschlecht = Geschlecht.D, /):
        """
        :type nachname: str
        :type persnr: int
        :type vorname: str
        :type einstdatum: date
        :type gebdatum: date
        :type geschlecht: Geschlecht
        :type gehalt: Decimal
        """
        self.__persnr = persnr
        self.__vorname = vorname
        self.__nachname = nachname
        self.__gebdatum = gebdatum
        self.__einstdatum = einstdatum
        self.__geschlecht = geschlecht
        self.__gehalt = gehalt

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

    # def __eq__(self, other) -> bool:
    #     if self is other:
    #         return True
    #     if (other is None) or (not isinstance(other, Mitarbeiter)):
    #         return False
    #     if self.__persnr != other.get_persnr():
    #         return False
    #     if self.__vorname != other.get_vorname():
    #         return False
    #     if self.__nachname != other.get_nachname():
    #         return False
    #     if self.__gebdatum != other.get_gebdatum():
    #         return False
    #     if self.__einstdatum != other.get_einstdatum():
    #         return False
    #     if self.__gehalt != other.get_gehalt():
    #         return False
    #     if self.__geschlecht != other.get_geschlecht():
    #         return False
    #     return True

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if (other is None) or (not isinstance(other, Mitarbeiter)):
            return False
        if (self.__persnr != other.__persnr
                or self.__vorname != other.__vorname
                or self.__nachname != other.__nachname
                or self.__gebdatum != other.__gebdatum
                or self.__einstdatum != other.__einstdatum
                or self.__gehalt != other.__gehalt
                or self.__geschlecht != other.__geschlecht):
            return False
        return True





####### Nutzen ##############

m1 = Mitarbeiter(1, "Max", "Muster", date(2000,
                 1, 1), date(2020, 1, 1), Decimal("5000"))

print(m1.get_persnr())
print(m1.get_vorname())
m1.set_nachname("Karrer")
print(m1.get_nachname())
print(m1)
print(m1.__dict__)

m2 = m1
print(m2==m1)
print(m2 is m1)

m2 = Mitarbeiter(1, "Max", "Karrer", date(2000,
                 1, 1), date(2020, 1, 1), Decimal("5000"))

print(m2.__eq__(m1))
print(m2 is m1)

