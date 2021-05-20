'''
Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.

na wejsciu: [49, 50, 20, 40, 35, 10]

na wyjsciu: [49, 10, 20, 40, 35, 50]
'''

lista = [49, 50, 20, 40, 35, 10]

max_listy = max(lista)
min_listy = min(lista)
pierwszy_index_max_listy = lista.index(max_listy)
del lista[lista.index(max_listy)]
lista.insert(lista.index(min_listy), max_listy)
del lista[lista.index(min_listy)]
lista.insert(pierwszy_index_max_listy, min_listy)

print(lista)
