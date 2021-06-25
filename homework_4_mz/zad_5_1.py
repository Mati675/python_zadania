'''
Plik CSV z danymi: https://students.alx.pl/~pgradzinski/kpython/zawodnicy.csv

Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują
ten plik i:

1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.

2. liczy ile łącznie ważą reprezentanci Polski
(np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)).
Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).

3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn.
ma się wypisać, być może w innej kolejności:

AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
4. jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników.
'''
from csv import reader, writer

with open("zawodnicy2.csv") as plik:
    #poniżej zamieniam plik csv na listę list
    skoczkowie = list(reader(plik))

for element in skoczkowie:
    #usuwam puste linijki z pliku csv
    if element == []:
        skoczkowie.remove(element)

najwyzszy = 0
najnizszy = 0
najciezszy = 0
najlzejszy = 0

#poniżej sprawdzam którzy skoczkowie spełniają kryteria zadania
for element in skoczkowie:
    if int(element[4]) > najwyzszy:
        #najpierw znajduję najwyżsy wzrost
        najwyzszy = int(element[4])
for element in skoczkowie:
    #następnie dodaję do zmiennej skoczka o tym wzroście
    if int(element[4]) == najwyzszy:
        najwyzszy = element

#kolejne 3 pętle analogicznie do powyższej
for element in skoczkowie:
    if int(element[4]) < najnizszy or najnizszy == 0:
        najnizszy = int(element[4])
for element in skoczkowie:
    if int(element[4]) == najnizszy:
        najnizszy = element


for element in skoczkowie:
    if int(element[5]) > najciezszy:
        najciezszy = int(element[5])
for element in skoczkowie:
    if int(element[5]) == najciezszy:
        najciezszy = element


for element in skoczkowie:
    if int(element[5]) < najlzejszy or najlzejszy == 0:
        najlzejszy = int(element[5])
for element in skoczkowie:
    if int(element[5]) == najlzejszy:
        najlzejszy = element

print(najwyzszy)
print(najnizszy)
print(najciezszy)
print(najlzejszy)

while True:
    #proszę użytkownika o podanie kraju, upewniając się że poda włąściwy
    kraj = input("Podaj kraj skoczka, wybierz z opcji: POL, GER, FIN, AUT, NOR, USA: ")
    if kraj.upper() in "POL, GER, FIN, AUT, NOR, USA":
        break
    else:
        print("Złe dane, spróbuj ponownie")

laczna_waga = 0

for element in skoczkowie:
    #znajduję graczy z podanego kraju i dodaję ich wagi do łącznej wagi
    if element[2] == kraj.upper():
        laczna_waga += int(element[5])

print(f"Laczna waga skoczkow z kraju {kraj.upper()} wynosi {laczna_waga}kg.")

#dla wszystkich krajów oblicza ilu jest zawodników z tego kraju
#jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników.

kraje = set()
#tworzę listę krajów, upewniając się że sie one nie powtórzą
for element in skoczkowie:
    kraje.add(element[2])
kraje = list(kraje)

for kraj in kraje:
    #tworzę zmienne o nawie kraju, z początkową wartością 0
    globals()[kraj] = 0
    for element in skoczkowie:
        #zwiększam ilosć graczy w kraju
        if element[2] == kraj:
            globals()[kraj] += 1
    print(f"Ilosc skoczków z kraju {kraj} to {globals()[kraj]}")


for kraj in kraje:
    #tworzę zmienne o nawie kraju, z początkową wartością 0
    globals()[kraj] = 0
    globals()[f"sredni_wzrost{kraj}"] = 0
    for element in skoczkowie:
        #zwiększam ilość graczy w kraju i ich sumaryczny wzrost
        if element[2] == kraj:
            globals()[kraj] += 1
            globals()[f"sredni_wzrost{kraj}"] += int(element[4])
    #liczę średni wzrost skoczków z danego kraju w oparciu o uzyskane dane
    globals()[f"sredni_wzrost{kraj}"] /= globals()[kraj]
    globals()[f"sredni_wzrost{kraj}"] = round(globals()[f"sredni_wzrost{kraj}"], 2)
    print(f'Sredni wzrost skoczków z kraju {kraj} to {globals()[f"sredni_wzrost{kraj}"]}')








