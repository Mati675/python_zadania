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
    ZWYCIESTWO_KRZYZYKOW = False
    ZWYCIESTWO_KOLEK = False
    GRA_TRWA = True
    KRZYZYKI = []
    KOLKA = []

    def dodaj_element(self, x: int, y: int, rodzaj_elementu: str):
        """
        definiuj,e funkcję dodania elementy na planszę, planszą jest zmienna zajete pola
        :param y:
        :param rodzaj_elementu:
        :return:
        """
        zajete_pola = []
        krzyzyki = []
        kolka = []

        if rodzaj_elementu.lower() not in "x, o":
            return False
        elif (x, y) in zajete_pola or 1 < x < 3 or 1 < y < 3:
            return False

        elif rodzaj_elementu.lower() == "x":
            zajete_pola.append((x, y))
            krzyzyki.append((x, y))
            print(f"zajęte pola = {zajete_pola}")
            print(f"krzyżyki = {krzyzyki}")
        elif rodzaj_elementu.lower() == "o":
            zajete_pola.append((x, y))
            kolka.append((x, y))
            print(f"zajęte pola = {zajete_pola}")
            print(f"kółka = {kolka}")

        if (1, 1) in krzyzyki and (1, 2) in krzyzyki and (1, 3) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 1) in krzyzyki and (2, 1) in krzyzyki and (3, 1) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 1) in krzyzyki and (2, 2) in krzyzyki and (3, 3) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 2) in krzyzyki and (2, 2) in krzyzyki and (3, 2) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 3) in krzyzyki and (2, 3) in krzyzyki and (3, 3) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (2, 1) in krzyzyki and (2, 2) in krzyzyki and (2, 3) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (3, 1) in krzyzyki and (3, 2) in krzyzyki and (3, 3) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 3) in krzyzyki and (2, 2) in krzyzyki and (3, 1) in krzyzyki:
            PlanszaXO.ZWYCIESTWO_KRZYZYKOW = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 1) in kolka and (1, 2) in kolka and (1, 3) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 1) in kolka and (2, 1) in kolka and (3, 1) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 1) in kolka and (2, 2) in kolka and (3, 3) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 2) in kolka and (2, 2) in kolka and (3, 2) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 3) in kolka and (2, 3) in kolka and (3, 3) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (2, 1) in kolka and (2, 2) in kolka and (2, 3) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (3, 1) in kolka and (3, 2) in kolka and (3, 3) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False
        elif (1, 3) in kolka and (2, 2) in kolka and (3, 1) in kolka:
            PlanszaXO.ZWYCIESTWO_KOLEK = True
            PlanszaXO.GRA_TRWA = False

        PlanszaXO.KRZYZYKI = krzyzyki
        PlanszaXO.KOLKA = kolka


    def stan_gry(self):
        if PlanszaXO.ZWYCIESTWO_KOLEK == True:
            return 1
        elif PlanszaXO.ZWYCIESTWO_KRZYZYKOW == True:
            return -1
        else:
            return 0


    def czyj_ruch(self):
        if len(PlanszaXO.KRZYZYKI) < len(PlanszaXO.KOLKA):
            print("Ruch krzyżyków")
        else:
            print("Ruch kółek")


plansza = PlanszaXO()

plansza.czyj_ruch()
plansza.dodaj_element(1, 1, "o")
plansza.dodaj_element(2, 1, "x")
plansza.dodaj_element(1, 2, "o")
plansza.dodaj_element(2, 3, "x")
plansza.dodaj_element(1, 3, "o")
print(plansza.stan_gry())









