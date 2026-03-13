""" Jetzt die Mitarbeiterverwaltung """
import random
from datetime import date
from decimal import Decimal

from mitarbeiter_Strategy import Mitarbeiter, Geschlecht, Fixgehaltmodell, Arbeitermodell


class Mitarbeiterverwaltung:

    def __init__(self):
        # Liste mit 100 Mitarbeitern als Dummy-Objekte
        self.__mlist = []
        for i in range(100):
            if i%2 == 0:
                # Fixgehalt
                m = Mitarbeiter(1, "Evelin", "Musterfrau" + str(i), date(2000,1, 1),
                                 date(2020, 1, 1),
                                 Fixgehaltmodell(Decimal(random.randint(100, 10000))),
                                 Geschlecht.W)
            else:
                # Arbeiter
                m = Mitarbeiter(1, "Max", "Maulwurf" + str(i), date(2000, 1, 1),
                                 date(2020, 1, 1),
                                 Arbeitermodell(Decimal(random.randint(10, 90)), Decimal(100)),
                                 Geschlecht.M)
            self.__mlist.append(m)

    def get_mlist(self ):
        return self.__mlist

    def getgehaltsumme(self):
        summe = 0
        for m in self.__mlist:
            summe += m.get_gehalt()
        return summe


###  Aufruf/Nutzung

mv = Mitarbeiterverwaltung()
for m in mv.get_mlist():
    print(m)
print("*" * 50)
print(mv.getgehaltsumme())