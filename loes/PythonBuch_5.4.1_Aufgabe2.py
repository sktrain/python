# Schreibe ein Programm, welches den Benutzer nach einer Zahl fragt und anschliessend prüft,
# ob diese Zahl eine Primzahl ist.

# Simples Verfahren: Probedivision
from math import sqrt

zahl = abs(int(input("Bitte Ganzzahl: ")))
boolean = True
for teiler in range(2,int(sqrt(zahl))+1):
    if zahl % teiler == 0:
        print("Zahl", zahl, "ist durch", teiler, "teilbar")
        boolean = False
        break
if (boolean):
    print("Zahl", zahl, "ist prim")

