'''
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i
zwraca przeliczoną wartość.

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)

podpowiedź: wartość PI jest dostępna jako `Math.PI`

5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

​
Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.
'''

import math

def stopy_na_metry(odleglosc):
    """
    przelicza stopy na metry
    :return:
    """

    return round(odleglosc * 0.3048, 2)

def test_stopy_na_metry():
    assert stopy_na_metry(6.6) == 2.01




def max(a: float, b: float)-> float:
    """
    zwraca większą z podanych wartości
    :param a:
    :param b:
    :return:
    """

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Liczby są równe"


def test_max():
    assert max(2, 4) == 4


def test_max_2():
    assert max(1, 1) == "Liczby są równe"


def srednia(liczba_1: float, liczba_2: float)-> float:
    """
    zwraca srednią dwóch liczb
    :return:
    """

    return round((liczba_1 + liczba_2) / 2, 2)


def test_srednia():
    assert srednia(3.5, 5.5) == 4.5


def pole_kola(promien: float)-> float:
    return round(math.pi * promien ** 2, 2)


def test_pole_kola():
    assert pole_kola(3) == 28.27


def bmi(wzrost: float, waga: float)-> float:
    """
    zwraca współczynnik bmi
    :return:
    """

    return round(waga / wzrost ** 2, 2)


def test_bmi():
    assert bmi(1.9, 80) == 22.16


def pole_trojkata(bok_1: float, bok_2: float, bok_3: float)-> float:
    """
    zwraca pole trójkąta o podanych bokach
    :param bok_1:
    :param bok_2:
    :param bok_3:
    :return:
    """

    if bok_1 > 0 and bok_2 > 0 and bok_3 > 0:
        return round(math.sqrt((bok_1 + bok_2 + bok_3) * (bok_1 + bok_2 - bok_3)\
                * (bok_1 - bok_2 + bok_3) * (bok_2 + bok_3 - bok_1)) / 4, 2)


def test_pole_trojkata():
    assert pole_trojkata(2, 3, 4) == 2.9


def test_pole_trojkata_2():
    assert pole_trojkata(0, 2, 3) == None


def kilometry_na_mile(odleglosc: float)-> float:
    """
    przelicza kilometry na mile
    :param odleglosc:
    :return:
    """

    return round(odleglosc * 0.621371192, 2)


def test_kilometry_na_mile():
    assert kilometry_na_mile(100) == 62.14


def mile_na_kilometry(odleglosc: float)-> float:
    """
    przelicza mile na kilometry
    :param odleglosc:
    :return:
    """

    return round(odleglosc * 1.609344, 2)


def test_mile_na_kilometry():
    assert mile_na_kilometry(100) == 160.93



