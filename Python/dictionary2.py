urunler={
    100:{
        "UrunAdi" : "Monitor",
        "UrunAcıklaması":"16 inç",
        "GarantiSuresi": 3,
        "Fiyati":[800,1200]
    },
    101:{ "UrunAdi" : "SSD",
        "UrunAcıklaması":"256GB",
        "GarantiSuresi": 2,
        "Fiyati":[1500,2000]}
}

sonuc0=urunler[100]#100 numaralı ürün hakkında bilgiler getirir.
sonuc1=urunler[100]["GarantiSuresi"]#100 numaralı ürünün sadece garanti süresini getirir.
sonuc2=urunler[101]["Fiyati"]

tutar=urunler[100]["Fiyati"][1]+urunler[101]["Fiyati"][1]


print(sonuc0)
print(sonuc1)
print(sonuc2)
print(tutar)
sonuc3=urunler[100]["GarantiSuresi"]
print(sonuc3)