araclar= [
    {"title":"Audi A4", "price":600000 },
    {"title":"Mercedes E","price":400000 },
    {"title":"BMW 520", "price": 900000}
]
sonuc0=sorted(araclar, key=lambda arac: arac["price"]) # sorted value'lere göre sıralama yapar.


print(sonuc0)