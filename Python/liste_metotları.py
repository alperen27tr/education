
sayılar=[1,3,5,10,25,36]
harfler=["a","d","f","k","n","y"]

sonuc1=min(sayılar)
sonuc2=max(sayılar)
sonuc3=min(harfler)#Alfabeye göre en baştaki harfi çağırır.
sonuc4=max(harfler)#Alfabeye göre en sondaki harfi çağırır.

print(sonuc1,sonuc2,sonuc3,sonuc4)

sayılar0=[1,2,4,5,6,8,9]
harfler0=["a","b","c"]
sayılar0.append(3)#Listenin sonuna 3 rakamını ekler.

harfler0.append("z")#Listenin sonuna z harfini ekler.

print("aaa",sayılar0,harfler0)

sayılar1=[10,20,40,50]
harfler1=["A","B","C","D"]
sayılar1.insert(2,30)#2.indexe"30"sayısını getirir.(indexler 0'dan başlar.)
harfler1.insert(4,"E")

print(sayılar1,harfler1)

sayılar2=[11,22,33,44,55]
harfler2=["q","a","z"]
sayılar2.pop(0)#Parantez içine kaçnıcı index silincekse o yazılır.
harfler2.remove("q")#Parantez içine doğrudan hangi eleman silincekse o yazılır.
harfler2.pop(0)
print("aaaa",sayılar2,harfler2)

sayılar3=[100,23,97,295,3,51]
harfler3=["i","f","l","o","a","z"]
harfler3.sort()#Harfleri alfabetik sıralar.
sayılar3.sort()#Sayıları küçükten büyüge sıralar.


print(sayılar3,harfler3)

sayılar4=[2,4,6,8,10,12,14]
harfler4=["s","h","f","z","p"]
sayılar4.reverse()#Sayıları büyükten küçüğe sıralar.
harfler4.reverse()

print(sayılar4,harfler4)

sayılar5=[10,20,30,10,40,10,70,20]
print(len(sayılar5))

print(sayılar5.count(10))#10 sayısı kaç defa geçiyor onu söyler.
print(sayılar5.index(30))#30 sayısının kaçınıcı indexte olduğunu söyler.
print(sayılar5.clear())#Listeyi boş gösterir.