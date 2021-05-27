'''
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża,
czy za mała. Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując,
w której próbie udało się zgadnąć liczbę.

​

Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją
i pełni w informatyce bardzo ważną rolę. Umiejętnie ją stosując powinno się te zagadki rozwiązywać
w 9-10 próbach (bo 2^10=1024).

​
'''

import random

odpowiedz = random.randint(0, 999)
ilosc_prob = 0

while True:
    try:
        liczba = int(input("Podaj liczbę w zakresie od 0 do 999: "))
        ilosc_prob += 1
        if liczba == odpowiedz:
            print(f"Gratulacje! Odgadnąłęś liczbę, zajęło Ci to {ilosc_prob} prób")
            break
        elif 999 >= liczba > odpowiedz:
            print("Zła odpowiedź, podałeś liczbę większą niż odpowiedź, spróbuj ponownie")
        elif 0 <= liczba < odpowiedz:
            print("Zła odpowiedź, podałeś liczbę mniejszą niż odpowiedź, spróbuj ponownie")
        elif liczba > 999:
            print("Zła odpowiedź, podałeś liczbę większą niż odpowiedź, spoza zakresu, spróbuj ponownie")
        elif liczba < 0:
            print("Zła odpowiedź, podałeś liczbę mniejszą niż odpowiedź, spoza zakresu, spróbuj ponownie")
    except ValueError:
        print("Nieprawidłowe dane, spróbuj ponownie")

