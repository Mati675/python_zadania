'''
Założenia:

	- 0-6   - wiek przedszkolny - cena biletu: 0

	- 7-17  - wiek szkolny      - cena biletu: 2.28

	- 18-64 - wiek dorosły      - cena biletu: 3.80

	- +65   - wiek emerytalny   - cena biletu: 1.90

​

Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety
i ile biletów chce kupić.

​

Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
'''

while True:
    try:
        wiek = int(input("Podaj swój wiek: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")


while True:
    try:
        ilosc_biletow = int(input("Podaj ile biletów chcesz kupić: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")


if wiek <= 6:
    cena = 0 * ilosc_biletow
elif 6 < wiek <= 17:
    cena = 2.28 * ilosc_biletow
elif 17 < wiek <= 64:
    cena = 3.8 * ilosc_biletow
else:
    cena = 1.9 * ilosc_biletow

print(f"Cena biletów to: {cena}")