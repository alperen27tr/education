sayılar=[2,45,90,56,43,59]
print(sum(sayılar)) #sayılar içindeki tüm sayıları toplar
print(sum(sayılar,100))#100 ekledi


urunler=[
    {"tittle":"kitap a","price":35},
    {"tittle":"kitap b","price":20},
    {"tittle":"kitap c", "price":45}
]
toplamFiyat=sum([urun["price"]for urun in urunler]) 
print(toplamFiyat) 

sonuc= round(4.7) #ondalıklı sayıları tam sayılara yuvarlar.
print(sonuc)