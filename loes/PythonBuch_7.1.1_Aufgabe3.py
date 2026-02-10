# Definiere eine Funktion teilermenge(zahl), welche die Menge der Teiler von zahl ausgibt.
# Zum Beispiel
# teilermenge(24)  ->  [1, 2, 3, 4, 6, 8, 12, 24]

def teilermenge(zahl):
    teilerliste = [1]
    for i in range (1,zahl):
        if zahl%i == 0:
            teilerliste.append(i)
    teilerliste.append(zahl)
    # return teilerliste     # wäre auch möglich
    print(teilerliste)


#########################
# Aufruf
teilermenge(24)

