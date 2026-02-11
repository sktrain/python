# Wir erstellen ein Objekt der Klasse Motorrad:

class Motorrad():
    def __init__(self, marke, hubraum):
        self.marke = marke
        self.__hubraum = hubraum

    def set_hubraum(self, kubik):
        if (kubik <= 0):
            print("Error: Negativer Wert für den Hubraum! \
                    Der Wert wurde nicht geändert")
        else:
            self.__hubraum = kubik
            print("Hubraum wurde geändert.")

    def get_hubraum(self):
        return self.__hubraum

##########################################################################
### Aufgabe 1
motrad = Motorrad("KTM", 950)

# motrad.set_hubraum(600)     # unerwünscht, aber möglich
#
# motrad.__hubraum += 400     # so nicht möglich
#
# motrad._Motorrad__hubraum += 400  # aber so möglich!!
#
# motrad.marke += 2       # Typ-Fehler
#
# print(motrad.__hubraum)         # so nicht möglich (wie oben)
#
# print(motrad.marke)
#
# print(motrad.get_hubraum())


###############################################################
### Aufgabe 2

das_rad = Motorrad("Buell", -1200)          # negativer Wert ist möglich
print(das_rad.get_hubraum())            # -1200

#### Veränderte Klasse #########

class Motorrad():
    def __init__(self, marke, hubraum):
        self.marke = marke
        self.set_hubraum(hubraum)

    def set_hubraum(self, kubik):
        if (kubik <= 0):
            print("Error: Negativer Wert für den Hubraum! \
                    Der Wert wurde nicht geändert")
        else:
            self.__hubraum = kubik
            print("Hubraum wurde geändert.")

    def get_hubraum(self):
        return self.__hubraum

das_rad = Motorrad("Buell", -1200)          # negativer Wert ist möglich
print(das_rad.get_hubraum())            # jetzt schlägt diese Variante fehl

