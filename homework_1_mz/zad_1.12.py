'''
Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.

Użytkownik może wprowadzać komendy zmieniające położenie postaci.

Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku.

Wyjście poza planszę oznacza koniec gry.

Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.

Dodatkowo:
- po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym
miejscu,
- z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.

'''

import math
import random

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)
skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)
minimalna_liczba_krokow = (abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y))
liczba_krokow = 0


while True:
    if gracz_x == skarb_x and gracz_y == skarb_y and liczba_krokow == 0:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        continue

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f"Znalazłeś skarb! Zajęło Ci to {liczba_krokow} kroków")
        break
    elif gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print("Wyszedłeś poza planszę, koniec gry")
        break

    if liczba_krokow > 2 * minimalna_liczba_krokow:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        liczba_krokow = 0
        print("Za dużo kroków, nowe położenie skarbu i zerowanie kroków")
        continue


    print(f"Twoja pozycja to x={gracz_x}, y={gracz_y}")
    kierunek = input("Podaj kierunek używając 'w', 's', 'd', lub 'a': ")
    szansa_na_podpowiedz = random.randint(1, 5)
    odleglosc_od_skarbu = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)

    if szansa_na_podpowiedz != 5:
        if kierunek == "w" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            > math.sqrt((skarb_x - gracz_x) ** 2 +(skarb_y - (gracz_y + 1)) ** 2):
            print("Idziesz w dobrym kierunku")
            gracz_y += 1
            liczba_krokow += 1
        elif kierunek == "s" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            > math.sqrt((skarb_x - gracz_x) ** 2 +(skarb_y - (gracz_y - 1)) ** 2):
            print("Idziesz w dobrym kierunku")
            gracz_y -= 1
            liczba_krokow += 1
        elif kierunek == "d" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            > math.sqrt((skarb_x - (gracz_x + 1)) ** 2 +(skarb_y - gracz_y) ** 2):
            print("Idziesz w dobrym kierunku")
            gracz_x += 1
            liczba_krokow += 1
        elif kierunek == "a" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            > math.sqrt((skarb_x - (gracz_x - 1)) ** 2 +(skarb_y - gracz_y) ** 2):
            print("Idziesz w dobrym kierunku")
            gracz_x -= 1
            liczba_krokow += 1
        elif kierunek == "w" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            < math.sqrt((skarb_x - gracz_x) ** 2 +(skarb_y - (gracz_y + 1)) ** 2):
            print("Idziesz w złym kierunku")
            gracz_y += 1
            liczba_krokow += 1
        elif kierunek == "s" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            < math.sqrt((skarb_x - gracz_x) ** 2 +(skarb_y - (gracz_y - 1)) ** 2):
            print("Idziesz w złym kierunku")
            gracz_y -= 1
            liczba_krokow += 1
        elif kierunek == "d" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            < math.sqrt((skarb_x - (gracz_x + 1)) ** 2 +(skarb_y - gracz_y) ** 2):
            print("Idziesz w złym kierunku")
            gracz_x += 1
            liczba_krokow += 1
        elif kierunek == "a" and math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)\
            < math.sqrt((skarb_x - (gracz_x - 1)) ** 2 +(skarb_y - gracz_y) ** 2):
            print("Idziesz w złym kierunku")
            gracz_x -= 1
            liczba_krokow += 1
        else:
            print("Niepoprawna instrukcja")
            continue

    else:
        if kierunek == 'w':
            gracz_y += 1
            liczba_krokow += 1
        elif kierunek == 's':
            gracz_y -= 1
            liczba_krokow += 1
        elif kierunek == 'd':
            gracz_x += 1
            liczba_krokow += 1
        elif kierunek == 'a':
            gracz_x -= 1
            liczba_krokow += 1
        else:
            print('Niepoprawny kierunek')
            continue





