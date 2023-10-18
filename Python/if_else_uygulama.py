#! /usr/bin/env python
#! _*_coding: UTF8 _*_


#UYGULAMA3 EHLİYET SORGULAMA 

isim= input("isim: ")
yas=int(input("yas: "))
egitim=input("egitim:" )
print(egitim.lower())
if (yas>=18):
    if(egitim.lower()=="lise" or egitim=="universite" or egitim== "yukseklisans"):
        print("ehliyet alabilirsiniz")
    else:
        print(f'{isim} egitim durumunuz yetersiz oldugundan ehliyet alamazsiniz.')
else:
    print("Yasınız kucuk oldugundan ehliyet alamazsiniz.")



    
