import psycopg2
import hasla
import csv

conn = psycopg2.connect(
    host="localhost",
    database="ogloszenia",
    user="postgres",
    password=hasla.haslo_postgres
)

cur = conn.cursor()
cur.execute('select * from ogloszenia')
ogloszenia = cur.fetchall()
print(ogloszenia)

with open('ogloszenia.csv', 'w') as plik:
    dane = csv.writer(plik)
    dane.writerow(["id", "title", "price", "year", "first_name", "last_name", "email", "phone"])
    for row in ogloszenia:
        dane.writerow(row)
