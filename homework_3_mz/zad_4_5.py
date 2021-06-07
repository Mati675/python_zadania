'''
Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie
(wyrażone dwiema współrzędnymi) i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).

Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.

Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.

Metoda `idz` powoduje przejście żółwia o określoną odległość.

Z klasy będzie się korzystać tak:

z = Zolw(100, 100)
z.idz(50)
print(z) # ma sie wypisac: x=100, y=50

z.obroc_sie(90)
z.idz(50)
print(z) # ma sie wypisac: x=150, y=50
'''

import math

class Zolw:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.kurs = 0


    def obroc_sie(self, obrot_o: float):
        """
        definuję funkcję obrócenia żółwia o ileś stopni
        :param obrot_o:
        :return:
        """
        if obrot_o < 360:
            self.kurs += obrot_o
        else:
            self.kurs += obrot_o % 360


    def idz(self, odleglosc):
        """
        definiuję funkcje idź z uwzględnieniem kursu zólwia
        :param odleglosc:z jego pomocą sinusów, i cosinusów kąta obliczam ile przesunie się
        obiekt po płaszczyznach x i y
        :return:
        """
        if self.kurs == 0:
            self.y += odleglosc
        elif self.kurs == 90:
            self.x += odleglosc
        elif self.kurs == 180:
            self.y -= odleglosc
        elif self.kurs == 270:
            self.x -= odleglosc
        elif 0 < self.kurs < 90:
            self.x += round(math.sin(math.radians(self.kurs)) * odleglosc, 2)
            self.y += round(math.cos(math.radians(self.kurs)) * odleglosc, 2)
        elif 90 < self.kurs < 180:
            self.x += round(math.cos(math.radians(self.kurs - 90)) * odleglosc, 2)
            self.y -= round(math.sin(math.radians(self.kurs - 90)) * odleglosc, 2)
        elif 180 < self.kurs < 270:
            self.x -= round(math.cos(math.radians(270 - self.kurs)) * odleglosc, 2)
            self.y -= round(math.sin(math.radians(270 - self.kurs)) * odleglosc, 2)
        elif 270 < self.kurs < 360:
            self.x -= round(math.sin(math.radians(360 - self.kurs)) * odleglosc, 2)
            self.y += round(math.cos(math.radians(360 - self.kurs)) * odleglosc, 2)


    def __str__(self):
        return f"x={self.x}, y={self.y}"



def test_zolw_1():
    """
    kilka testów na kąty obrotu obiektu z różnych zakresów do 360 stopni
    :return:
    """
    zolw = Zolw(0, 0)
    zolw.obroc_sie(30)
    zolw.idz(10)
    assert zolw.__str__() == "x=5.0, y=8.66"



def test_zolw_2():
    zolw = Zolw(0, 0)
    zolw.obroc_sie(100)
    zolw.idz(10)
    assert zolw.__str__() == "x=9.85, y=-1.74"


def test_zolw_3():
    zolw = Zolw(0, 0)
    zolw.obroc_sie(220)
    zolw.idz(10)
    assert zolw.__str__() == "x=-6.43, y=-7.66"


def test_zolw_4():
    zolw = Zolw(0, 0)
    zolw.obroc_sie(290)
    zolw.idz(10)
    assert zolw.__str__() == "x=-9.4, y=3.42"


def test_zolw_5():
    zolw = Zolw(0, 0)
    zolw.obroc_sie(90)
    zolw.idz(10)
    assert zolw.__str__() == "x=10, y=0"


def test_zolw_6():
    zolw = Zolw(0, 0)
    zolw.obroc_sie(270)
    zolw.idz(10)
    assert zolw.__str__() == "x=-10, y=0"


def test_zolw_6():
    """
    tym razem test na podany kąt powyżej 360 stopni
    :return:
    """
    zolw = Zolw(0, 0)
    zolw.obroc_sie(390)
    zolw.idz(10)
    assert zolw.__str__() == "x=5.0, y=8.66"




