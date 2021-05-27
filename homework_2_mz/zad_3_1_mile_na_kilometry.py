
def mile_na_kilometry():
    """
    przelicza mile na kilometry
    :return:
    """
    while True:
        try:
            odleglosc = float(input("Podaj odległość w milach: "))
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")

    return round(odleglosc * 1.609344, 2)

print(mile_na_kilometry())