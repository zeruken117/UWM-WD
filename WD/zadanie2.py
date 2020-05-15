import sys

print("Podaj liczbe a: ")
a = int(sys.stdin.readline())
print("Podaj liczbe b: ")
b = int(sys.stdin.readline())

wynik = int(a*b)

sys.stdout.write("Wynik mnozenia liczby a przez b wynosi: " + str(wynik))