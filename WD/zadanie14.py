import math

liczba = int(input("Podaj liczbe, ktora chcesz spierwiastkowac: "))

try:
    pierwiastek = float(math.sqrt(liczba))
    print("Pierwiastek z podanej liczby wynosi: " + str(pierwiastek))

except ValueError:
    print("To nie jest poprawna liczba, sprobuj ponownie !")