from csv import reader, writer
# tworzê nowy plik csv z wartoœciami oddzielonymi przecinkami
#¿eby da³o siê go skonwertowaæ na listê list w pythonie
reader = reader(open("zawodnicy.csv", "r", encoding='utf-8'), delimiter=';')
writer = writer(open("zawodnicy2.csv", 'w'), delimiter=',')
writer.writerows(reader)
