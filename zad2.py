km = float(input("Ile kilometrów planujesz przejechać: "))
spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena = float(input("Podaj cenę paliwa za litr: "))
p = int(input("Podaj liczbę pasażerów: "))

paliwo = km * spalanie / 100
koszt = paliwo * cena
na_osobe = koszt / p

print("Zużycie paliwa:", paliwo, "l")
print("Koszt podróży:", koszt, "zł")
print("Koszt na osobę:", na_osobe, "zł")

if km > 500:
    print("Długa trasa – zaplanuj przerwy na odpoczynek!")
