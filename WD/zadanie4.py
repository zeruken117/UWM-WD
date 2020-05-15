liczba = int(input("Podaj liczbe, ktorej wartosc bezwzgledna chcesz obliczyc: "))

if liczba<0:
    liczba = liczba*(-1)

print("Wartosc bezwzgledna z tej liczby wynosi: " + str(liczba))