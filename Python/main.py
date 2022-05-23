from ast import While
import string
from sys import implementation
import sqlite3
from telnetlib import TM
from tkinter.tix import Tree

con=sqlite3.connect("urunler.db")
cursor=con.cursor()

def yazdir():
    while True:
        try:
            secim=int(input("Lutfen istediğiniz telefonun etiketini giriniz: "))
            break
        except ValueError as hata:
            print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
    print("\n")
    t=0
    while True:
        t=t+1
        if t==secim:
            print("  |","-"*120,"|",sep="")
            print("  |Seçtiğiniz ürün: ",end="")
            cursor.execute("SELECT * FROM urunlertum WHERE etiket=={}".format(secim))
            data=cursor.fetchall()
            for i in data:
                print("|",i)
                print("  |","-"*120,"|",sep="")
            while True:
                fiyat=input("Ürünün diğer sitelerdeki fiyatlarını görmek istermisiniz?(E-e/H-h) ")
                print("\n")
                if (fiyat == "E" or fiyat == "e"):
                    cursor.execute("SELECT * FROM site_fiyat WHERE etiket=={}".format(secim))          
                    data1=cursor.fetchall()
                    for i in data1:
                        print("  |","-"*102,"|",sep="")   
                        print("  |",i,"|")
                        print("  |","-"*102,"|",sep="")
                    break
                elif (fiyat == "H" or fiyat == "h"):
                    break
                else:
                    print("Lütfen geçerli bir girdi giriniz!")
            print("\n")
            break

#Sisteme giriş kısmı
while True:
    giris=input("""
    Giriş yapmak için bas               : G-g
    Kayıt olmak için bas                : K-k
    Misafir olarak devam etmek için bas : M-m
    Seçiminiz: """ )
    if giris == "G" or giris == "g":
        ad = input("Kullanıcı adı: ")
        cursor.execute("SELECT * FROM kayitliKullanici WHERE ad == '{}'".format(ad))
        data = cursor.fetchone()
        if data != None:
            while True:
                sifre = input("Şifre: ")
                cursor.execute("SELECT * FROM kayitliKullanici WHERE sifre == '{}'".format(sifre))
                data = cursor.fetchone()
                if data != None:
                    print("Giriş başarılı\n")
                    break
                elif data == None:
                    print("Şifre yanlış")
                    secim = input("Tekrar denemek için 'T/t' basın\nDiğer giriş seçeneklerini görmek için 'D/d' basın\nSeçiminiz: ")
                    if secim == "T" or secim == "t":
                        continue
                    elif secim == "D" or secim == "d":
                        break
                    else:
                        print("Yanlış bir değer girdiniz şifre girme alanına yönlendiriliyorsunuz...")
            break
        elif data == None:
            print("Kullanıcı adı yanlış, lütfen tekrar deneyin!")
    elif giris == "K" or giris =="k":
        kayit = []
        ad = input("Lütfen bir kullanıcı adı belirleyiniz: ")
        cursor.execute("SELECT * FROM kayitliKullanici WHERE ad == '{}'".format(ad))
        data = cursor.fetchone()
        if data != None:
            print("Kullanıcı adı kayıtlı lütfen giriş yapınız.")
        elif data == None:
            while True:
                sifre = input("Lütfen şifre belirleyiniz: ")
                sifreOnay = input("Lütfen şifrenizi tekrar giriniz: ")
                if sifre == sifreOnay:
                    kayit += [(ad,sifre)]
                    for i in kayit:
                        cursor.execute("INSERT INTO kayitliKullanici VALUES(?,?)",i)
                        con.commit()
                        con.close()
                        print("Kayıt başarılı giriş yapabilirsiniz.")
                    con = sqlite3.connect("urunler.db")
                    cursor = con.cursor()
                    break
                elif sifre != sifreOnay:
                    print("Şifreler eşleşemedi lütfen tekrar deneyiniz")
    elif giris == "M" or giris == "m":
        print("Yönlendiriliyorsunuz...\n")
        break
    else:
        print("Lütfen geçerli bir değer giriniz")
#sisteme giriş yapıldı

#ürün listelenme kısmı
while(True):
    print("  |","-"*47,"ÜRÜNLER","-"*48,"|",sep="")
    cursor.execute("SELECT * FROM urunler")
    data=cursor.fetchall()
    x=1
    for i in data:
        print("  |","-"*102,"|",sep="")
        print(x,"|",i)
        print("  |"," "*102,"|",sep="")
        x=x+1
    print("  |","-"*102,"|",sep="")
