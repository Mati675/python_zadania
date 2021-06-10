'''
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut:
`ilosc_wody` (z początkową wartością 0).

Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` \
i niech odpowiednio dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`.
Niech nie da się odlać więcej wody, niż jest w zbiorniku.

Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis
`zbiornik z (ileś tam) litrami wody`.

Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`.
Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający
temperaturę dolewanej wody. Dolanie wody do zbiornika powinno powodować zmianę
temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
'''

class Zbiornik:
    def __init__(self):
        """
        inicjuję atrybuty klasy Zbiornik
        :param ilosc_wody:
        """
        self.ilosc_wody = 0


    def dolej(self, ile: float):
        """
        definuję co się stanie gdy doleję wody do zbiornika
        :param ile:
        :return:
        """
        self.ilosc_wody += ile


    def odlej(self, ile: float):
        """
        definuję co się stanie gdy odleję wody ze zbiornika
        :param ile:
        :return:
        """
        if ile <= self.ilosc_wody:
            self.ilosc_wody -= ile


    def __str__(self):
        return f"Zbiornik z {self.ilosc_wody} litrami wody."



class Zbiornik:
    def __init__(self):
        """
        inicjuję atrybuty klasy Zbiornik, z jednym nowym
        :param ilosc_wody:
        """
        self.ilosc_wody = 0
        self.temperatura = 0

    def dolej(self, ile: float, temp: float):
        """
        defniuję jak zachowa się woda w zbiorniku po dolaniu, z uwzględnieniem temperatury
        :param ile:
        :param temp:
        :return:
        """
        self.temperatura = ((self.temperatura * self.ilosc_wody) + (ile * temp)) / (ile + self.ilosc_wody)
        self.ilosc_wody += ile


    def odlej(self, ile: float):
        if ile <= self.ilosc_wody:
            self.ilosc_wody -= ile


    def __str__(self):
        return f"Zbiornik z {self.ilosc_wody} litrami wody. Mam temperaturę {self.temperatura} stopni."



def test_zbiornik_1():
    """
    test prostego użycia obiektu klasy Zbiornik
    :return:
    """
    zbiornik = Zbiornik()
    zbiornik.dolej(10, 15)
    assert zbiornik.__str__() == "Zbiornik z 10 litrami wody. Mam temperaturę 15.0 stopni."


def test_zbiornik_2():
    """
    Test bardziej zaawansowanego użycia obiektu klasy Zbiornik
    :return:
    """
    zbiornik = Zbiornik()
    zbiornik.dolej(10, 15)
    zbiornik.dolej(10, 25)
    assert zbiornik.__str__() == "Zbiornik z 20 litrami wody. Mam temperaturę 20.0 stopni."







