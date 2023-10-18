

ArabaAudi={
    "marka":"Audi",
    "yıl" : 2019,
    "renk":"siyah",
}
sonuc=ArabaAudi["marka"]
print("ac1",sonuc)
sonuc=ArabaAudi.get("yıl")
print("ac2",sonuc)
sonuc="renk" in ArabaAudi #Sorgulama işlemleri
print("ac",sonuc)
sonuc=len(ArabaAudi)#ArabaAudi içinde kaç değer var.
print("renk",sonuc)
ArabaAudi["Model"]="A5"#Listeye sonradan değer ekler.
ArabaAudi.pop("yıl")#Yılı siler.
del ArabaAudi["renk"]
# del ArabaAudi          #ArabaAudinin tamamı silinir.
ArabaAudi.clear() #ArabaAudinin içindeki değerleri siler.


print(ArabaAudi)
print(sonuc)