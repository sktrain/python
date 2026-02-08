# Schreibe ein Programm, welches den Benutzer nach einem oder mehreren deutschen Sätzen fragt.
# Anschliessend verändert das Programm den Text so, dass bei jedem Wort der erste und der letzte Buchstabe
# stehen gelassen werden und alle Buchstaben dazwischen jeweils wie Jasskarten gemischt werden.
# Das heisst, dass keine Buchstaben dazu kommen und auch keine entfernt werden, jedoch die Reihenfolge verändert wird.
# Gib anschliessend den so entstandenen Text aus.
from random import shuffle

string = input("Satz oder mehrere Sätze: ")
flag = False    # Flag für Wort
liste = []  # für die neue veränderte Zeichenfolge
puffer = [] # für den Shuffle-Teil
last_char = ""
for char in list(string):
    if char.isalpha() and not(flag):  # Wort beginnt
        print(char)
        flag = True
        liste.append(char)
    elif flag and char.isalpha():  # Wort geht weiter
        puffer.append(last_char)    # das vorher gelesene Zeichen in den Puffer
        last_char = char
        print(puffer)
    elif flag:                  # Wortende ist erreicht und nächstes Zeichen ist kein Buchstabe
        flag = False
        print("before shuffle", puffer)
        shuffle(puffer)
        print("After Shuffle",puffer)
        liste.extend(puffer)
        liste.append(last_char)
        liste.append(char)
        puffer.clear()
        last_char = ""
    else:                  # nächstes Zeichen ist kein Buchstabe
        liste.append(char)

# Code-Duplizierung unschön -> besser in Funktion auslagern
# falls das letzte Zeichen ein Buchstabe ist
print("before shuffle", puffer)
shuffle(puffer)
print("After Shuffle",puffer)
liste.extend(puffer)
liste.append(last_char)
print(liste)
string = "".join(liste)
print(string)



