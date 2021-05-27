'''
Napisz program obliczający średnią
wartość temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika.
'''

temperatury = []

for day in range(1, 8):
    while True:
        try:
            temperatura = float(input(f"Podaj temperaturę z {day} dnia tygodnia: "))
            temperatury.append(temperatura)
            break
        except ValueError:
            print("Złe dane, spróbuj ponownie")

print(f"Średnia temperatura w ciągu tygodnia wynosi: {sum(temperatury) / len(temperatury)}")