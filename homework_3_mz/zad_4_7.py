'''
Do zadania z klasą `Ogloszenie` dodaj kolejne klasy, które po niej dziedziczą.

`OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i 
dodatkowo określa cechy sprzedawanego samochodu jak model, 
markę, rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.

`OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, 
a dodatkowo cechy sprzedawanego mieszkania / domu: miejscowość, metraż, liczba pokoi.
'''

from zad_4_1 import Ogloszenia

class Ogloszenia_Samochodowe(Ogloszenia):
    """
    dziedziczę cechy klasy Ogloszenia do klasy Ogloszenia_Samochodowe
    """
    def __init__(self, tytul: str, cena: float, imie_sprzedawcy: str, nazwisko_sprzedawcy: str,
                 nr_tel: int, email: str, opis: str, model: str, marka: str,
                 rok_produkcji: int, przebieg: float, pojemnosc: float, moc: int, paliwo: str):
        """
        superem inicjuję te parametry pokrywające się z klasą rodzic
        :param tytul:
        :param cena:
        :param imie_sprzedawcy:
        :param nazwisko_sprzedawcy:
        :param nr_tel:
        :param email:
        :param opis:
        :param model:
        :param marka:
        :param rok_produkcji:
        :param przebieg:
        :param pojemnosc:
        :param moc:
        :param paliwo:
        """
        super().__init__(tytul, cena, imie_sprzedawcy, nazwisko_sprzedawcy,
                 nr_tel, email, opis)
        self.model = model
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.paliwo = paliwo


class Ogloszenia_Mieszkaniowe(Ogloszenia):
    def __init__(self, tytul: str, cena: float, imie_sprzedawcy: str, nazwisko_sprzedawcy: str,
                 nr_tel: int, email: str, opis: str, miejscowosc: str, metraz: float,
                 liczba_pokoi: int):
        """
        superem inicjuję te parametry pokrywające się z klasą rodzic
        :param tytul:
        :param cena:
        :param imie_sprzedawcy:
        :param nazwisko_sprzedawcy:
        :param nr_tel:
        :param email:
        :param opis:
        :param model:
        :param marka:
        :param rok_produkcji:
        :param przebieg:
        :param pojemnosc:
        :param moc:
        :param paliwo:
        """
        super().__init__(tytul, cena, imie_sprzedawcy, nazwisko_sprzedawcy,
                 nr_tel, email, opis)
        self.miejscowosc = miejscowosc
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi



def test_create_samochod():
    """
    testuję czy przekazywanie wartosci parametrow dziala
    :return:
    """
    samochod = Ogloszenia_Samochodowe("Auto", 2000, "Jan", "Kowalski", 123, "jan@mail.com", "Sprzedam auto",
                                      "Punto", "Fiat", 1998, 100000.5, 1.2, 75, "benzyna")
    assert samochod.paliwo == "benzyna"
    assert samochod.rok_produkcji == 1998


def test_create_mieszkanie():
    """
    testuję czy przekazywanie wartosci parametrow dziala
    :return:
    """
    mieszkanie = Ogloszenia_Mieszkaniowe("Mieszkanie", 400000, "Ala", "Kowalska",
                                         345, "ala@mail.com", "Sprzedam Mieszkanie", "Tychy", 50.3, 3)
    assert mieszkanie.email == "ala@mail.com"
    assert mieszkanie.metraz == 50.3