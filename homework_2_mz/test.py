'''
Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego
oraz końcowego:

Przykład użycia:

> przytnij( data=[1, 2, 3, 4, 5, 6, 7],

        start=lambda x: x > 3,

        stop=lambda x: x == 6,  )
[4, 5, 6]
'''


def przytnij(lista: list, start=lambda x: x == 2, stop=lambda x: x == 6)-> list:
    """
    funkcja przycina listę na podstawie podanych warunków początkowego
    i końcowego
    :param lista:
    :param start:
    :param stop:
    :return:
    """

    wynik = []



print(przytnij([1, 2, 3, 4, 5, 6]))
