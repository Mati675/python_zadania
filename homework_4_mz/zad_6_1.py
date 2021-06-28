import urllib.request
import json
import re

while True:
    while True:
        miasto = input("Podaj miasto, w przypadku dwoch czlonow oddziel je srednikiem: ").lower()
        if re.match(r"[a-zA-Z];[a-zA-Z]", miasto) or re.match(r"[a-zA-Z]", miasto):
            break
        else:
            print("Zle dane sprobuj ponownie.")

    with urllib.request.urlopen(f'https://www.metaweather.com/api/location/search/?query={miasto}') as response:
        dane = response.read()
        dane = json.loads(dane)

    if dane == []:
        print("Nie ma takiego miasta w bazie")
    else:
        break

woeid = dane[0]['woeid']

with urllib.request.urlopen(f'https://www.metaweather.com/api/location/{woeid}/') as response:
    dane = response.read()
    dane = json.loads(dane)
    print(dane)
