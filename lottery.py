import random

benutzereingabe = input("Bitte gib sechs Zahlen zwischen 1 und 49 ein, jeweils durch ein Leerzeichen getrennt.\n")

tipp = [int(zahl) for zahl in benutzereingabe.split(" ")]

zufallszahlen = []

for _ in range(6):
    zufallszahlen.append(random.randint(1, 49))

# Listen sortieren
tipp.sort()
zufallszahlen.sort()

print("Tipp:", tipp)
print("Zufallszahlen:", zufallszahlen)

gewinnzahlen = []

# Für jedes Element von Tipp prüfen, ob es in der List zufallszahlen enthalten ist
for zahl in tipp:
    if zahl in zufallszahlen:
        gewinnzahlen.append(zahl)

# Anzahl der richtigen Zahlen
anzahl_richtige = len(gewinnzahlen)

print("Du hast folgende richtige Zahlen:", end=" ")
for zahl in gewinnzahlen:
    print(zahl, end=" ")
print("Du hast ", anzahl_richtige, "richtige Zahlen:", end=" ")
for zahl in gewinnzahlen:
    print(zahl, end=" ")
print("aus der Ziehung", zufallszahlen)
