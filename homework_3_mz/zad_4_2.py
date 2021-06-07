'''
Napisz programy, w których tworzysz listę ogłoszeń samochodowych,
a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.

Na przykład ogłoszenia o cenach z określonego przedziału.

Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
Użyj poznanych kolekcji do trzymania ogłoszeń.
Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.

'''

from zad_4_1 import Ogloszenia

ogloszenie_1 = Ogloszenia("Lamborghini Diablo", 300000, "Jan", "N",
                          123, "janek@mail.com", "Wspaniały włoski supersamochód który\n"
                                                   "wzbogaci Twojego mechanika")

ogloszenie_2 = Ogloszenia("Rolls Royce Python", 500000, "Ala", "K",
                          666, "ala@mail.com", "Specjalna wersja limuzyny dla koderów")

ogloszenie_3 = Ogloszenia("Aston Martin DB5",
                          2000000, "James", "B", 234, "jimmy@mail.com", "Piękny klasyk\n"
                                                                   " z wyrzutniami rakiet")

ogloszenia = [ogloszenie_1, ogloszenie_2, ogloszenie_3]



a = list(filter(lambda x: x.cena < 1000000, ogloszenia))

b = [element.tytul for element in a]

print(b)


