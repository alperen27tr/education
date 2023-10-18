#! /usr/bin/env python
#! _*_coding: UTF8 _*_
def topla(a,b):
    return a+b
sonuc0=topla(20,50)
sonuc1=topla(35,55)#35 ve 45 parametre oluyor.
print(sonuc0)
print(sonuc1)


def YasHesapla(dogumyili):
    return(2023-dogumyili)
sonuc=YasHesapla(2002)

print(sonuc)


def selamlama(isim):
    return str("Merhaba") + str(isim) 
    

aaa = input("değer girin") 
sonuc=selamlama(aaa)

print(sonuc)

def kayitolma(ad,soyad,sehir):
    print("isim:        ",aaa)
    print("soyisim:     ",soyad)
    print("şehir:       ",sehir)
    print("Kaydınız Tamamlandı..")
    
sonuc=kayitolma("salla","Erdoğan","Kayseri")
print(sonuc)
