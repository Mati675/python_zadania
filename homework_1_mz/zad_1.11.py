'''
Napisz program obliczający średnią
wartość temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika.
'''

temperatury = (float(input("Podaj temperaturę z poniedziałku: ")), float(input("Podaj temperaturę z wtorku: ")),
float(input("Podaj temperaturę z srody: ")), float(input("Podaj temperaturę z czwartku: ")),
float(input("Podaj temperaturę z piątku: ")), float(input("Podaj temperaturę z soboty: ")),
float(input("Podaj temperaturę z niedzieli: ")))

print(sum(temperatury) / len(temperatury))