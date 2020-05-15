a = int(input("Ile kwadratow liczb chcesz obliczyc : "))

for x in range (1,a+1,1):
    b = int(input("Podaj liczbe, ktorej kwadrat chcesz obliczyc: "))
    w = b*b
    print("Kwadratem liczby " + str(b) + " jest " + str(w))