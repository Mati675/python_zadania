from csv import reader, writer
# tworz� nowy plik csv z warto�ciami oddzielonymi przecinkami
#�eby da�o si� go skonwertowa� na list� list w pythonie
reader = reader(open("zawodnicy.csv", "r", encoding='utf-8'), delimiter=';')
writer = writer(open("zawodnicy2.csv", 'w'), delimiter=',')
writer.writerows(reader)
