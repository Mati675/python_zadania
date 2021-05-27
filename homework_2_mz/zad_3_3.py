'''
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i
na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)

- `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji
`sum` wbudowanej w pythona
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji
`max` wbudowanej w pythona
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście;
`0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`,
które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą
od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe
niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`,
które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby`
liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno
w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma

'''

def suma(*args: float)-> float:
    """
    zwraca sumę podanych liczb
    :param args:
    :return:
    """

    wynik = 0
    for liczba in args:
        wynik += liczba
    return wynik


def test_suma():
    assert suma(3, 5, 10) == 18


def srednia(*args: float)-> float:
    """
    zwraca średnią z podanych liczb
    :param kwargs:
    :return:
    """

    liczby = []
    for liczba in args:
        liczby.append(liczba)
    return round(sum(liczby) / len(liczby), 2)


def test_srednia():
    assert srednia(2, 3, 5) == 3.33


def max_liczba(*args: float)-> float:
    """
    zwraca najwyższą z podanych liczb
    :param args:
    :return:
    """

    max_liczba = 0
    for liczba in args:
        if liczba > max_liczba:
            max_liczba = liczba
    return max_liczba

def test_max_liczba():
    assert max_liczba(1, 2, 3.5, 10, 0) == 10


def max_minus_min(*args: float) -> float:
    """
    zwraca różnicę pomiędzy największą i najmniejszą z podanych liczb
    :param args:
    :return:
    """

    if len(args) > 0:
        return round(max(args) - min(args), 2)
    else:
        return 0


def test_max_minus_min():
    assert max_minus_min(2, 3) == 1


def test_max_minus_min_2():
    assert max_minus_min() == 0


def wypisz_wieksze(*args: float, x: float)-> list:
    """
    wypisuje listę liczb większych od podanego x
    :param args:
    :param x:
    :return:
    """

    liczby_wieksze_od_x = [liczba for liczba in args if liczba > x]
    print(liczby_wieksze_od_x)
    return liczby_wieksze_od_x


def test_wypisz_wieksze():
    assert wypisz_wieksze(1, 2, 3, 4, x=2) == [3, 4]


def pierwsza_wieksza(*args: float, x: float)-> float:
    """
    zwraca pierwszą z podanych liczb większą od podanego x, albo None jeśli takiej nie ma
    :param args:
    :param x:
    :return:
    """

    for liczba in args:
        if liczba > x:
            return liczba


def test_pierwsza_wieksza():
    assert pierwsza_wieksza(1, 2, 3, 4, x=1.5) == 2


def test_pierwsza_wieksza_2():
    assert pierwsza_wieksza(1, 2, 3, 4, x=6) == None


def suma_wiekszych(*args: float, x: float)-> float:
    """
    zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
    :param args:
    :param x:
    :return:
    """

    liczby_wieksze_od_x = [liczba for liczba in args if liczba > x]
    return sum(liczby_wieksze_od_x)


def test_suma_wiekszych():
    assert suma_wiekszych(1, 2, 3, 4, x=2) == 7


def test_suma_wiekszych_2():
    assert suma_wiekszych(1, 2, 3, 4, x=6) == 0


def ile_wiekszych(*args: float, x: float)-> int:
    """
    liczy ile elementów listy `liczby` jest większych od liczby `x`
    :param args:
    :param x:
    :return:
    """

    liczby_wieksze_od_x = [liczba for liczba in args if liczba > x]
    return len(liczby_wieksze_od_x)


def test_ile_wiekszych():
    assert ile_wiekszych(1, 2, 3, 4, 5, x=2) == 3


def test_ile_wiekszych_2():
    assert ile_wiekszych(1, 2, 3, 4, 5, x=5) == 0


def wypisz_podzielne(*args: float, x: float)-> list:
    """
    wypisuje (`print`) wszystkie te liczby z listy `liczby`,
które są podzielne przez `x`
    :param args:
    :param x:
    :return:
    """

    podzielne_przez_x = [liczba for liczba in args if liczba % x == 0]
    print(podzielne_przez_x)
    return podzielne_przez_x


def test_wypisz_podzielne():
    assert wypisz_podzielne(2, 4, 5, 7, 8, 12, x=2) == [2, 4, 8, 12]


def pierwsza_podzielna(*args: float, x: float)-> float:
    """
    zwraca (`return`) pierwszą znalezioną w `liczby`
liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
    :param args:
    :param x:
    :return:
    """

    for liczba in args:
        if liczba % x == 0:
            return liczba


def test_pierwsza_podzielna():
    assert pierwsza_podzielna(1, 3, 4, 5, x=2.5) == 5


def test_pierwsza_podzielna_2():
    assert pierwsza_podzielna(1, 3, 4, 5, x=2.2) == None


def znajdz_wspolny(liczby_1: set, liczby_2: set)-> set:
    """
    zwraca element (liczbę), który występuje zarówno
w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
    :param liczby_1:
    :param liczby_2:
    :return:
    """

    wynik = liczby_1.intersection(liczby_2)
    if wynik == set():
        return None
    else:
        return wynik


def test_znajdz_wspolny():
    assert znajdz_wspolny({1, 2, 3, 4}, {3, 4, 5}) == {3, 4}

def test_znajdz_wspolny_2():
    assert znajdz_wspolny({1, 2, 3, 4}, {8, 6, 5}) == None
















