'''
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
'''

import random

liczba_1 = random.randint(0, 99)
liczba_2 = random.randint(0, 99)

print(liczba_1, liczba_2)

while True:
    try:
        odpowiedz = int(input("Jaka jest suma podanych liczb? "))
        if odpowiedz == liczba_1 + liczba_2:
            print("Prawidłowa odpowiedź")
            break
        else:
            print("Nieprawidłowa odpowiedź, spróbuj ponownie")
    except ValueError:
        print("Niewłaściwy rodzaj odpowiedzi, spróbuj ponownie")
