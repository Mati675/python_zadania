'''
Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia
(takie jak w serwisie internetowym z ogłoszeniami).

Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie,
m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.
'''


class Ogloszenia:
    def __init__(self, tytul: str, cena: float, imie_sprzedawcy: str, nazwisko_sprzedawcy: str,
                 nr_tel: int, email: str, opis: str):
        """
        definuję parametry klasy
        :param tytul:
        :param cena:
        :param imie_sprzedawcy:
        :param nazwisko_sprzedawcy:
        :param nr_tel:
        :param email:
        """
        self.tytul = tytul
        self.cena = cena
        self.imie_sprzedawcy = imie_sprzedawcy
        self.nazwisko_sprzedawcy = nazwisko_sprzedawcy
        self.nr_tel = nr_tel
        self.email = email
        self.opis = opis



def test_create():
    ogloszenie = Ogloszenia("Auto", 2000, "Jan", "Kowalski", 123, "jan@mail.com", "Sprzedam auto")
    assert ogloszenie.tytul == "Auto"
    assert ogloszenie.nazwisko_sprzedawcy == "Kowalski"