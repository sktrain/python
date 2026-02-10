# Ob ein Jahr im Gregorianischen Kalender ein Schaltjahr ist, kann nach den folgenden Regeln entschieden werden:
#
#     Jahre sind Schaltjahre, falls ihre Jahrzahl durch 400 teilbar ist.
#
#     Jahre sind Schaltjahre, falls ihre Jahrzahl durch 4 teilbar ist, ausser die Jahrzahl ist durch 100 teilbar.
#
# Schreibe ein Programm, welches den Benutzer nach einer Jahreszahl fragt und anschliessend prüft,
# ob es sich um ein Schaltjahr handelt.

jahr = int(input("Jahr: "))

if jahr % 400 == 0:
    print(jahr, "ist Schaltjahr")
elif jahr % 4 == 0:
    if jahr % 100 == 0:
        print(jahr, "ist kein Schaltjahr")
    else:
        print(jahr, "ist Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")


# oder besser und kompakter
jahr = int(input("Jahr: "))

if jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0):
    print(jahr, "ist Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")

