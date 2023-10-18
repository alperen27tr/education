
print("Alp Ustanın Mekanına Hoşgeldiniz...")

boyut=input("""Lütfen lahmacununuzun boyunu seçiniz... 
S için : 1
M için : 2
L için : 3'e tıklayınız.
 """)

acili=input("Acı istermisiniz? ")
icecek=input("İcecek istermisiniz? ")
tutar=0

if boyut=="1":
    
    tutar=+20
elif boyut=="2":
    
    tutar=+30
else :
    
    tutar=+40

if acili=="evet":
   
   tutar= tutar + 5
else :
   pass

if icecek=="evet":
    tutar+=10
else:
    pass


print(tutar)
