

r=range(10) #Listeyi teker teker yazmak yerine 0-10 arasındaki rakamları yazmanın kısa yolu.
r=range(2,20)#2den başlayarak 20ye kadar 20 stop değeri.
r=range(5,50,5)#5den başla 50de bitir 5er arttır.
r=range(0,-100,-5)#-li değerlerde de geçerli.


sonuc=list(r)
print(sonuc)

for i in range(0,10,2):
    print(i)
