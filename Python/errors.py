#! /usr/bin/env python
#! _*_coding: UTF8 _*_

try: # Hata olabilecek blok
    a=int(input("Sayı1: "))
    b=int(input("Sayı2: "))
    print(a+b)
    
except: #Hata mesajı
    print("Hata oluştu !")