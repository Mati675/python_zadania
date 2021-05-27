'''
Zakładamy, że 1 ludzki rok, to 5 lat psich.

​

Za pomocą konsoli wczytaj imię i wiek psa.

​

Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.

​

Przykład:

Podaj imię psa - Burek

Podaj wiek psa - 3

​

Gdyby Burek był człowiekiem, miałby 15 lat.
'''

imie_psa = input("Podaj imię psa: ")

while True:
    try:
        wiek_psa = int(input("Podaj wiek psa: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

psie_lata = wiek_psa * 5
print(f"Gdyby {imie_psa} był człowiekiem, miałby {psie_lata} lat.")