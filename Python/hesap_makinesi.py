from math import * 

print("Hesap makinesine hoşgeldiniz")

sayi1=int(input("ilk sayıyı giriniz: "))
sayi2=int(input("ikinci sayıyı giriniz: "))

print(""" 
      Toplama yapmak için: 1
      Çıkarma yapmak için: 2
      Çarpma yapmak için: 3
      Bölme yapmak için: 4
      """)

yapilmakistenenislem = input(str("Yapilmak istenen islemi giriniz: "))

if yapilmakistenenislem=="1":
      print(f'sonuç: ',sayi1+sayi2)
      
if yapilmakistenenislem=="2":
      print(f'sonuç: ',sayi1-sayi2)

if yapilmakistenenislem=="3":
      print(f'sonuç: ',sayi1*sayi2)

if yapilmakistenenislem=="4":
      print(f'sonuç: ',sayi1/sayi2)
else:
      print("Hatali karakter!")

                    

    
