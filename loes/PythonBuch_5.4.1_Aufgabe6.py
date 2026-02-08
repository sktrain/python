# Schreibe ein Programm, welches eine Liste von Zahlen sortiert und gib das Ergebnis in der Konsole aus.
# Für die Liste [1,4,3,3,5,7,2] sollte das Ergebnis die Liste [1,2,3,3,4,5,7] sein.
#
#   a. Speichere die Liste in der ersten Zeile als Variable ab und sortiere sie anschliessend.
#
#   b. Frage den Benutzer nach der Liste von Zahlen. Überlege dir, wie du es am besten lösen kannst,
#      dass der Benutzer eine vorher nicht bekannte Anzahl Zahlen eingeben kann.

# Das Interessante ist das einlesen!
# z.B.
liste = input("Liste durch leerzeichen getrennt: ").split()  # Listenelemente sind Strings
liste_zahlen=[]
for i in liste:
    liste_zahlen.append(int(i))
liste_zahlen.sort()         # sort existiert bereits!
print(liste_zahlen)

