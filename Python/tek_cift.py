sayi1=int(input("Birinci Sayı: "))
sayi2=int(input("İkinci Sayı: "))

for i in range(sayi1,sayi2):
    if i %2== 0:
        print (f'Çift sayılar: {i}')

for i in range(sayi1,sayi2):
    if i %2==1:
        print (f'Tek sayılar: {i}')

for sayi0 in range(sayi1,sayi2 ):
    if sayi0 > 1:
        for i in range(2, sayi0):
            if (sayi0 % i) == 0:
                break
        else:
            print(f'Asal sayılar: ',sayi0)

