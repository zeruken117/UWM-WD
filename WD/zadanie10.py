wysokosc = int(input("Podaj wysokosc wiezy: "))

litera = str("A")
i = int(0)

if 0<wysokosc<=10:
    while i<wysokosc:
        print(litera)
        litera = litera + str("A")
        i = i + 1
else:
    print("Nie moge zbudowac wiezy ! Blednie wpisana wysokosc")