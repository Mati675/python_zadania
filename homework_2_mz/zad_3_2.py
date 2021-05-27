'''
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.

Logikę obliczania liczby dni wydziel do osobnej funkcji.

**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty
był przestępny czy nie.

'''
import calendar

def ilosc_dni():
    """
    zwraca ilość dni w podanym miesiącu
    :return:
    """
    miesiace_po_30_dni = ["kwiecień", "czerwiec", "wrzesień", "listopad"]
    miesiace_po_31_dni = ["styczeń", "marzec", "maj", "lipiec", "sierpień", "październik", "grudzień"]
    while True:
        miesiac = input("Podaj miesiąc: ")
        if miesiac.lower() in miesiace_po_30_dni:
            return "Podany miesiac ma 30 dni"
            break
        elif miesiac.lower() in miesiace_po_31_dni:
            return "Podany miesiąc ma 31 dni"
            break
        elif miesiac.lower() == "luty":
            try:
                rok = int(input("Podaj rok: "))
                if calendar.isleap(rok):
                    return "Podany miesiąc ma 29 dni"
                    break
                else:
                    return "Podany miesiąc ma 28 dni"
                    break
            except ValueError:
                print("Złe dane, sprobuj ponownie")
        else:
            print("Złe dane, spróbuj ponownie")


print(ilosc_dni())


