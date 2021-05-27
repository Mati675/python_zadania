'''
Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik
BMI, oraz podsumowanie informujące o stanie/zaleceniach.
(Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
'''

while True:
    try:
        wzrost = float(input("Podaj swoj wzrost w m: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

while True:
    try:
        waga = float(input("Podaj swoją wagę w kg: "))
        break
    except ValueError:
        print("Złe dane, spróbuj ponownie")

bmi = waga / (wzrost**2)

if bmi < 18.5:
    print(f"Twoje BMI wynosi {bmi} i masz niedowagę, jedz więcej")
elif 18.5 <= bmi < 25:
    print(f"Twoje BMI wynosi {bmi} i masz odpowiednią wagę względem wzrostu, rób to co dotychczas")
elif 25 <= bmi < 30:
    print(f"Twoje BMI wynosi {bmi} i masz nadwagę, jedz nieco mniej, zacznij ćwiczyć, albo obydwa")
elif 30<= bmi < 35:
    print(f"Twoje BMI wynosi {bmi} i masz otyłość, jedz mniej i zacznij ćwiczyć")
else:
    print(f"Twoje BMI wynosi {bmi} i masz skrajną otyłość, jedz znacznie mniej i zacznij intensywnie ćwiczyć")
