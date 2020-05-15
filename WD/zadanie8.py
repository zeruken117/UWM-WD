a = 1
z = 1
print("Program dodaje liczby do listy, zatrzymuje sie po wprowadzeniu 0")
lista = ""
while(z != 0):
    z = int(input("Podaj liczbe " + str(a) + " aby dodac ja do listy: "))
    a += 1
    lista += (str(z) + ", ")
else:
    print("Koniec petli, lista wyglada nastepujaco: " + str(lista))