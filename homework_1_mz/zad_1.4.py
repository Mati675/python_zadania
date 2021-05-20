'''
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza,
ile trzeba zapłacić. Zasady są takie:

​

- nieletni (poniżej 18 roku życia) płacą 100 zł za noc

- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:

	- 200 zł za noc, jeśli nocują jedną noc

	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy

	- 150 zł za noc, jeśli nocują pięć lub więcej nocy

- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

​

Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z
10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.
'''

while True:
    try:
        wiek = int(input("Podaj swój wiek: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")


while True:
    try:
        czas_pobytu = int(input("Podaj ile dni zamierzasz spędzić w hotelu: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")



if wiek < 18:
    cena_za_noc = 100
elif 18 <= wiek < 65 and czas_pobytu == 1:
    cena_za_noc = 200
elif 18 <= wiek < 65 and 2 <= czas_pobytu < 5:
    cena_za_noc = 180
elif 18 <= wiek < 65 and czas_pobytu >= 5:
    cena_za_noc = 150
elif wiek >= 65 and czas_pobytu == 1:
    cena_za_noc = 200 * 0.9
elif wiek >= 65 and 2 <= czas_pobytu < 5:
    cena_za_noc = 180 * 0.9
elif wiek >= 65 and czas_pobytu >= 5:
    cena_za_noc = 150 * 0.9

koszt_pobytu = czas_pobytu * cena_za_noc
print(koszt_pobytu)