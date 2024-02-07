import random

benutzereingabe = input("Bitte gib sechs Zahlen zwischen 1 und 49 ein, jeweils durch ein Leerzeichen getrennt.\n")

tipp = [int(zahl) for zahl in benutzereingabe.split(" ")]

gewinnzahlen = []

schleifendurchlaeuf = 0


while gewinnzahlen != tipp:
    zufallszahlen = []

    for _ in range(6):
        zufallszahlen.append(random.randint(1, 49))

    tipp.sort()
    zufallszahlen.sort()

    gewinnzahlen = []

    for zahl in tipp:
        if zahl in zufallszahlen:
            gewinnzahlen.append(zahl)

    anzahl_richtige = len(gewinnzahlen)

    schleifendurchlaeuf += 1

print("Glückwunsch! Die Zufallszahlen entsprechen dem Tipp.")
print("Es hat", schleifendurchlaeuf, "Spielen gedauert, bis Lottogewinn.")
