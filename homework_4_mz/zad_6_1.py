
import urllib.request
import json
import requests



miasto = input("Podaj miasto, w przypadku dwoch czlonow oddziel je srednikiem: ").lower()

with urllib.request.urlopen(f'https://www.metaweather.com/api/location/search/?query={miasto}') as response:
    dane = response.read()
    dane = json.loads(dane)
    print(dane)
    print(type(dane))



woeid = dane[0]['woeid']

with urllib.request.urlopen(f'https://www.metaweather.com/api/location/{woeid}/') as response:
    dane = response.read()
    dane = json.loads(dane)
    print(dane)










