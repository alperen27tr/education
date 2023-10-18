#! /usr/bin/env python
#! _*_coding: UTF8 _*_

sonuc0=all([True,False,True,True]) #all hepsinin true olması lazım
sonuc1=any([True,False,False,True])#any herhangi biri true olması yeterli

print(sonuc0,sonuc1)

sayilar=[0,12,23,34,45,56,67,78]

sonuc0= [bool(sayi) for sayi in sayilar]
sonuc1=any([bool(sayi) for sayi in sayilar])
sonuc2=all([bool(sayi) for sayi in sayilar])
sonuc3=all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc4=all(sayi%2==0 for sayi in sayilar )
sonuc5=any(sayi%2==0 for sayi in sayilar )

print(sonuc0)
print(sonuc1)
print(sonuc2)
print(sonuc3)
print(sonuc4)
print(sonuc5)


isimler=["alper","sude","mehmet","arda","ali"]

sonuc0=[isim[0]=="a"for isim in isimler] 
sonuc1=any([isim[0]=="k" for isim in isimler])


print(sonuc0)
print(sonuc1)