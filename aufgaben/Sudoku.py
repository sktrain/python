# Ein Sudoku-Spiel besteht aus 81 Feldern in einem 9-×-9-Gitter.
# Das Gitter lässt sich in neun Blöcke zerlegen, jeder Block ist
# ein zweidimensionales Array der Größe 3 × 3.
# In jedem dieser Blöcke muss jede Zahl von 1 bis 9 genau einmal vorkommen
# — keine darf fehlen.
# Schreibe ein Programm, das ein zweidimensionales Array mit neun Elementen
# daraufhin testet, ob alle Zahlen von 1 bis 9 vorkommen.
# Fehlende Elemente sollen via print gemeldet werden.

# Das folgende Array ist eine gültige Sudoku-Belegung
array = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

# Das folgende Array ist keine gültige Sudoku-Belegung

array = [
    [ 1, 2, 3 ],
    [ 4, 2, 6 ],
    [ 7, 8, 8 ]
]

