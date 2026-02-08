# Schreibe ein Programm, welches den Benutzer nach einem oder mehreren deutschen Sätzen fragt.
# Anschliessend verändert das Programm den Text so, dass bei jedem Wort der erste und der letzte Buchstabe
# stehen gelassen werden und alle Buchstaben dazwischen jeweils wie Jasskarten gemischt werden.
# Das heisst, dass keine Buchstaben dazu kommen und auch keine entfernt werden, jedoch die Reihenfolge verändert wird.
# Gib anschliessend den so entstandenen Text aus.
from random import shuffle

# string = input("Satz oder mehrere Sätze: ")
# flag = False    # Flag für Wort
# liste = []  # für die neue veränderte Zeichenfolge
# puffer = [] # für den Shuffle-Teil
# last_char = ""
# for char in list(string):
#     if char.isalpha() and not(flag):  # Wort beginnt
#         print(char)
#         flag = True
#         liste.append(char)
#     elif flag and char.isalpha():  # Wort geht weiter
#         puffer.append(last_char)    # das vorher gelesene Zeichen in den Puffer
#         last_char = char
#         print(puffer)
#     elif flag:                  # Wortende ist erreicht und nächstes Zeichen ist kein Buchstabe
#         flag = False
#         print("before shuffle", puffer)
#         shuffle(puffer)
#         print("After Shuffle",puffer)
#         liste.extend(puffer)
#         liste.append(last_char)
#         liste.append(char)
#         puffer.clear()
#         last_char = ""
#     else:                  # nächstes Zeichen ist kein Buchstabe
#         liste.append(char)
#
# # Code-Duplizierung unschön -> besser in Funktion auslagern
# # falls das letzte Zeichen ein Buchstabe ist
# print("before shuffle", puffer)
# shuffle(puffer)
# print("After Shuffle",puffer)
# liste.extend(puffer)
# liste.append(last_char)
# print(liste)
# string = "".join(liste)
# print(string)



#################################################################################
###     Alternativ:
#################################################################################



string = input("Satz oder mehrere Sätze: ")

wortliste = string.split()  # Liste von Strings, eventuell mit Satzzeichen bzw. Anführungszeichen
print(wortliste)
realwortliste = []
# Vorsicht: Strings sind immutable!
for wort in wortliste:
    w = wort.lstrip("'\"")
    print(w)
    w = w.rstrip((",.!?'\""))
    print(w)
    realwortliste.append(w)
print(realwortliste)
print("#########################################")

resultstring = ""
i = 0
j = 0
while i < len(string):
    resultstring += string[i]
    while j < len(realwortliste):
        if string[i] == realwortliste[j]:         # Wort beginnt
                puffer = []
                for char in wort[1:-1]:     # Puffer für Shuffle füllen
                    puffer.append(char)
                print("before shuffle", puffer)
                shuffle(puffer)
                print("After Shuffle", puffer)
                resultstring.join(puffer)
        resultstring += wort[-1]
        i = i + len(wort)
        j = j + 1
        break
    i = i + 1

print(resultstring)



# wortliste.sort()
# print(wortliste)     # print(wortliste.sort()) funktioniert nicht, da nichts zurück geliefert wird!!
# # Allerdings ist die Sortierung ASCII-Like (Großbuchstaben vor Kleinbuchstaben)
# # Um das zu beheben:
# wortliste.sort(key=str.lower)
# print(wortliste)

