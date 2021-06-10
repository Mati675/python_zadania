'''
Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty:
predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).

Dodaj do klasy `Pociag` metode `opis`.
Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam).
Mam jeszcze (ileś tam) litrów paliwa." Dodatkowo zaimplementuj metodę `__str__`.

Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący,
o ile ma zwiekszyć się prędkość. Ta metoda niech zwiększa predkość pociągu o tyle,
ile jest powiedziane w argumencie.
I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.

Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75%
(jeśli ktoś spróbuje tak zwiększyć prędkość, prędkość niech pozostaje po prostu bez zmian).
Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa
(jeśli ktoś spróbuje zwiększyć prędkość, kiedy nie ma paliwa, prędkość niech pozostaje
po prostu bez zmian).

Przetestuj swoje rozwiązanie i napisz testy, w których:
- zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
'''


class Pociag:
    predkosc = 10
    ilosc_paliwa = 1000


    def przyspiesz(self, przyspieszenie_o: float):
        """
        definiuję o ile pociąg ma przyspieszyc
        :param przyspieszenie_o:
        :return:
        """
        if isinstance(przyspieszenie_o, float) or isinstance(przyspieszenie_o, int):
            if Pociag.ilosc_paliwa > 0 and przyspieszenie_o <= Pociag.predkosc * 0.75:
                Pociag.ilosc_paliwa -= przyspieszenie_o * (Pociag.predkosc / 100)
                Pociag.predkosc += przyspieszenie_o
            else:
                pass
        else:
            print("Złe dane")


    def __str__(self):
        """
        zwracam opis sytuacji
        :return:
        """
        return f"Moja predkosc to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrow paliwa."




def test_pociag_1():
    pociag = Pociag()
    pociag.przyspiesz(5)
    assert pociag.__str__() == "Moja predkosc to 15. Mam jeszcze 999.5 litrow paliwa."


def test_pociag_2():
    pociag = Pociag()
    pociag.przyspiesz(20)
    assert pociag.__str__() == "Moja predkosc to 10. Mam jeszcze 1000 litrow paliwa."


def test_pociag_3():
    pociag = Pociag()
    pociag.przyspiesz(8)
    assert pociag.__str__() == "Moja predkosc to 10. Mam jeszcze 1000 litrow paliwa."


def test_pociag_4():
    pociag = Pociag()
    pociag.przyspiesz(10)
    assert pociag.__str__() == "Moja predkosc to 10. Mam jeszcze 1000 litrow paliwa."












