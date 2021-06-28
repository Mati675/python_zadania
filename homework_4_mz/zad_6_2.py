import urllib.request
import json
import re

while True:

    nip = input("Podaj Nip firmy: ")
    data = input("Podaj date w formacie rrrr-mm-dd: ")

    if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", data) and re.match("\d{10}", nip):
        break
    else:
        print("Niewlasciwe dane, sprobuj ponownie.")

with urllib.request.urlopen(f'https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={data}') as response:
    dane = response.read()
    dane = json.loads(dane)
    print(dane)
    print(type(dane))
