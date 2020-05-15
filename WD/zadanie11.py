import sys

wysokosc = int(input("Podaj wysokosc diamentu: "))

litera = str("o")
a = int(1)

if 3 <= wysokosc <= 9:
    if wysokosc % 2 == 0:
        print("Nie moge zbudowac diamentu ! Liczba musi byc nieparzysta")
    else:

        srodek = int((wysokosc+1)/2)
        sr = srodek
        while 1 < sr:
            sr = sr-1
            print(" " * sr, end = '')
            print("o" * ((srodek-sr)+(srodek-sr)-1))
        print("o" * ((srodek * 2)-1))

        while a < srodek:
            print(" " * a, end = '')
            print("o" * ((srodek-a)+(srodek-a)-1))
            a = a+1


else:
    print("Nie moge zbudowac diamentu ! Blednie wpisana wysokosc")