'''

Napisz program wy�wietlaj�cy pogod� dla wskazanej przez u�ytkownika lokalizacji.

Skorzystaj z modu�u urllib.request, json oraz API MetaWeather.

===============================================================

Napisz program, kt�ry sprawdzi w wykazie podatnik�w VAT informacje o firmie
na podstawie jej numeru NIP.

https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat
'''

with urllib.request.urlopen(f'https://www.metaweather.com/api/location/{woeid}/') as response:
    dane = response.read()
    dane = json.loads(dane)
    print(dane)


#InvalidURL- b��d do excepta