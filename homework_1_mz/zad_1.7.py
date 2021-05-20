'''
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić
i jaka jest jego cena. Wyświetl odpowiedni komunikat.

​

Przykład:

Co chcesz kupić? - ziemniaki

Podaj cenę towaru - 5

Podaj ilość towaru - 10

​

Za ziemniaki, który chcesz kupić, zapłacisz 50 zł

​
'''

towar = input("Powiedz co chesz kupić: ")

while True:
    try:
        ilosc_towaru = int(input("Powiedz ile jednostek tego towaru chcesz kupić: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

while True:
    try:
        cena_jednostkowa_towaru = int(input("Powiedz jaka jest jednostkowa cena tego towaru w złotówkach: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

cena_zakupow = ilosc_towaru * cena_jednostkowa_towaru
print(f"Za podane zakupy należy zapłacić {cena_zakupow}zł")