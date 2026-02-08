# Schreibe ein Programm, welches alle Primzahlen zwischen 1 und einer vom Benutzer
# gewählten oberen Grenze ausgibt.
#
# Zusatzaufgabe: Versuche im Internet herauszufinden, wie man dieses Problem möglichst effizient
# (d.h. so, dass es wenig Zeit braucht) löst und schreibe dein Programm um, damit es schneller wird.

# Simples Verfahren: Nutzt die Probedivision aus Aufgabe 2 für jede Zahl:

from math import sqrt

limit = (int(input("Bitte positive Ganzzzahl: ")))
prim_liste = []

for i in range(1, limit+1):
    boolean = True
    for teiler in range(2,int(sqrt(i))+1):
        if i % teiler == 0:
            boolean = False
            break
    if (boolean):
        prim_liste.append(i)

print(prim_liste)


############################################################################
# hübschere Variante, die das ganze in Funktionen kapselt

def isPrime(n):
    boolean = True
    for teiler in range(2, int(sqrt(n)) + 1):
        if n % teiler == 0:
            boolean = False
            break
    return boolean

def primeList(n):
    prim_liste = []
    for i in range(1,limit + 1):
        if (isPrime(i)):
            prim_liste.append(i)
    return(prim_liste)

# Aufruf
limit = (int(input("Bitte positive Ganzzzahl: ")))
prim_liste = primeList(limit)
print(prim_liste)





##########################################################################################
# Performantere Variante: Sieb des Eratosthenes
# Quelle: https://www.delftstack.com/de/howto/python/sieve-of-eratosthenes-in-python/
# geringfügig ergänzt, da ich 1 als Primzahl betrachte!

def sieveOfEratosthenes(val):
    max = val + 1
    lst = [True] * max
    for i in range(2, int(val ** 0.5 + 1)):
        if lst[i]:
            for j in range(i * i, max, i):
                lst[j] = False
    final = []
    for i in range(1, max):
        if lst[i]:
            final.append(i)
    return final


# Aufruf
limit = (int(input("Bitte positive Ganzzzahl: ")))
print(sieveOfEratosthenes(limit))


##########################################################################################
# Performantere Variante: Sieb von Atkin
# Quelle: https://www.geeksforgeeks.org/dsa/sieve-of-atkin/
#
def sieveOfAtkin(val):
    limit = val

    # intialise the arr array
    # with initial 0 values
    arr = [0] * (limit + 1)

    # mark 2 and 3 as prime
    if limit > 2:
        arr[2] = 1
    if limit > 3:
        arr[3] = 1

    # check for all three conditions
    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):

            # condition 1
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                arr[n] = (arr[n] + 1) % 2

            # condition 2
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                arr[n] = (arr[n] + 1) % 2

            # condition 3
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                arr[n] = (arr[n] + 1) % 2

    # Mark all multiples
    # of squares as non-prime
    for i in range(5, limit + 1):
        if i * i > limit:
            break
        if arr[i] == 0:
            continue
        for j in range(i * i, limit + 1, i * i):
            arr[j] = 0

    # store all prime numbers
    primes = [1]        # Ergänzung bzgl. der Quelle, da 1 prim
    for i in range(2, limit + 1):
        if arr[i] == 1:
            primes.append(i)
    return primes



# Aufruf
limit = (int(input("Bitte positive Ganzzzahl: ")))
print(sieveOfAtkin(limit))



