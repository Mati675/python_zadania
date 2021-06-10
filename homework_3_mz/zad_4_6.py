'''
Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.

Ma ona mieć metody:

`dodaj_element(x: int, y: int, rodzaj_elementu)`

W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"o"`.
Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.

`stan_gry()`

Ta metoda ma zwracać liczbę oznaczającą stan gry
(gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).

`czyj_ruch()`

Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).

Wyświetlenie obiektu tej klasy ma wypisać planszę.

Użyj tej klasy do zrobienia gry w kółko i krzyżyk.
'''

class PlanszaXO:
    def __init__(self):
        self.stan_planszy = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def dodaj_element(self, x: int, y: int, rodzaj_elementu: str):
        """
        funkcja umieszcza okreslony element na konkretnych indeksach w stanie planszy
        :param x:
        :param y:
        :param rodzaj_elementu:
        :return:
        """
        if rodzaj_elementu.lower() not in "x, o":
            return False
        elif not 0 <= x <= 2 or not 0 <= y <= 2:
            return False
        elif self.stan_planszy[y][x] is not None:
            return False
        elif self.stan_gry() != 0:
            return False
        else:
            self.stan_planszy[y][x] = rodzaj_elementu

    def stan_gry(self):
        x_wygralo = 1
        o_wygralo = -1
        gra_trwa = 0

        if self.stan_planszy[0] == ["x", "x", "x"] or\
        self.stan_planszy[1] == ["x", "x", "x"] or \
        self.stan_planszy[2] == ["x", "x", "x"] or \
        (self.stan_planszy[0][0] == "x" and self.stan_planszy[1][0] == "x" \
        and self.stan_planszy[2][0] == "x") or \
        (self.stan_planszy[0][1] == "x" and self.stan_planszy[1][1] == "x" \
        and self.stan_planszy[2][1] == "x") or \
        (self.stan_planszy[0][2] == "x" and self.stan_planszy[1][2] == "x" \
        and self.stan_planszy[2][2] == "x") or \
        (self.stan_planszy[0][0] == "x" and self.stan_planszy[1][1] == "x" \
        and self.stan_planszy[2][2] == "x") or \
        (self.stan_planszy[0][2] == "x" and self.stan_planszy[1][1] == "x" \
        and self.stan_planszy[2][0] == "x"):
            return x_wygralo

        elif self.stan_planszy[0] == ["o", "o", "o"] or\
        self.stan_planszy[1] == ["o", "o", "o"] or \
        self.stan_planszy[2] == ["o", "o", "o"] or \
        (self.stan_planszy[0][0] == "o" and self.stan_planszy[1][0] == "o" \
        and self.stan_planszy[2][0] == "o") or \
        (self.stan_planszy[0][1] == "o" and self.stan_planszy[1][1] == "o" \
        and self.stan_planszy[2][1] == "o") or \
        (self.stan_planszy[0][2] == "o" and self.stan_planszy[1][2] == "o" \
        and self.stan_planszy[2][2] == "o") or \
        (self.stan_planszy[0][0] == "o" and self.stan_planszy[1][1] == "o" \
        and self.stan_planszy[2][2] == "o") or \
        (self.stan_planszy[0][2] == "o" and self.stan_planszy[1][1] == "o" \
        and self.stan_planszy[2][0] == "o"):
            return o_wygralo
        else:
            return gra_trwa


    def __str__(self):
        if self.stan_planszy.count("o") >= self.stan_planszy.count("x"):
            return ("Ruch krzyżyków")
        else:
            return ("Ruch kółek")




def test_plansza_1():
    plansza = PlanszaXO()
    plansza.dodaj_element(1, 1, "x")
    plansza.dodaj_element(2, 1, "o")
    plansza.dodaj_element(1, 2, "x")
    plansza.dodaj_element(2, 3, "o")
    assert plansza.__str__() == "Ruch krzyżyków"
    assert plansza.stan_gry() == 0


def test_plansza_2():
    plansza = PlanszaXO()
    assert plansza.dodaj_element(1, 5, "x") == False
    assert plansza.dodaj_element(1, 2, "r") == False


def test_plansza_3():
    plansza = PlanszaXO()
    plansza.dodaj_element(0, 0, "x")
    plansza.dodaj_element(1, 2, "o")
    plansza.dodaj_element(0, 1, "x")
    plansza.dodaj_element(2, 3, "o")
    plansza.dodaj_element(0, 2, "x")
    assert plansza.stan_planszy == [['x', None, None], ['x', None, None], ['x', 'o', None]]
    assert plansza.stan_gry() == 1










