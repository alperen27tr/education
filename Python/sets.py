#Setler indexlenemez,sıralanamaz.
#Setlerde sıralama önemsizdir,karışıktır.

markalar={"Audi","Mercedes","Bmw","Honda"}
markalar2={"Mazda","ferrari"}

sonuc="Honda" in markalar
markalar.add("Opel")#"Markalar" içine yeni madde ekleme.
markalar.update(["Skoda","Toyota"])#"Markalar" içine yeni maddeler ekleme.(Güncelleme)
sonuc0=len(markalar)#Markalar içinde kaç madde var.
markalar.remove("Mercedes")
sonuc=markalar.pop()#Rastgele bir maddeyi siler.Silinen madde terminalde gözükür.
sonuc1=markalar.union(markalar2)


print(sonuc1)
print(sonuc0)
print(sonuc)
print(markalar)