#Filtreleme kısmı
    filtre=input("Tercihlerinize göre filtre uygulamak istermisiniz(E-e/H-h): ")
    print("\n")
    if(filtre=="E" or filtre=="e"):
        while True:
            print("""Lütfen iki filtreden birini seçiniz!
            1-FİYAT
            2-DEPOLAMA ALANI\n""")
            while True:
                try:
                    filtre_Secim=int(input("Seçtiğiniz seçeneğin numarasını giriniz: "))
                    break
                except ValueError as hata:
                    print("Lütfen rakam giriniz\nHata mesajı: {}".format(hata))
            if filtre_Secim==1:
                while True:
                    while True:
                        try:
                            filtre_Fiyat_Bas = int(input("İstediğiniz fiyat aralığının başlangıç değerini giriniz: "))
                            break
                        except ValueError as hata:
                            print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
                    while True:
                        try:
                            filtre_Fİyat_Son = int(input("İstediğiniz fiyat aralığının bitiş değerini giriniz: "))
                            break
                        except ValueError as hata:
                            print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
                    cursor.execute("SELECT * FROM urunler WHERE fiyat>={} and fiyat<={}".format(filtre_Fiyat_Bas , filtre_Fİyat_Son))
                    data=cursor.fetchall()
                    x=1
                    for i in data:
                        print("  |","-"*102,"|",sep="")
                        print(x,"|",i)
                        print("  |"," "*102,"|",sep="")
                        x=x+1
                    print("  |","-"*102,"|",sep="")
                    #2.Filtre kısmı
                    while True:
                        baska_filtre=input("Başka filtre uygulamak istermisiniz?(E-e/H-h) ")
                        if baska_filtre == "E" or baska_filtre == "e":
                            print(""""
                            1-FİYAT / Uygulandı tekrar uygulanamaz
                            2-DEPOLAMA ALANI\n""")
                            while True:
                                while True:
                                    try:
                                        baska_filtre_secim = int(input("Uygulanacak filtrenin numarasını giriniz: "))
                                        break
                                    except ValueError as hata:
                                        print("Lütfen rakam giriniz\nHata mesajı: {}".format(hata))
                                if baska_filtre_secim == 1:
                                    print("Bu filtre zaten uygulanmış tekrar uygulanamaz!")
                                    continue
                                elif baska_filtre_secim == 2:
                                    while True:
                                        while True:
                                            try:
                                                baska_filtre_rom = int(input("İstediğiniz depolama alanının değerini 'GB' cinsinden giriniz: "))
                                                break
                                            except ValueError as hata:
                                                print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
                                        while True:
                                            cursor.execute("SELECT * FROM urunler WHERE depolama == {} and fiyat >= {} and fiyat <= {}".format(baska_filtre_rom , filtre_Fiyat_Bas , filtre_Fİyat_Son))
                                            data = cursor.fetchall()
                                            x=1
                                            for i in data:
                                                print("  |","-"*102,"|",sep="")
                                                print(x,"|",i)
                                                print("  |"," "*102,"|",sep="")
                                                x=x+1
                                            print("  |","-"*102,"|",sep="")
                                            yazdir()
                                            uygulu_filtre_yeni_urun = input("Uygulanmış filtrelere göre başka bir telefon incelemek istermisiniz?(E-e/H-h) ")
                                            if uygulu_filtre_yeni_urun == "E" or uygulu_filtre_yeni_urun == "e":
                                                continue
                                            elif uygulu_filtre_yeni_urun == "H" or uygulu_filtre_yeni_urun == "h":
                                                break
                                        yeni_baska_filtre_rom = input("Tekrar ek 'Rom' filtresi uygulamak istiyormusunuz?(E-e/H-h) ")
                                        if yeni_baska_filtre_rom == "E" or yeni_baska_filtre_rom == "e":
                                            continue
                                        elif yeni_baska_filtre_rom == "H" or yeni_baska_filtre_rom == "h":
                                            break
                                else:
                                    print("Lütfen geçerli bir değer giriniz!")
                                break
                            break
                        elif baska_filtre == "H" or baska_filtre == "h":
                            yazdir()
                            uygulu_filtre_yeni_urun = input("Uygulanmış filtrelere göre başka bir telefon incelemek istermisiniz?(E-e/H-h) ")
                            if uygulu_filtre_yeni_urun == "E" or uygulu_filtre_yeni_urun == "e":
                                continue
                            elif uygulu_filtre_yeni_urun == "H" or uygulu_filtre_yeni_urun == "h":
                                break
                            else:
                                print("Lütfen geçerli bir değer giriniz")
                    yeni_filtre_fiyat = input("Yeni bir fiyat filtresi uygulamak istermisiniz?(E-e/H-h) ")
                    if yeni_filtre_fiyat == "E" or yeni_filtre_fiyat == "e":
                        continue
                    elif yeni_filtre_fiyat == "H" or yeni_filtre_fiyat == "h":
                        break
            elif filtre_Secim==2:
                while True:
                    while True:
                        try:
                            filtre_Rom = int(input("Uygulamak istediğiniz depolama alanını GB cinsinden giriniz: "))
                            break
                        except ValueError as hata:
                            print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
                    cursor.execute("SELECT * FROM urunler WHERE depolama = {}".format(filtre_Rom))
                    data = cursor.fetchall()
                    x = 1
                    for i in data:
                        print("  |","-"*102,"|",sep="")
                        print(x,"|",i)
                        print("  |"," "*102,"|",sep="")
                        x=x+1
                    print("  |","-"*102,"|",sep="")
                    while True:
                        baska_filtre=input("Başka filtre uygulamak istermisiniz?(E-e/H-h) ")
                        if baska_filtre == "E" or baska_filtre == "e":
                            print(""""
                            1-FİYAT
                            2-DEPOLAMA ALANI / Uygulandı tekrar uygulanamaz!\n""")
                            while True:
                                while True:
                                    try:
                                        baska_filtre_secim = int(input("Uygulanacak filtrenin numarasını giriniz: "))
                                        break
                                    except ValueError as hata:
                                        print("Lütfen sadece rakam giriniz\nHata mesajı: {}".format(hata))
                                if baska_filtre_secim == 1:
                                    while True:
                                        while True:
                                            try:
                                                baska_filtre_fiyat_bas = int(input("İstediğiniz fiyat aralığının başlangıç değerini giriniz: "))
                                                break
                                            except ValueError as hata:
                                                print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
                                        while True:
                                            try:
                                                baska_filtre_fiyat_son = int(input("İstediğiniz fiyat aralığının son değerini giriniz: "))
                                                break
                                            except ValueError as hata:
                                                print("Lütfen sadece sayı giriniz\nHata mesajı: {}".format(hata))
                                        while True:
                                            cursor.execute("SELECT * FROM urunler WHERE depolama == {} and fiyat >= {} and fiyat <= {}".format(filtre_Rom , baska_filtre_fiyat_bas, baska_filtre_fiyat_son))
                                            data = cursor.fetchall()
                                            x=1
                                            for i in data:
                                                print("  |","-"*102,"|",sep="")
                                                print(x,"|",i)
                                                print("  |"," "*102,"|",sep="")
                                                x=x+1
                                            print("  |","-"*102,"|",sep="")
                                            yazdir()
                                            uygulu_filtre_yeni_urun = input("Uygulanmış filtrelere göre başka bir telefon incelemek istermisiniz?(E-e/H-h) ")
                                            if uygulu_filtre_yeni_urun == "E" or uygulu_filtre_yeni_urun == "e":
                                                continue
                                            elif uygulu_filtre_yeni_urun == "H" or uygulu_filtre_yeni_urun == "h":
                                                break
                                        yeni_baska_filtre_rom = input("Tekrar ek fiyat filtresi uygulamak istiyormusunuz?(E-e/H-h) ")
                                        if yeni_baska_filtre_rom == "E" or yeni_baska_filtre_rom == "e":
                                            continue
                                        elif yeni_baska_filtre_rom == "H" or yeni_baska_filtre_rom == "h":
                                            break
                                elif baska_filtre_secim == 2:
                                    print("Bu filtre zaten uygulanmış tekrar uygulanamaz!")
                                    continue
                                else:
                                    print("Lütfen geçerli bir değer giriniz!")
                                break
                            break
                        elif baska_filtre == "H" or baska_filtre == "h":
                            yazdir()
                            uygulu_filtre_yeni_urun = input("Uygulanmış filtrelere göre başka bir telefon incelemek istermisiniz?(E-e/H-h) ")
                            if uygulu_filtre_yeni_urun == "E" or uygulu_filtre_yeni_urun == "e":
                                continue
                            elif uygulu_filtre_yeni_urun == "H" or uygulu_filtre_yeni_urun == "h":
                                break
                            else:
                                print("Lütfen geçerli bir değer giriniz")
                    yeni_filtre_depolama = input("Yeni bir depolama filtresi uygulamak istermisiniz?(E-e/H-h) ")
                    if yeni_filtre_depolama == "E" or yeni_filtre_depolama == "e":
                        continue
                    elif yeni_filtre_depolama == "H" or yeni_filtre_depolama == "h":
                        break
            else:
                print("Lütfen doğru bir girdi giriniz!")
            tekrar_filtre = input("Tekrar bir filtre uygulamak istermisiniz?(E-e/H-h) ")
            if tekrar_filtre == "E" or tekrar_filtre == "e":
                continue
            elif tekrar_filtre == "H" or tekrar_filtre == "h":
                break
        farkli_urun=input("Farklı bir telefon incelemek istermisini?(E-e/H-h) ")
        print("\n")
        if farkli_urun=="E" or farkli_urun=="e":
            continue
        elif farkli_urun=="H" or farkli_urun == "h":
            break
    elif(filtre == "H" or filtre == "h"):
        yazdir()
        farkli_urun=input("Başka telefon incelemek istermisiniz?(E-e/H-h)")
        if farkli_urun == "E" or farkli_urun == "e":
            print("\n")
        elif farkli_urun == "H" or farkli_urun == "h":
            break
        else:
            print("Lütfen geçerli bir değer giriniz!")
    else:
        print("Geçerli bir girdi giriniz!\n")
