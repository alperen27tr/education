import random

sayi=random.randint(0,100)
girilen_sayi=int(input("Tahmin: "))
adim_sayisi=0
def tahmin(girilen_sayi,adim_sayisi):
   
    if girilen_sayi < sayi:
        girilen_sayi= int(input("Sayıyı Büyült"))
        adim_sayisi=int(adim_sayisi)+1
   
    if girilen_sayi > sayi:     
        girilen_sayi=int(input("Sayıyı Küçült"))
    adim_sayisi=int(adim_sayisi)+1
   
    if girilen_sayi == sayi:
        (print("Tebrikler..."))  
        print(int(adim_sayisi) )
        return 
   
    tahmin(girilen_sayi,adim_sayisi)
tahmin(girilen_sayi,adim_sayisi)
