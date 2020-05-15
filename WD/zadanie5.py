a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))

if (0<a<=10) and (a>b or b>c):
    print('a zawiera sie w przedziale od 0 do 10, oraz a jest wieksze od b lub b jest wieksze od c')
else:
    print('warunek nie zostal spelniony')