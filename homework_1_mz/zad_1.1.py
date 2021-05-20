'''
Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.

​

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków
i ile kilo chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.

​

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
'''

while True:
    try:
        cena_ziemniakow_1 = float(input("Podaj cenę za 1kg ziemniaków w złotówkach: "))
        print(f"Za 5kg ziemniaków trzeba zapłacić {cena_ziemniakow_1 * 5}zł")
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

while True:
    try:
        cena_ziemniakow_2 = float(input("Podaj cenę za 1kg ziemniaków w złotówkach: "))
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

while True:
    try:
        ilosc_ziemniakow_2 = float(input("Powiedz ile kg ziemniakow chcesz kupic: "))
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

print(f"Za podaną ilość ziemniaków trzeba zapłacić {cena_ziemniakow_2 * ilosc_ziemniakow_2}zł")

while True:
    try:
        cena_ziemniakow_3 = float(input("Podaj cenę za 1kg ziemniaków w złotówkach: "))
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

while True:
    try:
        ilosc_ziemniakow_3 = float(input("Powiedz ile kg ziemniakow chcesz kupic: "))
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

while True:
    try:
        cena_bananow = float(input("Podaj cenę za 1kg bananów w złotówkach: "))
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

while True:
    try:
        ilosc_bananow = float(input("Powiedz ile kg bananów chcesz kupic: "))
        break
    except ValueError:
        print("Niewłaściwa wartość, spróbuj ponownie.")

rachunek_za_ziemniaki = cena_ziemniakow_3 * ilosc_ziemniakow_3
rachunek_za_banany = cena_bananow * ilosc_bananow
if rachunek_za_ziemniaki > rachunek_za_banany:
    print(f"""Za podane ilości ziemniaków i bananów trzeba zapłacić 
{rachunek_za_ziemniaki + rachunek_za_banany}zł, przy czym droższe będą ziemniaki""")
elif rachunek_za_banany > rachunek_za_ziemniaki:
    print(f"""Za podane ilości ziemniaków i bananów trzeba zapłacić
{rachunek_za_ziemniaki + rachunek_za_banany}zł, przy czym droższe będą banany""""")
elif rachunek_za_banany == rachunek_za_ziemniaki:
    print(f"""Za podane ilości ziemniaków i bananów trzeba zapłacić 
{rachunek_za_ziemniaki + rachunek_za_banany}zł, przy czym obydwa towary wyjdą tyle samo""")



