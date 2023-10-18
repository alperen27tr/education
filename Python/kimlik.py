
class Kimlik:
    kayitli_kisi_sayisi=0
    def __init__(self,TCno,Name,City):
        self.tcno=TCno
        self.name=Name
        self.city=City
        Kimlik.kayitli_kisi_sayisi+=1

isim = input("1.isim giriniz: ")
tcno = input("1.tcno giriniz: ")
sehir = input("1.sehir giriniz: ")
person1=Kimlik(tcno,isim,sehir)


isim = input("2.isim giriniz: ")
tcno = input("2.tcno giriniz: ")
sehir = input("2.sehir giriniz: ")
person2=Kimlik(tcno,isim,sehir)


print(person1.name)
print(person2.city)
print(f'Sisteme kayıtlı kişi sayısı: ',Kimlik.kayitli_kisi_sayisi)
        
		