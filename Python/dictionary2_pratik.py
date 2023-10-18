urunler={
    100:{
        "urun marka":"Samsung",
        "urun model":"Galaxy S8",
        "urun yıl":"2018",
        "urun garanti":"2",
        "urun fiyat":[2000,2500]
    },
    101:{
        "urun marka":"Apple",
        "urun model":"Iphone X",
        "urun yıl":"2019",
        "urun garanti":"3",
        "urun fiyat":[3000,4500]
    }
}
tutar=urunler[100]["urun fiyat"][1]+urunler[101]["urun fiyat"][1]
print(tutar)
sonuc0=urunler[101]["urun model"]+ urunler[101]["urun garanti"]
print(sonuc0)
sonuc1=urunler[100]["urun garanti"]
print(sonuc1)
