import sqlite3


con=sqlite3.connect("urunler.db")
cursor=con.cursor()

#ÜRÜNLER
cursor.execute("CREATE TABLE IF NOT EXISTS urunler (ad TEXT, fiyat INT, depolama INT, puan TEXT, etiket TEXT)")

cursor.execute("INSERT INTO urunler VALUES ('Xiaomi Mi 9',6399,64,'73 Puan','#1')")
cursor.execute("INSERT INTO urunler VALUES ('Samsung Galaxy M31',6239,128,'62 Puan','#2')")
cursor.execute("INSERT INTO urunler VALUES ('Apple iPhone 12 Pro Max',23458,512,'90 Puan','#3')")
cursor.execute("INSERT INTO urunler VALUES ('Samsung Galaxy Note 9',10999,512,'77 Puan','#4')")


#TÜM ÖZELLİKLER
cursor.execute("CREATE TABLE IF NOT EXISTS urunlertum (ad TEXT, depolama TEXT, ekranboyut TEXT, bellek TEXT, batarya TEXT, kamera TEXT, cozunurluk TEXT, etiket TEXT)")

cursor.execute("""INSERT INTO urunlertum VALUES("Xiaomi Mi 9","64 GB","6.39 İnç","6 GB","3300 mAh","48 MP","1080x2340(FHD+)",1)""")
cursor.execute("""INSERT INTO urunlertum VALUES("Samsung Galaxy M31","128 GB","6.4 İnç","6 GB","6000 mAh","64 MP","1080x2340(FHD+)",2)""")
cursor.execute("""INSERT INTO urunlertum VALUES("Apple iPhone 12 Pro Max","512 GB","6.7 İnç","6 GB","3687 mAh","12 MP","1284x2778(FHD+)",3)""")
cursor.execute("""INSERT INTO urunlertum VALUES("Samsung Galaxy Note 9","512 GB","6.4 İnç","8 GB","4000 mAh","12 MP","1440x2960(QHD+)",4)""")


#SİTE FİYATLARI
cursor.execute("CREATE TABLE IF NOT EXISTS site_fiyat (etiket INT, site1fiyat TEXT, site2fiyat TEXT, site3fiyat TEXT)")

cursor.execute("""INSERT INTO site_fiyat VALUES("1","Hepsi Burada: 6399TL","N11: 6450TL","Amazon: 6899TL")""")
cursor.execute("""INSERT INTO site_fiyat VALUES("2","Hepsi Burada: 6489TL","N11: 6239TL","Amazon: 7109TL")""")
cursor.execute("""INSERT INTO site_fiyat VALUES("3","Hepsi Burada: 28655TL","N11: 23458TL","Amazon: 33000TL")""")
cursor.execute("""INSERT INTO site_fiyat VALUES("4","Hepsi Burada: 10999TL","N11: 11050TL","Amazon: 12300TL")""")


#İLK FİLTRE SONRASI TABLO
cursor.execute("""CREATE TABLE IF NOT EXISTS filtreList(ad TEXT, fiyat INT, depolama INT, puan TEXT, etiket TEXT)""")

#2. FİLTRE SONRASI TABLO
cursor.execute("CREATE TABLE IF NOT EXISTS filtreList2(ad TEXT, fiyat INT, depolama INT, puan TEXT, etiket TEXT)")


#KAYITLI KULLANICILAR
cursor.execute("CREATE TABLE IF NOT EXISTS kayitliKullanici(ad TEXT, sifre TEXT)")
cursor.execute("INSERT INTO kayitliKullanici VALUES('tunahannas', 'qwe123')")


con.commit()
con.close()

