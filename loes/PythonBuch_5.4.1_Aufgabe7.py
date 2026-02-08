# Schreibe ein Programm, welches eine Liste von vom Benutzer eingegebenen Worten alphabetisch sortiert.

# Das Interessante ist das einlesen!
# z.B.
string = input("Liste durch Komma getrennt: ").replace(","," ")  # ersetzen des Kommas durch Leerzeichen
# print(string)
wortliste = string.split()  # jetzt kann das Splitten einfach anhand Leerzeichen erfolgen
print(wortliste)
wortliste.sort()
print(wortliste)     # print(wortliste.sort()) funktioniert nicht, da nichts zurück geliefert wird!!
# Allerdings ist die Sortierung ASCII-Like (Großbuchstaben vor Kleinbuchstaben)
# Um das zu beheben:
wortliste.sort(key=str.lower)
print(wortliste)

