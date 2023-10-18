kare=1
ucgen=2
dikdortgen=3

istenen_sekil=input("Kare icin:1 , Ucgen icin:2, dikdortgen icin:3...")

istenen_sekil={
   kare:1,
   ucgen:2,
   dikdortgen:3
   }
     
if istenen_sekil==1:
    a=input(int("Bir kenari: "))
    print(a*a)
else:
    print("Hatali islem...")

if istenen_sekil==2:
    b=input("Taban uzunlugu: ")
    c=input("Yukseklik: ")
    print(b*c/(2))
else:
    print("Hatali islem...")

                
