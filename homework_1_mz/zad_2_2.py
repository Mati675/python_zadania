'''
Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:

​

    *

  * * *

* * * * *
'''

while True:
    try:
        liczba = int(input("Podaj liczbę całkowitą: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

for x in range(liczba):
    print(" " * (liczba - (x + 1)), '*' * (2 * x + 1))