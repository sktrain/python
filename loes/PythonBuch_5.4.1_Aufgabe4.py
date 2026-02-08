# Im Zahlenlotto werden sechs Zahlen aus 49 zufällig ausgewählt, wobei keine doppelt vorkommen darf.
# Schreibe ein Programm, welches 6 Zahlen aus 49 zufällig wählt. Verwende dafür wiederum Funktionen
# aus dem random Modul.
# a. Benutze ausschliesslich die randrange() Funktion, um dies zu erreichen.
# b. Lies die Dokumentation des random Moduls und versuche jene Funktion zu finden, mit welcher du
# die Aufgabe am einfachsten lösten kannst. (Das heisst mit möglichst wenig Programmcode)

from random import randrange, sample


# Lösung a
def lotto_6of49_a():
    tipps = [randrange(1, 50)]
    while len(tipps) < 6:
        nexttip = randrange(1, 50)
        if nexttip not in tipps:
            tipps.append(nexttip)
    return tipps


# Aufruf
print("Mein Tip:", lotto_6of49_a())

# Lösung b
def lotto_6of49_b():
    tipps = sample(range(1, 50), 6)
    return tipps


# Aufruf
print("Mein Tip:", lotto_6of49_b())
