'''
Napisz program, który na podstawie wprowadzonych wymiarów opakowania
(x, y, z) obliczy jego objętość oraz sprawdzi, czy jest ona większa od 1 litra (1000 cm3).

​
'''

while True:
    try:
        x = int(input("Podaj długość opakowania w cm: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

while True:
    try:
        y = int(input("Podaj szerokość opakowania w cm: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

while True:
    try:
        z = float(input("Podaj wysokość opakowania w cm: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

objetosc = x * y * z

if objetosc > 1000:
    print("Objętość opakowania jest większa niż 1 litr")
elif objetosc == 1000:
    print("Objętość opakowania jest równa 1 litr")
else:
    print("Objętość opakowania jest mniejsza niż 1 litr")