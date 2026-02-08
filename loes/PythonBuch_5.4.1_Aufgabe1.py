# Schreibe ein Programm, welches den Benutzer mit Hilfe von input() nach einem Satz fragt.
#
# Das Programm soll anschliessend die Anzahl Worte im Satz sowie die Anzahl Buchstaben ausgeben.
#
# Erweitere das Programm so, dass es auch angibt, wie viele Buchstaben davon Grossbuchstaben sind.

satz = input("Bitte Satz eingeben: \n")

# Methodik der str-Klasse nutzen
list_of_words = satz.split()
anzahl_words = len(list_of_words)

anzahl_nonwhitespace = 0
anzahl_letters = 0
anzahl_capitals = 0
for word in list_of_words:
    anzahl_nonwhitespace += len(word)
    for letter in word:
        if letter.isalpha():
            anzahl_letters += 1
            if letter.isupper():
                anzahl_capitals += 1


print("Worte:", anzahl_words)
print("Keine Leerzeichen:",anzahl_nonwhitespace)
print("Buchstaben:", anzahl_letters)
print("Großbuchstaben:",anzahl_capitals)






