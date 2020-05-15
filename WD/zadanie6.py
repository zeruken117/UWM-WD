a = int(input("Podaj poczatek przedzialu : "))
b = int(input("Podaj koniec przedzialu: "))

for x in range (a,b,1):
    if int(x)%5==0:
        print("Liczba " + str(x) + " jest podzielna przez 5")