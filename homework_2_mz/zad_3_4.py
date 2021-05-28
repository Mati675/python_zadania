'''
Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego oraz końcowego:

Przykład użycia:

> przytnij( data=[1, 2, 3, 4, 5, 6, 7],

        start=lambda x: x > 3,

        stop=lambda x: x == 6,  )
[4, 5, 6]
'''

def przytnij(lista: list, start=lambda x: x == 2, stop=lambda x: x == 5)-> list:
    """
    funkcja przycina listę na podstawie podanych warunków początkowego
    i końcowego
    :param lista:
    :param start:
    :param stop:
    :return:
    """

    wynik = []
    poziom = 0
    for element in lista:
        if element ==  start:
            poziom += 1
        elif element == stop:
            poziom -= 1
            wynik.append(element)
        if poziom == 1:
            wynik.append(element)
    return wynik


def test_przytnij():
    assert przytnij([1, 2, 3, 4, 5, 6], 2, 5) == [2, 3, 4, 5]


def test_przytnij_2():
    assert przytnij(["a", "b", "c", "d", "e", "f", "g"], "b", "f") == ["b", "c", "d", "e", "f"]
