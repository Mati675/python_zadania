
while True:
    try:
        odleglosc = float(input("Podaj odległość w milach: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")


def mile_na_kilometry(odleglosc=odleglosc):
    """
    przelicza mile na kilometry
    :return:
    """

    return round(odleglosc * 1.609344, 2)

print(mile_na_kilometry())