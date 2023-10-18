
yazı="Benim adım Alperen ERDOĞAN".split()

print(yazı[2][2])#Yazının 2.indexinin 2.harfini söyler. Not: Rakamlar 0'dan başlar.

isimler=["Alperen","İsmet","Ahmet","Mustafa"]
sonuc= isimler[0] #Listenin içinden 0.indeksi çağırır.

print(sonuc)

iller=["Ankara","Kayseri","Gaziantep","Adana"]
sonuc1=iller[0:2]#Liste içinden 0-2 aralığındaki indexleri yazar.
sonuc1=iller[:3]#Liste içinden 0-3 aralığındaki indexleri yazar.
iller[0]="Van"#Liste içinde 0.index yerine Van yaz.
sonuc2=len(iller)#Listede kaç eleman olduğunu söyler.

print(sonuc2)

iller1=["Van","Diyarbakır","Bitlis","Ağrı,"]
sonuc3= iller1 + iller 
print(sonuc3)

sonuc4= iller1 + ["Muş","Balıkesir"]
print(sonuc4)

del iller1[0]#0.indeks silinir.
del iller1[0:2]
print(iller1)