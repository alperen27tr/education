
sayilar=[]
for i in range(10):
    sayilar.append(i)
print(sayilar)


sayilar0=[i for i in range(10)]
sayilar1=[i*2 for i in range(10)]
sayilar2=[i*i for i in range(10)]

print(sayilar0)
print(sayilar1)
print(sayilar2)

isim="Alperen"

sonuc= [a.upper() for a in isim ]
sonuc0=[i.lower() for i in isim ]

print(sonuc)
print(sonuc0)