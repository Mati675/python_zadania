'''
Napisz program, który odczytuje od użytkownika wiele liczb.
Program powinien wyliczyć i na końcu wypisać następujące statystyki:

- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum

NIE używaj funkcji wbudowanych!
'''
liczby = []

while True:
    dane = input("Podaj liczbę lub powiedz koniec: ")
    try:
        float(dane)
        liczby.append(float(dane))
    except ValueError:
        if dane.lower() == "koniec":
            break
        else:
            print("Złe dane, sprobuj ponownie")

print(liczby)
ilosc_liczb = 0
suma_liczb = 0
min_liczb = 0
max_liczb = 0

for liczba in liczby:
    ilosc_liczb += 1
    suma_liczb += liczba
    if liczba < min_liczb or min_liczb == 0:
        min_liczb = liczba
    elif liczba > max_liczb or max_liczb == 0:
        max_liczb = liczba

srednia_liczb = suma_liczb / ilosc_liczb

print(f"Ilość liczb wynosi {ilosc_liczb}")
print(f"Suma liczb wynosi {suma_liczb}")
print(f"Średnia liczb wynosi {srednia_liczb}")
print(f"Najmniejsza liczba to {min_liczb}")
print(f"Największa liczba to {max_liczb}")


