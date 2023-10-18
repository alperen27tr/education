

sayilar=[2,85,96,34,56,71,13]
harfler=["v","s","a","k","y"]
isimler=["ali","veli","alp","eren","alper"]

sonuc0=min(sayilar)
sonuc1=max(sayilar)

sonuc2=min(harfler)
sonuc3=max(harfler)

sonuc4=min(isimler)
sonuc5=max(isimler)
sonuc6=[len(isim) for isim in isimler] #isimlerin harf sayılarını listeler.

print(sonuc0)
print(sonuc1)
print(sonuc2)
print(sonuc3)
print(sonuc4)
print(sonuc5)
print(sonuc6)


araclar=[
    {"title":"Audi A6","price":400000},
    {"title":"Mercedes E","price":700000},
    {"title":"BMW 520", "price":500000}
]

sonuc7 = min(araclar, key=lambda urun: urun["price"])
sonuc8 = max(araclar, key=lambda urun: urun["price"])

print(sonuc7)
print(sonuc8)





