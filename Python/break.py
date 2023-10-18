isim="Alperen Erdoğan"
for harf in isim:
    if (harf=="ğ"): # ğ harfine gelince döngüyü kes.
        break
    print(harf)


i=0
while(i<10):
    print(i)
    i+=1
    if(i==6):
        break

#1-100 arası çift sayıların toplamı
    i=0
    toplam=0
    while (i<=100):
        i+=1
        if (i%2==1):
            continue
        toplam+=i
print(f'toplam:{toplam}')


