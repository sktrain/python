# Schreibe eine Funktion summe(), welche für die Eingabe einer Zahl n folgendes Resultat ausgibt:
# Summe der Zahlen von 1 bis n

def summe(n):
    summe = sum(range(n+1))
    print("Summe der Zahlen von 1 bis n", summe)



# Aufruf

summe(100)

