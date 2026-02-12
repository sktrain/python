strings = ["Baby Shark", "Corona", "Baby Yoda", "Corona", "Baby Yoda", "Tiger King",
    "David Bowie", "Kylie Jenner", "Kardashian", "Love Island", "Bachelorette",
    "Baby Yoda", "Tiger King", "Billie Eilish", "Corona"]

haeufigkeit = {}
for string in strings:
    if string in haeufigkeit:
        haeufigkeit[string] += 1
    else:
        haeufigkeit[string] = 1

print(haeufigkeit)