liczba = str(input("Podaj liczbe wielocyfrowa: "))

wynik = int(0)

i = int(0)

while i<len(str(liczba)):
    wynik = wynik + int(liczba[i])
    i = i + 1

print("Suma cyfr tworzacych ta liczbe wynosi: " + str(wynik))