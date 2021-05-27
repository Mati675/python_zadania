'''
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.

​

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała
dłużej niż siedem dni.
'''

dni_tygodnia = {
    "poniedzialek" : 1,
    "wtorek" : 2,
    "sroda" : 3,
    "czwartek" : 4,
    "piatek" : 5,
    "sobota" : 6,
    "niedziela" : 7

}

while True:
    dzien_oddania_butow = input("Podaj dzień tygodnia oddania butów do szewca: ")
    if dzien_oddania_butow in dni_tygodnia.keys():
        break
    else:
        print("Złe dane, spróbuj ponownie")

while True:
    try:
        czas_naprawy = int(input("Podaj ilość dni jaką zajmie naprawa: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

dzien_gotowosci_butow = dni_tygodnia[dzien_oddania_butow] + czas_naprawy

if dzien_gotowosci_butow <= 7:
    print(f"Buty będą gotowe do odbioru {dzien_gotowosci_butow} dnia tygodnia")
else:
    print(f"Buty będą gotowe do odbioru {dzien_gotowosci_butow % 7} dnia tygodnia")

