# Das Collatz-Problem gehört zu den ungelösten Problemen der Mathematik.
# Es besagt, dass jede Abfolge von Zahlen, welche nach der folgenden Regel gebildet wird,
# irgendwann bei der Zahl 1 landet:
#   - Die Folge beginnt bei einer beliebigen Zahl.
#   - Ist die momentane Zahl n gerade, so ist die nächste Zahl die Hälfte von dieser, also n//2
#   - Ist die momentane Zahl n ungerade, so ist die nächste Zahl um eins grösser als das dreifache der Zahl, also 3*n+1
#
# Schreibe ein Programm, welches diese Folge für eine vom Benutzer gewählte Zahl ausgibt und mit der
# Berechnung stoppt, sobald 1 erreicht wurde.

def collatz(n):
    folge = [n]
    i = n
    while i > 1:
        if i%2 == 0:
            i = i//2
        else:
            i= i*3+ 1
        folge.append(i)
    return folge


# Aufruf
zahl = abs(int(input("Positive Ganzzzahl: ")))
print(collatz(zahl))