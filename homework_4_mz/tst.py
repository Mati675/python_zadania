'''

Napisz program wyœwietlaj¹cy pogodê dla wskazanej przez u¿ytkownika lokalizacji.

Skorzystaj z modu³u urllib.request, json oraz API MetaWeather.

===============================================================

Napisz program, który sprawdzi w wykazie podatników VAT informacje o firmie
na podstawie jej numeru NIP.

https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat
'''

with urllib.request.urlopen(f'https://www.metaweather.com/api/location/{woeid}/') as response:
    dane = response.read()
    dane = json.loads(dane)
    print(dane)


#InvalidURL- b³¹d do excepta