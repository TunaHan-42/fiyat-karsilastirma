from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
import sqlite3
from numpy import kaiser
import pandas as pd

con = sqlite3.connect("urunler.db")
cursor = con.cursor()

sozluk = {}
ad = []
fiyat = []
depolama = []
puan = []
etiket = []

cursor.execute("SELECT ad FROM urunler")
data = cursor.fetchall()
for i in data:
    ad.append(i)

sozluk.setdefault("ad", ad)

cursor.execute("SELECT fiyat FROM urunler")
data = cursor.fetchall()
for i in data:
    fiyat.append(i)

sozluk.setdefault("fiyat", fiyat)

cursor.execute("SELECT depolama FROM urunler")
data = cursor.fetchall()
for i in data:
    depolama.append(i)

sozluk.setdefault("depolama", depolama)

cursor.execute("SELECT puan FROM urunler")
data = cursor.fetchall()
for i in data:
    puan.append(i)

sozluk.setdefault("puan", puan)

cursor.execute("SELECT etiket FROM urunler")
data = cursor.fetchall()
for i in data:
    etiket.append(i)

sozluk.setdefault("etiket", etiket)

df = pd.DataFrame(sozluk)
print(df)

