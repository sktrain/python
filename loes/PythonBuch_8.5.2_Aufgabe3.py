# Aufgabe 3
# Schreibe die Klasse Person von oben folgendermasen um, so dass das Gewicht einer Person
# garantiert nie negativ gesetzt werden kann. Benutze dazu setter() und getter() Methoden.

class Person:
    def __init__(self, name, vorname, geb_datum, gewicht):
        self.name = name
        self.vorname = vorname
        self.geb_datum = geb_datum
        self.set_gewicht(gewicht)

    def vorstellen(self):
        text = "Hallo.\nIch heisse " \
               + self.vorname + " " \
               + self.name + ", wiege " \
               + str(self.__gewicht) + " kg und habe am " \
               + self.geb_datum + " Geburtstag.\n"\
               + "Nice to meet you."
        print(text)

    def abnehmen(self, wie_viel):
        print("Altes Gewicht:",self.__gewicht,"kg")

        self.set_gewicht(self.__gewicht - wie_viel)

        print("Neues Gewicht:",self.__gewicht,"kg")

    def set_gewicht(self, gewicht):
        if gewicht < 0:
            raise ValueError("Gewicht must be greater than zero.")
        self.__gewicht = gewicht

    def get_gewicht(self):
        return self.__gewicht

##########################################################################
### Nutzer

p = Person("Karrer", "Stephan", "1.1.1999", 100)
p.vorstellen()
#p.abnehmen(10)
print(p.get_gewicht())
p.set_gewicht(40)
print(p.get_gewicht())
p.abnehmen(40)
print(p.get_gewicht())
p.set_gewicht(100)
print(p.get_gewicht())
p.abnehmen(101)









