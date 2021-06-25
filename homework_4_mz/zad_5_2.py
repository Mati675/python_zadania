

with open("pan_tadeusz.txt", encoding='utf-8') as plik:
    zawartosc = plik.read()
    print(zawartosc.count("Tadeusz"))