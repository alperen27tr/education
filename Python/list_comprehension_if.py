
sayılar=[1,3,4,10,23,74,93]
sonuc=[]

for sayı in sayılar:
    if (sayı%2==0):
        sonuc.append(sayı)
        print("sayı çift")
    else:
        print("sayı tek")

