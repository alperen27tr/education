import random

sonuc=random.random() #0.0-1.0 arasi sayi uretir.
print(sonuc)

sonuc0 = random.random()*10 #1.0-10.0 arasi sayi uretir.
print(sonuc0)

sonuc1=int(random.uniform(10,100)) #10-100 arasi tam sayi uretir.
print(sonuc1)

sonuc2=random.randint(1,100) #1-100 arasindan tam sayi 
print(sonuc2)

users=["alp","eren","alper","selma","yagiz","dilay"]
sonuc3= users[random.randint(0,len(users)-1)]#liste eleman sayisindan 1 cikardik cunku index sayisi uyusmaz.
print(sonuc3)

sonuc4= random.choice(users) #16.satirin kisa versiyonu
print(sonuc4)

isim="ALPEREN"
sonuc5=random.choice(isim) #ismin icinden rastgele bir harf secer
print(sonuc5)

liste=list(range(10))
random.shuffle(liste)#listeyi karistirir
print(liste)

liste0=list(range(100))
sonuc6=random.sample(liste0,5) #listenin icinden 5 eleman secer.
print(sonuc6)