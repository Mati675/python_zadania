
def bmi():
    """
    zwraca współczynnik bmi
    :return:
    """
    while True:
        try:
            wzrost = float(input("Podaj wzrost w metrach:"))
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")

    while True:
        try:
            waga = float(input("Podaj wagę w kilogramach:"))
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")

    return round(waga / wzrost ** 2, 2)

print(bmi())