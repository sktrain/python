# Schreibe eine Funktion quersumme(zahl), welche die Quersumme von zahl
# berechnet und zurückgibt.

def quer(zahl):
    string = str(zahl)      # string-Darstellung liefert die Ziffern
    ergebnis = 0
    for ziffer in string:
        ergebnis += int(ziffer)
    return ergebnis


#########################
# Aufruf
print(quer(1234))


