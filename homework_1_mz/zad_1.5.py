'''
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą,
oblicza pole powierzchni trójkąta o takich bokach.

​

Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).

​

Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:

​

```

import math

​

x = math.sqrt(10)
'''

import math

while True:
    while True:
        try:
            a = float(input("Podaj długość pierwszego boku trójkąta: "))
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")
            continue

    while True:
        try:
            b = float(input("Podaj długość drugiego boku trójkąta: "))
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")
            continue

    while True:
        try:
            c = float(input("Podaj długość trzeciego boku trójkąta: "))
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")
            continue
    if a < b + c and b < a + c and c < a + b:
        break
    else:
        print("Z takich boków nie da się stworzyć trójkąta, spróbuj ponownie")


p = (a + b + c) / 2
print(f"Pole trojkąta wynosi: {math.sqrt(p * (p - a) * (p - b) * (p - c))}")