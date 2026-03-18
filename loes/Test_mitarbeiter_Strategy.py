from datetime import date
from decimal import Decimal
from unittest import TestCase

from Mitarbeiterverwaltung import Mitarbeiter, Fixgehaltmodell, Geschlecht, KarrerException


class TestMitarbeiter(TestCase):
    def test_get_persnr(self):
        pass


    def test_set_persnr(self):
        self.fail()

    def test_get_vorname(self):
        self.fail()

    def test_set_vorname(self):
        self.fail()

    def test_get_nachname(self):
        m = Mitarbeiter("Max", "Muster", date(2000,
                                              1, 1), date(2020, 1, 1), Fixgehaltmodell(Decimal("5000")), Geschlecht.D)
        m.set_nachname("Karrer")
        self.assertEqual(m.get_nachname(), "Karrer")

    def test_set_nachname(self):
        m = Mitarbeiter("Max", "Muster", date(2000,
                                              1, 1), date(2020, 1, 1), Fixgehaltmodell(Decimal("5000")), Geschlecht.D)
        with self.assertRaises(KarrerException):
            m.set_nachname("1")
        with self.assertRaises(KarrerException):
            m.set_nachname("abc")
        with self.assertRaises(KarrerException):
            m.set_nachname("A")

    def test_get_gebdatum(self):
        self.fail()

    def test_set_gebdatum(self):
        self.fail()

    def test_get_einstdatum(self):
        self.fail()

    def test_set_einstdatum(self):
        self.fail()

    def test_get_gehalt(self):
        self.fail()

    def test_get_gehaltsmodell(self):
        self.fail()

    def test_set_gehaltmodell(self):
        self.fail()

    def test_get_geschlecht(self):
        self.fail()

    def test_set_geschlecht(self):
        self.fail()
