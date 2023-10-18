
ArabaAudi={
    "model":"A5",
    "yıl":2019,
    "renk":"siyah"
}
Araba=ArabaAudi.copy()#Yeni bir "araba" değişkeni içinde "ArabaAudi"'yi kopyalama.
Araba["model"]="A7" #Yeni değişkende herhangi bir maddeyi değiştirme.
Araba["renk"]="beyaz"

ArabaAudi.update({     #Güncelleme
    "yıl":2020,
    "renk":"Mavi"
})

print(Araba)
print(ArabaAudi)

